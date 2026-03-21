resource "aws_key_pair" "deployer" {
  key_name   = "terra-key-ec2"
  public_key = file("./terra-key-ec2.pub")
}

resource "aws_default_vpc" "default" {
  tags = {
    Name = "Default VPC"
  }
}

resource "aws_default_subnet" "public_ip" {
  availability_zone = "ap-south-1a"
  
  # IMPORTANT: Set this to false to override the default behavior.
  map_public_ip_on_launch = true 

  tags = {
    Name = "Default Subnet"
  }
}

resource "aws_security_group" "my-sg" {
  name        = "my_instane_sg"
  description = "Allow TLS inbound traffic and all outbound traffic"
  vpc_id      = aws_default_vpc.default.id  #interpolation

  tags = {
    Name = "my_instane_sg"
  }
}

resource "aws_security_group_rule" "my-sg-rule_ssh" {
  type              = "ingress"
  from_port         = 22
  to_port           = 22
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.my-sg.id
  description = "Allow ssh access"
}

resource "aws_security_group_rule" "my-sg-rule_http" {
  type              = "ingress"
  from_port         = 80
  to_port           = 80
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.my-sg.id
  description = "Allow http access"
}

# resource "aws_security_group_rule" "my-sg-rule_custom_http" {
#   type              = "ingress"
#   from_port         = 8080
#   to_port           = 8080
#   protocol          = "tcp"
#   cidr_blocks       = ["0.0.0.0/0"]
#   security_group_id = aws_security_group.my-sg.id
#   description = "Allow custom tcp access"
# }

# resource "aws_security_group_rule" "my-sg-rule_https" {
#   type              = "ingress"
#   from_port         = 443
#   to_port           = 443
#   protocol          = "tcp"
#   cidr_blocks       = ["0.0.0.0/0"]
#   security_group_id = aws_security_group.my-sg.id
#   description       = "Allow https access (TLS)"
# }

resource "aws_security_group_rule" "my-sg-rule-out1" {
  type              = "egress"
  from_port         = 0      # All ports (when protocol is -1)
  to_port           = 0      # All ports (when protocol is -1)
  protocol          = "-1"   # All protocols
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = aws_security_group.my-sg.id
  description = "Outbound Internet access"
}


resource "aws_instance" "my_instance" {
  for_each = tomap({
    Instance1 = "c7i-flex.large"
  })

  key_name = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.my-sg.id]
  instance_type = each.value
  ami = "ami-019c927fb527c7c37" #Amazon Linux 2023 kernel-6.1 AMI
  availability_zone = "ap-south-1a"
  root_block_device {
    volume_size = var.env == "prod" ? 30 : var.root_volume_size
    volume_type = "gp3"
  }

  subnet_id = aws_default_subnet.public_ip.id
  associate_public_ip_address = true
  user_data = file("install_apps.sh")
  tags = {
    Name = each.key
    Dept = "Operations"
  }
  depends_on = [ aws_security_group.my-sg, aws_key_pair.deployer ]
}

resource "null_resource" "copy_files" {

  for_each = aws_instance.my_instance
  depends_on = [aws_instance.my_instance]

  connection {
    type        = "ssh"
    host        = each.value.public_ip
    user        = "ec2-user"
    private_key = var.private_key
  }

  # Copy install script
  provisioner "file" {
    source      = "./install_apps.sh"
    destination = "/tmp/install_apps.sh"
  }

  # Install nginx and docker
  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/install_apps.sh",
      "sudo /tmp/install_apps.sh"
    ]
  }

  # Copy docker-compose.yml
  provisioner "file" {
    source      = "./docker-compose.yml"
    destination = "/home/ec2-user/docker-compose.yml"
  }

  # Copy nginx config
  provisioner "file" {
    source      = "./default.conf"
    destination = "/tmp/default.conf"
  }

  # Apply nginx config
  provisioner "remote-exec" {
    inline = [
      "sudo mv /tmp/default.conf /etc/nginx/conf.d/default.conf",
      "sudo nginx -t",
      "sudo systemctl restart nginx"
    ]
  }
}


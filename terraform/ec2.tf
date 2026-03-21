resource "aws_key_pair" "deployer" {
  key_name   = "terra-key-ec2"
  public_key = file("terra-key-ec2.pub")
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
    #Instance2 = "t3.micro"
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

# resource "local_file" "foo" {
#   filename        = "services"
#   file_permission = "0700"
#   content = <<-EOF
# This file is created with terraform on ${timestamp()}.
# ------------------------------------------------------
# Service Configuration Details:

# ${join("\n",[ for key,instance in aws_instance.my_instance: 
# "Instance key:  ${key}\nInstance ID:  ${instance.id}\nInstance Name: ${instance.tags.Name}\nDept: ${instance.tags.Dept}"])}

# VPC ID: ${aws_default_vpc.default.id}
# VPC Name: ${aws_default_vpc.default.tags.Name}
# Security Group ID: ${aws_security_group.my-sg.id}
# Security Group Name: ${aws_security_group.my-sg.name}
# Key Pair Name: ${aws_key_pair.deployer.key_name}

# The file permissions are set to 0700.
# EOF
# }


resource "null_resource" "copy_files" {

  for_each = aws_instance.my_instance
  depends_on = [aws_instance.my_instance]

  connection {
    type        = "ssh"
    host        = each.value.public_ip
    user        = "ec2-user"
    private_key = file("./terra-key-ec2")
  }

  # Step 1: Copy script
  provisioner "file" {
    source      = "./install_apps.sh"
    destination = "/tmp/install_apps.sh"
  }

  # Step 2: Execute script
  provisioner "remote-exec" {
    inline = [
      "chmod +x /tmp/install_apps.sh",
      "sudo /tmp/install_apps.sh"
    ]
  }

}


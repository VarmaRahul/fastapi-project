output "ec2_private_ip" {
    value = [
        for key, instance in aws_instance.my_instance : instance.private_ip
    ]
    description = "A list of private IPs for all EC2 instances."
}

output "ec2_public_ip" {
  value = [
    for key, instance in aws_instance.my_instance : instance.public_ip
  ]
  description = "A list of public IPs for all EC2 instances."
}

output "website" {
  value = [
    for key, instance in aws_instance.my_instance : "http://${instance.public_ip}"
  ]
  description = "Website URLs for all EC2 instances."
}

output "server-access" {
  value = [
    for key, instance in aws_instance.my_instance : "ssh -i ./terra-key-ec2 ubuntu@${instance.public_ip}"
  ]
  description = "ssh command to server"
}

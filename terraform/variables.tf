variable "env" {
    description = "my env name"
    type = string
    default = "prod"
}

variable "root_volume_size" {
    description = "my root volume size"
    type = number
    default = 20
}

variable "private_key" {
  description = "Private key for EC2 SSH"
  type        = string
  sensitive   = true
}

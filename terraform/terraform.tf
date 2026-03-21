terraform {
  backend "s3" {
    bucket         = "vvvrahul-state-bucket"
    key            = "fastapi-app/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "state-table"
    encrypt        = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.18.0"
    }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.2"
    }
  }
}

provider "aws" {
  # Configuration options
  region = "ap-south-1"
}
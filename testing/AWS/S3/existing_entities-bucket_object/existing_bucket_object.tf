terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.20.0"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
    region     = "us-west-1"
    access_key = "${var.access_key}"
    secret_key = "${var.secret_key}"
}


resource "aws_s3_bucket" "newbucket" {
    bucket =  "${var.existing_bucket_name}"
}

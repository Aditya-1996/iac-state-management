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
    bucket =  "${var.new_bucket_name}"
}

resource "aws_s3_bucket" "newbucket2" {
    bucket =  "${var.new_bucket2_name}"
    acl = "public-read"
}

/*
resource "aws_s3_bucket_policy" "example_bucket_policy" {
  bucket = aws_s3_bucket.example_bucket.id

  policy = jsonencode({
    Version = "2023-02-07"
    Statement = [
      {
        Effect = "Allow"
        Principal = "*"
        Action = [
          "s3:GetObject",
          "s3:PutObject"
        ]
        Resource = [
          "${aws_s3_bucket.example_bucket.arn}/*"
        ]
      }
    ]
  })
}
*/

resource "aws_s3_bucket_object" "bucket2object" {
    bucket =  aws_s3_bucket.newbucket2.id
    key = "Adi_Resume.pdf"
    source = "Adi_Resume.pdf"
}

resource "aws_s3_bucket_object_lock_configuration" "resumelock" {
  bucket = aws_s3_bucket.example.id

  rule {
    default_retention {
      mode = "COMPLIANCE"
      days = 1
    }
  }
}




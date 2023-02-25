# Improving State Management in IaC

IAC-state-management project attempts to find ways to improve state management in Infrastrcuture as a Code applications. In this case, we specifically examine Terraform's state management system, and see how I can attempt to improve the various issues with state management in IaC.

## Getting Started

Index of Contents:

1. testing - 
    Shall contain files that are being tested for a custom - user or client driven solution.
    These files are mostly in terraform and related support files. 
2. dev - 
    Shall contain python files that are used to develop the 

### Prerequisites

The things you need before installing the software.

* A cloud provider account - This project relies primarily on AWS, but also Azure to test; This project runs the test on Object Store - AWS's S3 and Azure's Blob storage
* Terraform - installation instructions link below
* Files - Objects/Blobs to insert into the cloud environment to test. I'm currently using a resume file

### Installation and use

1. Install Terraform 

Terraform installation instructions - https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli

2. Once terraform is installed, run the following commands in order 

    * terraform init
        Generates the binaries and installs the provider on your local. 
    * terraform plan
        Generates and displays a plan to apply and build infrastructure. 
    * terraform apply
        Applies the infrastrcuture and creates the entities on the cloud provider server.


## Additional Documentation and Acknowledgments

* Project guide - Professor Dr. Chen Qian
* Project reader - Professor Dr. Heiner Litz

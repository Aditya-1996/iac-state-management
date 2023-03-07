
'''
File name: s3_bucket_creation_event_lamda_trigger.py
Author: adravish@ucsc.edu
Python Version: 3.9.10

Description: This python file captures an S3 bucket creation event and writes the details about the creation to an S3 file - which is a Terraform State file

Functions:
- lambda_handler(): loads an event and writes to the Terraform state file within S3

Imported Library/Modules:
- boto3: AWS specific library that is used to interact with AWS services. Here, we are using it to capture a bucket creation event
- json: Used to handle json inputs/outputs formatting
'''


import boto3
import json



s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

def lambda_handler(event, context):

    '''
    Function name: lambda_handler
    Author: adravish@ucsc.edu
    Python Version: 3.9.10

    Description: loads an event and writes to the Terraform state file within S3

    Input:
    - event: The S3 bucket creation event (can be extended to other S3 events later)
    - context: The context metadata for capturing the event

    Output:
    - The sum of a and b (int or float)
    '''


    # Read S3 bucket name just created
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    #object_key_name = e vent['Records'][0]['s3']['object']['key']
    

    '''Read the existing file as an object and convert it to json'''
    # Read the Terraform state file as an object
    cur_state_object = s3.get_object(Bucket='adi-tf-state-bucket', Key='terraform.tfstate')
    # Conver the object to json format
    cur_state_json = json.loads(cur_state_object['Body'].read().decode('utf-8'))
    


    # Check if the 'aws_s3_bucket' resource is already defined in the state file
    if 'aws_s3_bucket' not in cur_state_json['resources']:
        
        # Create a new 'aws_s3_bucket' resource and add the newly created bucket to it
        new_aws_s3_bucket_with_bucket_name = {
            "mode": "managed",
            "type": "aws_s3_bucket",
            "name": "my_bucket",
            "provider": "provider.aws",
            "instances": [
                {
                    "attributes": {
                        "bucket": bucket_name
                    }
                }
            ]
        }

        #add the new s3 bucket resource to the json
        cur_state_json['resources']['aws_s3_bucket.my_bucket'] = new_aws_s3_bucket_with_bucket_name
        
    else:
        # Update the existing 'aws_s3_bucket' resource to include the newly created bucket
        cur_state_json['resources']['aws_s3_bucket.my_bucket']['instances'][0]['attributes']['bucket'] = bucket_name
    
    # Write the updated state file back to S3
    Body=json.dumps(cur_state_json, indent=4)
    s3_resource.Object('adi-tf-state-bucket', 'terraform.tfstate').put(Body)

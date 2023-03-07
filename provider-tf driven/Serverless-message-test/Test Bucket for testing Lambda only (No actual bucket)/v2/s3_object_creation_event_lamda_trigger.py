'''
File name: s3_object_creation_event_lamda_trigger.py
Author: adravish@ucsc.edu
Python Version: 3.9.10

Description: This python file captures an S3 bucket creation event and writes the details about the creation to an S3 file - which is a Terraform State file

Functions:
- lambda_handler(): loads an event and writes to the Terraform state file within S3

Imported Library/Modules:
- boto3: AWS specific library that is used to interact with AWS services. Here, we are using it to capture a bucket creation event
- json: Used to handle json inputs/outputs formatting
- os 
'''

import json
import boto3

s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

def lambda_handler(event, context):



    # Check if the resource already exists in the state file
    resource_exists = False


    '''Read the existing file as an object and convert it to json'''
    # Read the Terraform state file as an object
    cur_state_object = s3.get_object(Bucket='adi-tf-state-bucket', Key='terraform.tfstate')
    # Conver the object to json format
    cur_state_json = json.loads(cur_state_object['Body'].read().decode('utf-8'))
    

    # Check if the new aws_s3_bucket_object resource already exists in the state file 
    for resource in cur_state_json['resources']:
        if resource['type'] == 'aws_s3_bucket_object':
            if resource['name'] == event['detail']['object']['key']:
                resource_exists = True
                break
            


    # Create a new aws_s3_bucket_object resource in the state file if it doesn't exist
    if not resource_exists:
        
        #create new json with the object resource
        new_aws_s3_object_resource_with_name = {
            "mode": "managed",
            "type": "aws_s3_bucket_object",
            "name": event['detail']['object']['key'],
            "values": {
                "bucket": event['detail']['bucket']['name'],
                "key": event['detail']['object']['key'],
            }
        }

        cur_state_json['resources'].append(new_aws_s3_object_resource_with_name)
    
    
    ''' 
        Write the updated state file to S3
    '''
    s3.put_object(Bucket='adi-tf-state-bucket', Key='terraform.tfstate', Body=json.dumps(cur_state_json))
    

    ''' 
        Return state to Lambda
    '''
    return {
        'statusCode': 200,
        'body': json.dumps('Terraform state file updated successfully with new object')
    }
import json

state = {
  "version": 4,
  "terraform_version": "1.3.9",
  "serial": 8,
  "lineage": "323a9c10-400e-ea55-88c7-d43b19b1926f",
  "outputs": {},
  "resources": [
    {
      "mode": "managed",
      "type": "aws_s3_bucket",
      "name": "newbucket",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "acceleration_status": "",
            "acl": null,
            "arn": "arn:aws:s3:::adiprojectbucket2",
            "bucket": "adiprojectbucket2",
            "bucket_domain_name": "adiprojectbucket2.s3.amazonaws.com",
            "bucket_prefix": null,
            "bucket_regional_domain_name": "adiprojectbucket2.s3.us-west-1.amazonaws.com",
            "cors_rule": [],
            "force_destroy": false,
            "grant": [
              {
                "id": "a1bd360e4da349013b2b866b39e3431a1e73c8d99fb10b4e60191c398e66a1b1",
                "permissions": [
                  "FULL_CONTROL"
                ],
                "type": "CanonicalUser",
                "uri": ""
              }
            ],
            "hosted_zone_id": "Z2F56UZL2M1ACD",
            "id": "adiprojectbucket2",
            "lifecycle_rule": [],
            "logging": [],
            "object_lock_configuration": [],
            "object_lock_enabled": false,
            "policy": "",
            "region": "us-west-1",
            "replication_configuration": [],
            "request_payer": "BucketOwner",
            "server_side_encryption_configuration": [
              {
                "rule": [
                  {
                    "apply_server_side_encryption_by_default": [
                      {
                        "kms_master_key_id": "",
                        "sse_algorithm": "AES256"
                      }
                    ],
                    "bucket_key_enabled": false
                  }
                ]
              }
            ],
            "tags": {},
            "tags_all": {},
            "versioning": [
              {
                "enabled": false,
                "mfa_delete": false
              }
            ],
            "website": [],
            "website_domain": null,
            "website_endpoint": null
          },
          "sensitive_attributes": [],
          "private": "bnVsbA=="
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_s3_bucket",
      "name": "newbucket2",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "acceleration_status": "",
            "acl": null,
            "arn": "arn:aws:s3:::adiprojectbucket3",
            "bucket": "adiprojectbucket3",
            "bucket_domain_name": "adiprojectbucket3.s3.amazonaws.com",
            "bucket_prefix": null,
            "bucket_regional_domain_name": "adiprojectbucket3.s3.us-west-1.amazonaws.com",
            "cors_rule": [],
            "force_destroy": false,
            "grant": [
              {
                "id": "a1bd360e4da349013b2b866b39e3431a1e73c8d99fb10b4e60191c398e66a1b1",
                "permissions": [
                  "FULL_CONTROL"
                ],
                "type": "CanonicalUser",
                "uri": ""
              }
            ],
            "hosted_zone_id": "Z2F56UZL2M1ACD",
            "id": "adiprojectbucket3",
            "lifecycle_rule": [],
            "logging": [],
            "object_lock_configuration": [],
            "object_lock_enabled": false,
            "policy": "",
            "region": "us-west-1",
            "replication_configuration": [],
            "request_payer": "BucketOwner",
            "server_side_encryption_configuration": [
              {
                "rule": [
                  {
                    "apply_server_side_encryption_by_default": [
                      {
                        "kms_master_key_id": "",
                        "sse_algorithm": "AES256"
                      }
                    ],
                    "bucket_key_enabled": false
                  }
                ]
              }
            ],
            "tags": {},
            "tags_all": {},
            "versioning": [
              {
                "enabled": false,
                "mfa_delete": false
              }
            ],
            "website": [],
            "website_domain": null,
            "website_endpoint": null
          },
          "sensitive_attributes": [],
          "private": "bnVsbA=="
        }
      ]
    },
    {
      "mode": "managed",
      "type": "aws_s3_bucket_object",
      "name": "bucket2object",
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",
      "instances": [
        {
          "schema_version": 0,
          "attributes": {
            "acl": "private",
            "bucket": "adiprojectbucket3",
            "bucket_key_enabled": false,
            "cache_control": "",
            "content": null,
            "content_base64": null,
            "content_disposition": "",
            "content_encoding": "",
            "content_language": "",
            "content_type": "binary/octet-stream",
            "etag": "4ce99fc82aa2b99ae4c9f2b709484eac",
            "force_destroy": false,
            "id": "Adi_Resume.pdf",
            "key": "Adi_Resume.pdf",
            "kms_key_id": null,
            "metadata": null,
            "object_lock_legal_hold_status": "",
            "object_lock_mode": "",
            "object_lock_retain_until_date": "",
            "server_side_encryption": "AES256",
            "source": "Adi_Resume.pdf",
            "source_hash": null,
            "storage_class": "STANDARD",
            "tags": null,
            "tags_all": {},
            "version_id": "",
            "website_redirect": ""
          },
          "sensitive_attributes": [],
          "private": "bnVsbA==",
          "dependencies": [
            "aws_s3_bucket.newbucket2"
          ]
        }
      ]
    }
  ],
  "check_results": null
}


with open("terraform.tfstate", "w") as f:
    json.dump(state, f, indent=2)

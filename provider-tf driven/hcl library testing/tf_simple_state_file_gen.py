import json
import hcl2

# Define the path to the Terraform configuration file
terraform_config_file_path = "/path/to/terraform/config.tf"

# Read the Terraform configuration file
with open(terraform_config_file_path, "r") as f:
    config = hcl2.load(f)

# Generate the state file
state = {}
for resource_type, resources in config.items():
    state[resource_type] = {}
    for resource_name, resource_config in resources.items():
        state[resource_type][resource_name] = {
            "id": "resource_id",
            "attributes": resource_config
        }

# Serialize the state file to JSON
state_json = json.dumps(state, indent=2)

# Write the state file to disk
with open("terraform.tfstate", "w") as f:
    f.write(state_json)

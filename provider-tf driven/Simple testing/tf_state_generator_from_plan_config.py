import json

'''
# # Load Terraform configuration file
# with open("new_bucket_object.tf", "r") as f:
#     config = f.read()

# # # Run Terraform plan command to generate plan output
# # # Replace "terraform plan -out=plan.tfout" with the appropriate command for your setup
# import subprocess
# subprocess.run("terraform plan -out=plan.tfout", shell=True)
'''

# Load plan output file
with open("plan.tfout", "r") as f:
    planfile = json.load(f)

# Extract resource changes from plan output
resource_changes = planfile["resource_changes"]
resources = []
for change in resource_changes:
    if change["type"] == "aws_s3_bucket": 
        resources.append({
            "mode": "managed",
            "type": change["type"],
            "name": change["name"],
            "provider": "provider.aws",  
            "instances": [
                {
                    "attributes": change["change"]["after"]
                }
            ],
            "depends_on": []
        })

# Generating tf state 
state = {
    "version": 4,
    "terraform_version": "0.12.24",  # Replace with the appropriate version
    "serial": 1,
    "lineage": "your-lineage-here",
    "outputs": {},
    "resources": resources
}

with open("terraform.tfstate", "w") as f:
    json.dump(state, f, indent=2)

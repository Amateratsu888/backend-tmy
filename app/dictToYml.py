import yaml
import boto3
import os
from os import environ 


def dict_to_yaml_and_upload(input_dict, yaml_file_name, s3_bucket_name, s3_key_prefix):
    try:
        # Convert the dictionary to YAML
        yaml_content = yaml.dump(input_dict, default_flow_style=False, sort_keys=False, indent=2, default_style=None)

        # Save the YAML content to a local file
        local_yaml_file = f"{yaml_file_name}.yml"
        with open(local_yaml_file, 'w') as file:
            file.write(yaml_content)

        print(f"Successfully converted dictionary to YAML and saved to {local_yaml_file}")

        # Upload the YAML file to AWS S3
        s3_client = boto3.client('s3',aws_access_key_id = environ.get('AWS_ACCESS_KEY'),aws_secret_access_key = environ.get('AWS_PRIVATE_KEY'))
        s3_key = os.path.join(s3_key_prefix, f"{yaml_file_name}.yml")
        s3_client.upload_file(local_yaml_file, s3_bucket_name, s3_key)

        print(f"Uploaded {local_yaml_file} to S3 bucket {s3_bucket_name} with key {s3_key}")

        # Delete the local YAML file
        os.remove(local_yaml_file)
        print(f"Deleted {local_yaml_file} from the local directory")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

import json
import os
import boto3

# from botocore.exceptions import NoCredentialsError


def wasabi_auth():
    """
    function to authenticate user on wasabi
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(current_dir, 'wasabi_keys.cfg')

    with open(config_file, 'r') as wasabi_keys:
        wasabi = json.load(wasabi_keys)
        WASABI_ACCESS_KEY = wasabi["key"]
        WASABI_SECRET_KEY = wasabi["secret"]


    # Creating a Session on Wasabi
    # mentioning the endpoint to wasabi, this is insane

    session = boto3.Session(
        aws_access_key_id=WASABI_ACCESS_KEY,
        aws_secret_access_key=WASABI_SECRET_KEY,
    )
    s3 = session.client(
        "s3", endpoint_url="https://s3.ap-southeast-1.wasabisys.com"
    )
    return s3
def wasabi_auth_client():
    pass
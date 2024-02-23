import os

import boto3
from botocore.client import Config


def get_minio_client():
    s3_client = boto3.client(
        "s3",
        endpoint_url=os.getenv("MINIO_ENDPOINT"),
        aws_access_key_id=os.getenv("MINIO_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("MINIO_SECRET_KEY"),
        config=Config(signature_version="s3v4"),
        region_name=os.getenv("MINIO_REGION_NAME"),
    )
    return s3_client

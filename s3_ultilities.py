import logging
import boto3
from botocore.exceptions import ClientError
import os

def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def download_file(file_name, bucket, object_name=None):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.download_file(bucket, object_name, file_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def download_directory(bucketName, remoteDirectoryName):
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucketName) 
    for obj in bucket.objects.filter(Prefix = remoteDirectoryName):
        if not os.path.exists(os.path.dirname(obj.key)):
            os.makedirs(os.path.dirname(obj.key))
        bucket.download_file(obj.key, obj.key)

def upload_directory(bucketName, localDirectoryName):
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucketName) 
    for path, subdirs, files in os.walk(localDirectoryName):
        for file in files:
            filepath = os.path.join(path, file).replace('\\','/')
            print(filepath)
            bucket.upload_file(filepath, filepath)

def delete_file(bucketName, filepath):
    s3_resource = boto3.resource('s3')
    object = s3_resource.Object(bucketName, filepath)
    object.delete()

def init_data(bucket_name, dirs=[]):
    for dir in dirs:
        download_directory(bucket_name, dir)


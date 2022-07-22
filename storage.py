import boto3
import io
from botocore.exceptions import ClientError

class S3:
  def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
    self.s3 = boto3.client('s3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region_name)

  def list_buckets(self):
    response = self.s3.list_buckets()
    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
      print(f'  {bucket["Name"]}')
  
  def store_file(self, file, filename):
    response = self.s3.upload_fileobj(file, "solo2022-chestnut", filename)
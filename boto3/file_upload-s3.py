import boto3
from boto3.s3.transfer import TransferConfig


s3_client = boto3.client('s3')

S3_BUCKET = 'mybucket'
FILE_PATH = '/path/to/file/'
KEY_PATH = "/path/to/s3key/" 

def uploadFileS3(filename):
    config = TransferConfig(multipart_threshold=1024*25, max_concurrency=10,
                        multipart_chunksize=1024*25, use_threads=True)
    file = FILE_PATH + filename
    key = KEY_PATH + filename
    s3_client.upload_file(file, S3_BUCKET, key,
    ExtraArgs={ 'ACL': 'public-read', 'ContentType': 'video/mp4'},
    Config = config,
    Callback=ProgressPercentage(file)
    )

uploadFileS3('upload.mp4')

#!/usr/bin/python

import boto3
import os

s3 = boto3.client('s3')
filename = 'subham.txt'
sent_name = 'mandal.txt'
bucket_name = 'mandbucket'
files = [ f for f in os.listdir('.') if os.path.isfile(f) ]
for file in files:
 print('uploading file {}'.format(file))
 s3.upload_file(file, bucket_name, file)

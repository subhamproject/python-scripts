#!/usr/bin/python

import os
import boto3
region = 'us-west-2'
s3 = boto3.client('s3', region_name=region)
location = {'LocationConstraint': region}
s3.create_bucket(Bucket='mandbucket', CreateBucketConfiguration=location)

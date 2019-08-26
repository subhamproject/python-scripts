#!/usr/bin/python
import boto3

s3 = boto3.client('s3')
r = s3.list_buckets()
buckets = [ bucket['Name'] for bucket in r['Buckets'] ]

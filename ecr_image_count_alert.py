#!/usr/bin/python3

import sys
import boto3
from email.message import EmailMessage
import subprocess

#Global variable for mailing
sender = 'subham@gmail.com'
recevier = 'subham@gmail.com'

#Global list for repo name
repo_name=[]


#Connect to aws account
def connect(region):
  session = boto3.Session(region_name=region)
  ecr = session.client('ecr')
  return ecr

def aws_registry():
  cmd = subprocess.run(args = ["dig", "+short", "registries.devops.lmvi.net", "TXT"],
                              universal_newlines = True,
                              stdout = subprocess.PIPE)
  cmd_out = cmd.stdout.splitlines()
  registry=[]
  for item in cmd_out:
   id,region = item.split(':')
   registry.append({'aws-region':region.replace('"',''), 'aws-account':id.replace('"','')})
  return registry

#Sendmail as alert
def sendEmail(sender, recevier, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['From'] = sender
    msg['To'] = recevier
    msg['Subject'] = subject

    sendmail_location = "/usr/sbin/sendmail"
    subprocess.run([sendmail_location, "-t", "-oi"], input=msg.as_bytes())


#Get repo list from each AWS account
def repo_list(account):
 ecr=connect(region)
 response = ecr.describe_repositories(registryId=account)
 for i in range(0,len(response['repositories'])):
   repo=response['repositories'][i]['repositoryName']
   if repo.startswith(('rcx', 'rle')):
    repo_name.append(repo)


#Get image count for each repo
def image_count(account,repo_name):
 ecr=connect(region)
 for name in repo_name:
     paginator = ecr.get_paginator('list_images')
     try:
       response_list = paginator.paginate(
                        registryId=account,
                        repositoryName=name,
                        filter={
                           'tagStatus': 'ANY'
                           }
                          )
       count=0
       for image in response_list:
        count+=len(image['imageIds'])
       if count > 8000:
        mail_body="Images on account {} for repo {} has reached threshold - {},Please take action".format(account,name,count)
        subject = 'Alert:: ECR Image Threhold Breach :: {} :: {}'.format(account,name)
        sendEmail(sender, recevier, subject, mail_body)
     except:
         pass


if __name__ == "__main__":
 registries=aws_registry()
 region=[registries[i]['aws-region'] for i, x in enumerate(registries) if registries[i]['aws-account'] == 'xxxxxxxxx234' and registries[i]['aws-region'] == 'ap-southeast-1'][0]
 repo_list(account=[registries[i]['aws-account'] for i, x in enumerate(registries) if registries[i]['aws-account'] == 'xxxxxx234' and registries[i]['aws-region'] == 'ap-southeast-1'][0])
 for i,j in enumerate(registries):
  region=registries[i]['aws-region']
  account=registries[i]['aws-account']
  image_count(account,repo_name)

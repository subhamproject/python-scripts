#!/usr/bin/python

''' This scipt will be used to Manage jenkins via command line '''

import jenkins
import argparse

parser = argparse.ArgumentParser(description='Manage jenkins via command line')
parser.add_argument('-f','--folder',type=str,help='Please provide folder name where job resides.',dest='folder')
parser.add_argument('-j','--job',type=str,help='Please provide jenkins job name.',dest='job')
parser.add_argument('-b','--branch',type=str,help='Please provide branch name for the job to run.',dest='branch')
parser.add_argument('-v','--version',help='To get jenkins version from server.',action='store_true')
parser.add_argument('-r','--run',help='To run jenkins job.',action='store_true')
parser.add_argument('-s','--stop',help='To stop jenkins job.',action='store_true')
parser.add_argument('-e','--enable',help='To enable jenkins job.',action='store_true')
parser.add_argument('-d','--disable',help='To disable jenkins job.',action='store_true')
parser.add_argument('--shutdown',help='To publish jenkins going down.',action='store_true')
parser.add_argument('-n','--nodes',help='To get number of nodes and it status.',action='store_true')
parser.add_argument('-l','--logs',help='To get build logs.',action='store_true')


args = parser.parse_args()
folder = args.folder
job = args.job
branch = args.branch

server = jenkins.Jenkins('http://3.0.104.94:8080/', username='admin',
                        password='112ddxxxxxxxd98fcf68e9448be8379')

#server = jenkins.Jenkins('http://10.10.100.101:8080/', username='admin',
                        #password='116794xxxxxxxx59f63af7ded45743550')
#Defining functions

def build_job(job_name):
   if server.job_exists(job_name):
      server.build_job(job_name)
   else:
      print('Job {} does not exist in jenkins'.format(job_name))

def stop_build(job_name):
    if server.job_exists(job_name):
      info = server.get_job_info(job_name)
      builds = info['builds']
      for number in builds:
        server.stop_build(job_name,number['number'])
        print('Jenkins job {} with job id {} has been stopped'.format(job_name,number['number']))
        break
    else:
       print('Job {} does not exist in jenkins'.format(job_name))

def jenkins_version():
    user = server.get_whoami()
    version = server.get_version()
    print('Hello %s from Jenkins %s' % (user['fullName'], version))

def jenkins_going_down():
    server.quiet_down()
    print('Jenkins is going to shutdown!')

def get_node_details():
    for node in server.get_nodes():
      print('Node_Name: {} ==>  Is_offline: {}'.format(node['name'], node['offline']))

def enable_job(job_name):
   if server.job_exists(job_name):
      server.enable_job(job_name)
      print('Jenkins job {} is successfully enabled.'.format(job_name))
   else:
      print('Job {} does not exist in jenkins'.format(job_name))


def disable_job(job_name):
   if server.job_exists(job_name):
      server.disable_job(job_name)
      print('Jenkins job {} is successfully disabled.'.format(job_name))
   else:
      print('Job {} does not exist in jenkins'.format(job_name))


def build_logs(job_name):
    if server.job_exists(job_name):
      info = server.get_job_info(job_name)
      builds = info['builds']
      for number in builds:
        print(server.get_build_console_output(job_name,number['number']))
        break
    else:
        print('Job {} does not exist in jenkins'.format(job_name))

def multi_args(*args):
     argCount = len(args)
     if argCount == 1:
        for i in args:
          return i
     else:
        lists = [ item for item in args ]
        return ("/".join(lists))

# Execution part
if not args.enable and not args.disable and not args.logs:
   if args.run and folder and job and branch:
      build_job(multi_args(folder,job,branch))
   elif args.run and folder and job:
      build_job(multi_args(folder,job))
   elif args.run and job:
      build_job(multi_args(job))

if args.version:
   jenkins_version()

if args.enable:
   if folder and job:
     enable_job(multi_args(folder,job))
   elif job:
     enable_job(multi_args(job))

if args.logs:
  if folder and job:
      build_logs(multi_args(folder,job,branch))
  elif job:
      build_logs(multi_args(job))

if args.disable:
   if folder and job:
     disable_job(multi_args(folder,job))
   elif job:
     disable_job(multi_args(job))

if args.shutdown:
   jenkins_going_down()

if args.nodes:
   get_node_details()

if not args.enable and not args.disable and not args.logs:
  if args.stop and folder and job and branch:
     stop_build(multi_args(folder,job,branch))
  elif args.stop and folder and job:
     stop_build(multi_args(folder,job))
  elif args.stop and job:
     stop_build(multi_args(job))

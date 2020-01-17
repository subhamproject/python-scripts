#!/usr/bin/python

''' This scipt will be used to Manage jenkins via command line '''

import jenkins
import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Manage jenkins via command line')
parser.add_argument('--directory',type=str,help='Please provide directory name where job resides.',dest='directory')
parser.add_argument('--job',type=str,help='Please provide jenkins job name to run.',dest='job')
parser.add_argument('--branch',type=str,help='Please provide branch name for the job to run.',dest='branch')
parser.add_argument('--version',help='To get jenkins version from server.',action='store_true')
parser.add_argument('--run',help='To run jenkins job.',action='store_true')
parser.add_argument('--stop',help='To stop jenkins job.',action='store_true')
parser.add_argument('--enable',help='To enable jenkins job.',action='store_true')
parser.add_argument('--disable',help='To disable jenkins job.',action='store_true')
parser.add_argument('--shutdown',help='To publish jenkins going down.',action='store_true')
parser.add_argument('--nodes',help='To get number of nodes and it status.',action='store_true')
parser.add_argument('--plugins',help='To install plugins.',dest='plugin')
parser.add_argument('--number',help='Jenkins build number for the job to be stopped.',dest='number')


args = parser.parse_args()
directory = args.directory
job = args.job
branch = args.branch
plugin = args.plugin
number = args.number

server = jenkins.Jenkins('http://3.1.100.2413:8080/', username='admin',
                        password='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

#Defining functions

def build_job(job_name):
   if server.job_exists(job_name):
      server.build_job(job_name)
   else:
      print('Job {} does not exist in jenkins'.format(job_name))

def stop_build(job_name,build_num):
    if server.job_exists(job_name):
       server.stop_build(job_name,build_num)
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
      print('Node_Name: {} --> Is_offline: {}'.format(node['name'] ,node['offline']))

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


def install_plugins(plugin):
    server.install_plugin(plugin, include_dependencies=True)


def multi_args(*args):
     argCount = len(args)
     if argCount == 1:
        for i in args:
          return i
     else:
        lists = [ item for item in args ]
        return ("/".join(lists))

# Execution part
if not args.enable and not args.disable and not number:
   if args.run and directory and job and branch:
      build_job(multi_args(directory,job,branch))
   elif args.run and job:
      build_job(multi_args(job))
   elif not args.version and not args.shutdown and not args.nodes:
      print('Please provide all the arguments and re-run!')
      parser.print_help()
      raise SystemExit

if args.version:
   jenkins_version()

if args.enable:
   if directory and job:
     enable_job(multi_args(directory,job))
   elif job:
     enable_job(multi_args(job))

if args.disable:
   if directory and job:
     disable_job(multi_args(directory,job))
   elif job:
     disable_job(multi_args(job))

if args.shutdown:
   jenkins_going_down()

if args.nodes:
   get_node_details()

if plugin:
   install_plugins(plugin)

if not args.enable and not args.disable and number:
  if args.stop and directory and job and branch:
     stop_build(multi_args(directory,job,branch),int(number))
  elif args.stop and job:
     stop_build(multi_args(job),int(number))
  elif not args.version and not args.shutdown and not args.nodes:
      print('Please provide all the arguments and re-run!')
      parser.print_help()
      raise SystemExit

#!/usr/bin/python

import subprocess
import os
import argparse

add_user = argparse.ArgumentParser(description='Add/Delete Users From Server')
add_user.add_argument('-a','--add',metavar='UserName',nargs='+',required=False,help='Add user to server',dest='username')
add_user.add_argument('-d','--del',metavar='UserName',nargs='+',required=False,help='Add user to server',dest='deluser')
args = add_user.parse_args()
user = args.username
del_user = args.deluser

if user:
   try:
     from subprocess import DEVNULL
   except ImportError:
     DEVNULL = open(os.devnull, 'wb')
   for user_name in user:
     status = subprocess.run(['grep','^'+user_name+'$','/etc/passwd'],stdout=DEVNULL, stderr=DEVNULL)
     if status.returncode == 0:
        print('User \"{}\" already present'.format(user_name))
     else:
        print('Adding user \"{}\"'.format(user_name))
        status_code = subprocess.run(['useradd','-m','-d','/home/'+user_name,'-s','/bin/bash',user_name])
        if status_code.returncode == 0:
           print('User \"{}\" was successfully added'.format(user_name))
if del_user:
   try:
     from subprocess import DEVNULL
   except ImportError:
     DEVNULL = open(os.devnull, 'wb')
   for d_user in del_user:
     status = subprocess.run(['grep','^'+d_user,'/etc/passwd'],stdout=DEVNULL, stderr=DEVNULL)
     if status.returncode != 0:
        print('User \"{}\" not present'.format(d_user))
     else:
        print('Deleting user \"{}\"'.format(d_user))
        status_code = subprocess.run(['userdel','-r',d_user])
        if status_code.returncode == 0:
           print('User \"{}\" was successfully added'.format(d_user))

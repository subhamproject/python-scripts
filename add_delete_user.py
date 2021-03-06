#!/usr/bin/python

import subprocess
import os
import argparse
import pwd
import sys
import getpass
import re

add_users = argparse.ArgumentParser(description='Add/Delete Users From Server')
add_users.add_argument('-a','--add',metavar='UserName',nargs='+',required=False,help='Add user to server',dest='username')
add_users.add_argument('-d','--del',metavar='UserName',nargs='+',required=False,help='Add user to server',dest='deluser')
args = add_users.parse_args()
user = args.username
del_user = args.deluser

def root_check():
    ''' Exit if login name not root.'''

    if not getpass.getuser() == 'root':
        raise SystemExit('ERROR: THIS PROGRAM REQUIRES ROOT PRIVILEGES. EXITING.')

def add_user(usersname):
    for user_name in usersname:
         try:
            pwd.getpwnam(user_name)
            print('User \"{}\" already present'.format(user_name))
         except KeyError:
            print('Adding user \"{}\"'.format(user_name))
            status_code = subprocess.run(['useradd','-m','-d','/home/'+user_name,'-s','/bin/bash',user_name])
            if status_code.returncode == 0:
               print('User \"{}\" was successfully added'.format(user_name))

def delete_user(usersname):
    for d_user in usersname:
        try:
           pwd.getpwnam(d_user)
           print('Deleting user \"{}\"'.format(d_user))
           status_code = subprocess.run(['userdel','-r',d_user])
           if status_code.returncode == 0:
              print('User \"{}\" was successfully deleted'.format(d_user))
        except KeyError:
           print('User \"{}\" not present'.format(d_user))

if __name__ == '__main__':
    root_check()
    if not user:
       add_users.print_help()
       raise SystemExit()
    else:
       add_user(user)
    if not del_user:
       add_users.print_help()
       raise SystemExit()
    else:
       delete_user(del_user)
############################################################################################################################
## First way
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
           print('User \"{}\" was successfully deleted'.format(d_user))
         
=================================================================================================================================         
## Second Way

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

def add_user(usersname):
    if usersname:
       try:
         from subprocess import DEVNULL
       except ImportError:
         DEVNULL = open(os.devnull, 'wb')
       for user_name in usersname:
           #status = subprocess.run(['grep','-E','^'+user_name+'$'+'|',user_name,'/etc/passwd'],stdout=DEVNULL, stderr=DEVNULL)
           status = subprocess.run(['compgen','-u','|','grep','^'+user_name+'$'],stdout=DEVNULL, stderr=DEVNULL)
           if status.returncode == 0:
              print('User \"{}\" already present'.format(user_name))
           else:
              print('Adding user \"{}\"'.format(user_name))
              status_code = subprocess.run(['useradd','-m','-d','/home/'+user_name,'-s','/bin/bash',user_name])
              if status_code.returncode == 0:
                 print('User \"{}\" was successfully added'.format(user_name))
    else:
       print('User name is null')

def delete_user(usersname):
    try:
      from subprocess import DEVNULL
    except ImportError:
      DEVNULL = open(os.devnull, 'wb')
    for d_user in usersname:
      status = subprocess.run(['grep','^'+d_user+'$','/etc/passwd'],stdout=DEVNULL, stderr=DEVNULL)
      if status.returncode != 0:
         print('User \"{}\" not present'.format(d_user))
      else:
         print('Deleting user \"{}\"'.format(d_user))
         status_code = subprocess.run(['userdel','-r',d_user])
         if status_code.returncode == 0:
            print('User \"{}\" was successfully deleted'.format(d_user))

if __name__ == '__main__':
    if user:
       add_user(user)
    elif del_user:
       delete_user(del_user)

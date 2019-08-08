#!/usr/bin/python

import subprocess
user_name = input('Please enter the name of the user: ')
print('Adding user {}'.format(user_name))
subprocess.run(['useradd','-m','-d','/home/'+user_name,'-s','/bin/bash',user_name])
root@rcxdev:~#

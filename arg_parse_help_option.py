#!/usr/bin/python

import subprocess
import os
import argparse
import pwd
import sys
import getpass
import re

add_user = argparse.ArgumentParser(description='Add/Delete Users From Server')
add_user.add_argument('-a','--add',metavar='UserName',nargs='+',required=False,help='Add user to server',dest='username')
add_user.add_argument('-d','--del',metavar='UserName',nargs='+',required=False,help='Add user to server',dest='deluser')
args = add_user.parse_args()

if not args.username:
   print('Please enter username')
   add_user.print_help() -->  // print the help message only if no arguments are supplied on the command line //
   raise SystemExit()
else:
   str(input('Please enter your name; '))

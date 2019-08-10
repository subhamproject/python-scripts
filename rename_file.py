#!/usr/bin/python

import os

os.chdir('/tmp')
#print(os.getcwd())
for f in os.listdir():
   if not os.path.isdir(f):
     file_name, file_ext = os.path.splitext(f)
     file_ext = '.py'
     os.rename(f , file_name + file_ext)

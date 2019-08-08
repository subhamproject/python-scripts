#!/usr/bin/python
## This script will help to rename file ext from 'py' to 'txt' and vice versa

import os

dir_name = input('Please enter the directory name where files resides: ')
file_ext = input('Please enter the file ext you wish to change to: ')

os.chdir(dir_name)
for f in os.listdir():
   if not os.path.isdir(f):
      f_name, f_ext = os.path.splitext(f)
      if f_ext == '.py' or '.txt':
        print('Changing the file \"{}\" ext from \"{}\" to \"{}\"'.format(f_name, f_ext, file_ext))
        f_ext = file_ext
        os.rename(f, f_name + f_ext)

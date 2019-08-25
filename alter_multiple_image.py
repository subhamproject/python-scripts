#!/usr/bin/python3

''' This scipt will be used to Alter image for multi service at once '''

import os
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Alter Image for multiple services')
parser.add_argument(
     '-v',
     '--version',
     nargs='?',
     metavar='VERSION',
     required=False,
     type=str,
     help='Please provide image version:',
     dest='ver'
)
parser.add_argument(
     '-f',
     '--file',
     nargs='?',
     metavar='FILE',
     required=False,
     type=str,
     help='Please provide source image file name:',
     dest='files'
)
args = parser.parse_args()
version = args.ver
filename = args.files

def alter_image(update_version,file_name):
 if os.path.exists(file_name):
  with open(file_name) as file:
    for f in file:
      image,serv = f.split(':')
      first,second,third = serv.split('.')
      current_version = serv[-7:]
      f = f.replace(current_version,update_version)
      service_name = first[:-2][7:].strip()
      image_name = f.strip()
      print('Service Name:',service_name)
      print('Image Name:',image_name)
      n1,n2,n3 = file_name.split('_')
      if n1 == 'core':
         pass
        subprocess.run(['subham','service','alter','--image',image_name,service_name])
      elif n1 == 'backend':
         pass
        subprocess.run(['subham','jobs','alter','--image',image_name,service_name])
 else:
    print('file \"{}\" does not exist in this path \"{}\"'.format(filename,os.getcwd()))

if __name__ == '__main__':
  if not version or not filename:
     print('Version or Filename cannot be null,Please provide both the input and try again...')
     parser.print_help()
     raise SystemExit
  else:
     alter_image(version,filename)

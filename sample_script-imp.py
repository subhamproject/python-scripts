#!/usr/bin/python

import os
import subprocess
import click

version = str(input('Please enter the latest image version: '))

with open('log') as file:
    for f in file:
      image,serv = f.split(':')
      first,second,third = serv.split('.')
      current = serv[-7:]
      f = f.replace(current,version)
      service_name = first[:-2][7:].strip()
      if service_name == 'event':
         service_name = 'mep0'
      elif service_name == 'publisher':
         service_name = 'aep0'
      else:
         service_name = service_name
      image_name = f.strip()
      print('Service Name:',service_name)
      print('Image Name:',image_name)

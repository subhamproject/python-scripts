#!/usr/bin/python

import os
#print(os.environ.get('RCX_BACKEND'))
file_path = os.path.join(os.environ.get('HOME'),'nifi_compose.yml')
print(file_path)

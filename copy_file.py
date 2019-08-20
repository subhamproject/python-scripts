#!/usr/bin/python
import os, shutil

directorya = "exampledir"
directoryb = "exampledir2"
files = [file for file in os.listdir(directorya) if os.path.isfile(os.path.join(directorya, file))]
for file in files:
    if not os.path.exists(os.path.join(directoryb, file)):
        shutil.copy(os.path.join(directorya, file), directoryb)


#!/usr/bin/python

import glob
import os
import shutil
dira = 'path-to-dira'
dirb = 'path-to-dirb'

for filename in glob.glob(os.path.join(dira,'*.txt')):
   print os.path.join(dirb,os.path.basename(filename))
   if not os.path.isfile(os.path.join(dirb,os.path.basename(filename))):
       shutil.copy(filename,dirb)


#!/usr/bin/python

import glob
import shutil

src = "/opt/"
dst = "/opt/something/"

files_src = set(glob.glob(src+"*.txt"))
files_dst = set(glob.glob(dst+"*.txt"))

other_files = files_src-files_dst
for _file in other_files:
    shutil.copy(src+_file, dst)


#!/usr/bin/python

import shutil
from os import listdir
from os.path import isfile, join

DIR_A = "<Complete path to A directory>"
DIR_B = "<Complete path to B directory>"

onlyfiles_A = [ f for f in listdir(DIR_A) if isfile(join(DIR_A,f)) ]
onlyfiles_B = [ f for f in listdir(DIR_B) if isfile(join(DIR_B,f)) ]

for f_a in onlyfiles_A:
    if not f_a in onlyfiles_B:
        src = DIR_A+"/"+f_a
        shutil.copy(src, DIR_B)



#!/usr/bin/python

import glob
import os
import shutil
dira = 'path-to-dira'
dirb = 'path-to-dirb'

for filename in glob.glob(os.path.join(dira,'*.txt')):
   print os.path.join(dirb,os.path.basename(filename))
   if not os.path.isfile(os.path.join(dirb,os.path.basename(filename))):
       shutil.copy(filename,dirb)

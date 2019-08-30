https://pythonprogramming.altervista.org/how-to-get-all-the-file-in-a-directory/?doing_wp_cron=1567164553.1879150867462158203125

import os
 
def searchfiles(extension='.ttf'):
    "Create a txt file with all the file of a type"
    with open("file.txt", "w", encoding="utf-8") as filewrite:
        for r, d, f in os.walk("C:\\"):
            for file in f:
                if file.endswith(extension):
                    filewrite.write(f"{r + file}\n")
 
# looking for ttf file (fonts)
searchfiles('ttf')


========================================

import glob
import os
filelist=glob.glob("/home/ismail/*.txt")
for file in filelist:
  os.remove(file)
  
  
  ====================================================
import os

dir_name = "/Users/ben/downloads/"
test = os.listdir(dir_name)

for item in test:
    if item.endswith(".zip"):
        os.remove(os.path.join(dir_name, item))
=================================================================
        
 import os
from fnmatch import fnmatch

for dirpath, dirnames, filenames in os.walk(os.curdir):
    for file in filenames:
        if fnmatch(file, '*.pdf'):
            os.remove(os.path.join(dirpath, file))
            
            
 ================================================================
 
 import glob
import os
filelist=glob.glob("/home/test/*.txt")
for file in filelist[:-2]:
  os.remove(file)

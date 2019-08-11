### Get the file with py extenstion

#!/usr/bin/python
import os

files = os.listdir('/root/')
print(files)
py_files = []
for file in files:
    if file.endswith('.py'):
        py_files.append(file)
print(py_files)



############################################################################################################

#!/usr/bin/python
import os
import glob
print(glob.glob('*.py'))

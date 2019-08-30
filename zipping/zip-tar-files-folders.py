import os
import tarfile
def tardir(path, tar_name):
    with tarfile.open(tar_name, "w:gz") as tar_handle:
        for root, dirs, files in os.walk(path):
            for file in files:
                tar_handle.add(os.path.join(root, file))
tardir('./my_folder', 'sample.tar.gz')
tar.close()
The above code will compress the contents of my_folder in a file 'sample.tar.gz'. and store it in the current directory.



import tarfile
import os

path = raw_input('Please enter your path: ')
backup = 'subham'+'.tar.gz'
if os.path.exists(backup):
   os.remove(backup)
   with tarfile.open(backup, mode='w:gz') as archive:
    print('Deleting file '+backup+' if exitst from: ' + os.getcwd())
    if os.path.exists(backup) or not os.path.exists(backup):
      print('taking backup of this path: ' + path)
      archive.add(path,recursive=True)

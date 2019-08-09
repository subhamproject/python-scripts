
#!/usr/bin/python

import subprocess
import os

with open(os.devnull, 'w') as DEVNULL:
  user = input('Please enter the name of the user to add: ')
  for user_name in user.split(','):
      status = subprocess.run(['grep',user_name,'/etc/passwd'],stdout=DEVNULL, stderr=DEVNULL)
      if status.returncode == 0:
         print('User \"{}\" already present'.format(user_name))
      else:
         print('Adding user \"{}\"'.format(user_name))
         status_code = subprocess.run(['useradd','-m','-d','/home/'+user_name,'-s','/bin/bash',user_name])
         if status_code.returncode == 0:
            print('User \"{}\" was successfully added'.format(user_name))


#!/usr/bin/python3

import subprocess, re
user = input('Please enter the name of the user to add: ')
for user_name in user.split(','):
   if re.match(r'user_name',open('/etc/passwd').read()):
      print('User \"{}\" already present'.format(user_name))
   else:
      print('Adding user \"{}\"'.format(user_name))
      status = subprocess.run(['useradd','-m','-d','/home/'+user_name,'-s','/bin/bash',user_name])
      if status.returncode == 0:
         print('User \"{}\" was successfully added'.format(user_name))

#!/usr/bin/python

import subprocess
user_name = input('Please enter the name of the user: ')
print('Adding user {}'.format(user_name))
subprocess.run(['useradd','-m','-d','/home/'+user_name,'-s','/bin/bash',user_name])
root@rcxdev:~#

  #!/usr/bin/python

import subprocess
user_name = input('Please enter the name of the user: ')
if user_name in open('/etc/passwd').read():
     print('User {} already present'.format(user_name))
else:
     print('Adding user {}'.format(user_name))
     subprocess.run(['useradd','-m','-d','/home/'+user_name,'-s','/bin/bash',user_name])
      
 #!/usr/bin/python

import subprocess
user_name = input('Please enter the name of the user to add: ')
if user_name in open('/etc/passwd').read():
     print('User \"{}\" already present'.format(user_name))
else:
     print('Adding user \"{}\"'.format(user_name))
     status = subprocess.run(['useradd','-m','-d','/home/'+user_name,'-s','/bin/bash',user_name])
     if status.returncode == 0:
        print('User \"{}\" was successfully added'.format(user_name)

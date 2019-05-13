This script creates a user and adds them to the Wheel group

#!/usr/bin/env python
#sudo user creation
import sys
import subprocess
#import colored
while True:
        print "********Warning : Sudo users have special privileges. Be careful!!!!!!!********* "
        print "Sudo users list:"
        subprocess.call(["grep","wheel","/etc/group"])
        if len(sys.argv) > 1:
                name = sys.argv[1]
        else:
                name = raw_input('Enter User Name:')
        if name == 'root':
                print("Can't do anything with the 'root' user account......Breaking the program")
                sys.exit()
        opt = int(raw_input("Select option: 1. Create 2.Delete :"))
        if opt == 1:
                subprocess.call(["useradd", name])
                subprocess.call(["usermod", "-aG","wheel", name])
                subprocess.call(["passwd", name])
                print('\x1b[6;30;42m' + 'Sudo user creation is a Success!' + '\x1b[0m')
        elif opt == 2:
                subprocess.call(["userdel","-r", name])
                print('\x1b[6;30;42m' + 'Sudo user deletion is a Success!' + '\x1b[0m')
        else:
                print "Invalid option"
        op = raw_input("Do you want to continue (yes/no):")
        if op == 'no':
                sys.exit()

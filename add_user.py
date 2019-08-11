
#!/usr/bin/env python

from __future__ import print_function
from builtins import *

import os 
import sys
import re 
import pwd
import getpass

# Error message for invlaid user input. 
TRY_AGAIN="Sorry, that's not allowed. Check input and try again." 

def root_user_check():
    """Exit if current UID not 0."""

    if not os.getuid() == 0:
        print("This program requires ROOT privileges. Exiting.")
        sys.exit()

def username_prompt(): 
    """Prompt user. Check that input matches, and contains at least one 
    allowable character.""" 

    print("Valid usernames contain only the characters 'a-z', e.g. pdiddy.")

    while True: 
        username = str(input("Enter username to add: "))
        confirm_name = str(input("To confirm, re-enter username: "))
        
        if username != confirm_name or not re.match("^[a-z]+$", username):
            print(TRY_AGAIN)
            continue 
        
        else:
            print("OK, checking if user: %s exists..." %(username))
            return username 

def username_check(username): 
    """Check if username exists."""

    try: 
        pwd.getpwnam(username)
        print("User %s DOES EXIST. Try a different username." % (username)) 
        return False

    except KeyError: 
        print("User %s DOES NOT exist. Continuing..." % (username))    
        return True

def comment_prompt(): 
    """Prompt for input. Check that input matches and contains allowable 
    characters. No input is allowable.""" 

    print("Valid comments contain only the characters 'a-z' and ','," 
          "e.g. daddy,puff. This field may be left blank.")
 
    while True: 
        comment = str(input("Enter user comments, or press 'return' twice " \
                            "to leave blank: "))
        confirm_comment = str(input("To confirm, re-enter comments: "))
        
        if comment != confirm_comment or not re.match("^[a-z,]*$", comment):
            print(TRY_AGAIN)
            continue 
        
        else:
            print("Comments match. Continuing...") 
            return comment

def passwd_prompt(): 
    """Prompt user for input. Check that input matches and meets password 
    complexity requirements."""

    print("Passwords MUST contain AT LEAST: one lower-case letter," 
          "one number, one symbol, and be a MINIMUM of 8 characters in length,"
          "e.g. r!ght2oE")

    while True:

        passy = getpass.getpass(prompt="Enter password for user: ")
        confirm_passy = getpass.getpass(prompt="To confirm, " \
                                               "re-enter password: ")

        # check for the following conditions: 
        # user input matches
        # length of input is at least 8 characters
        # input contains at least 1 number  
        # input contains at least 1 letter      
        # input contains at least 1 symbol 
  
        if passy != confirm_passy \
        or len(passy) <8 \
        or not re.search('\d', passy) \
        or not re.search(r"[a-z]",passy) \
        or not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', passy):  
        
            print(TRY_AGAIN)
            continue 
        
        else:
            print("Password meets complexity requirement. Continuing...") 
            return passy 

def add_user(username, comment, password ): 
    """Call the useradd command to create an account with given parameters."""

    print("Adding user: %s" % (username)) 
   
    # create user  
    # create group with same name as user, adding user to group
    # comment (lastname, firstname) 
    # create home directory           
    # login shell 
    # password (encrypted via openssl) 
 
    os.system("useradd --create-home \
    --user-group \
    --comment "+comment+" \
    --home /home/"+username+" \
    --shell /bin/bash \
    --password $(printf %s "+password+" |openssl passwd -1 -stdin) "+username+"")
 
    print("Done.")   

def add_me(): 
    """Add user to Linux-based OSs."""

    root_user_check()

    username = username_prompt()
    while not username_check(username): 
        username = username_prompt()

    comment = comment_prompt()
    password = passwd_prompt()

    add_user(username, comment, password)

if __name__ == '__main__':
    print('Python script to create user accounts in Linux.')

    while True:
        """Loop to run program, then prompt user to run again."""
        add_me()

        while True:
            reply = str(input("Run script again? (Yes/No): ")).lower().strip()
            if reply in ('yes', 'no'):
                break
            print(TRY_AGAIN) 

        if reply == 'yes':
            continue
        else:
            print("Ciao!")
            break
            
            
#################################################################################################################################


"""
Author: Ahad Sheriff
Description:
    Python script to add users to Linux groups. You can easily change the content
    of this script to fit your needs. 
    Sample CSV file that I used to test is 
    included as `sampleAccounts.csv`
Data:
    The data in the csv file must be of the form:
    "Full Name", "Office Number", "Phone Extension #", "Department Name"
 
"""

import os
import csv

def readFile(file):

    with open(file, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]

        for i in data:

            fullName = i[0]
            splitName = [x.strip() for x in fullName.split(',')]
            firstAndMiddle = [c.strip() for c in splitName[1].split(' ')]
            first = firstAndMiddle[0].lower()
            last = splitName[0].lower()

            """
                Capitalize only the first letter of the names
            """
            newFirst = first[0]
            newFirst = newFirst.upper()
            firstName = newFirst + first[1:]

            newLast = last[0]
            newLast = newLast.upper()
            lastName = newLast + last[1:]

            if ((len(firstAndMiddle)) > 1):
                middle = firstAndMiddle[1].lower()
                newMiddle = middle[0]
                newMiddle = newMiddle.upper()
                middleName = newMiddle + middle[1:]
            else:
                middleName = ""

            officeNumber = i[1]
            extension = i[2]
            department = i[3]

            """
                generate unique user id's for each user
                the script will give each member a user id that consists of:
                    The first letter of their first name
                    Their last name
                    Their office extension number
                This uid prevents problems occuring with multiple users of the same name
            """
            uid = firstName[0].lower() + lastName.lower() + extension

            """
                All users should use the default shell
                    /bin/bash
                except Engineering folks who's default path is
                    /bin/csh
            """
            if department == "Engineering":
                shell = "/bin/csh"
            else:
                shell = "/bin/bash"

            print("Adding user: \n" + firstName + " " + middleName + " " + lastName + " | " + officeNumber
                  + " | " + extension + " | " + department + " | " + uid + " | " + shell + "\n")

            os.system("useradd " + uid + " -c " + "'" + firstName + " " + middleName + " " + lastName + "'" + " -g "
                      + department + " -d /home/" + department + "/" + uid + " -s " + shell)


def main():
    file = input("Enter a filename: ")
    readFile(file)

main()

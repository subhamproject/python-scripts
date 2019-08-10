#!/usr/bin/env python

from __future__ import print_function
from builtins import *

import sys
import getpass
import re
import pwd 
import os 

def root_check():
    """Exit if login name not root."""

    if not getpass.getuser() == 'root':
        print("ERROR: THIS PROGRAM REQUIRES ROOT PRIVILEGES. EXITING.")
        sys.exit()

def username_prompt(): 
    """Prompt user. Check that input matches, and cotains at least one allowable character.""" 

    print("Valid usernames contain only the characters 'a-z', e.g. trex") 

    while True: 
        username = str(input("Enter username to add: "))
        confirm_name = str(input("To confirm, re-enter username: "))

        if username != confirm_name or not re.match("^[a-z]+$", username):
            print("SORRY, THAT'S NOT ALLOWED. TRY AGAIN.")
            continue 

        else: 
            print("OK, checking if user: %s exists." %(username))
            return username 

def username_check(): 
    """Check if username exists."""

    while True: 
        check = username_prompt()

        try: 
            pwd.getpwnam(check)
            print("USER %s EXISTS. TRY A DIFFERENT USERNAME." % (check)) 

        except KeyError: 
            print("User %s does not exist. Continuing..." % (check))     
            return check 

def comment_prompt(): 
    """Prompt for input. Check that input matches and contains allowable characters. No input is allowable.""" 

    print("Valid comments contain only the characters 'a-z' and ',', e.g. rex,tyrannosaurus. This field can be left blank.")
 
    while True: 
        comment = str(input("Enter user comments, or press 'return' twice to leave blank: "))
        confirm_comment = str(input("To confirm, re-enter comments: "))
        
        if comment != confirm_comment or not re.match("^[a-z,]*$", comment):
            print("SORRY, THAT'S NOT ALLOWED. TRY AGAIN.")
            continue 
        
        else:
            print("Comments match. Continuing...") 
            return comment 

def passwd_prompt(): 
    """Prompt user for input. Check that input matches and meets password complexity requirements."""

    print("Password MUST contain AT LEAST: one lower-case letter, one number, one symbol, and be a MINIMUM of 8 characters in length, e.g. 4.lizard")

    while True:

        passy = getpass.getpass(prompt="Enter password for user: ")
        confirm_passy = getpass.getpass(prompt="To confirm, re-enter password: ")

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
        
            print("SORRY, THAT'S NOT ALLOWED. TRY AGAIN.")
            continue 
        
        else:
            print("Password meets complexity requirement. Continuing...") 
            return passy 

def add_usr(): 
    """Call the useradd command to create an account with given parameters."""
   
    name = username_check()
    note = comment_prompt()
    code = passwd_prompt()

    print("Adding user: %s" % (name)) 
   
    # create user  
    # create group with same name as user, adding user to group
    # comment (lastname, firstname) 
    # create home directory           
    # login shell 
    # password (encrypted via openssl) 
 
    os.system("useradd --create-home \
    --user-group \
    --comment "+note+" \
    --home /home/"+name+" \
    --shell /bin/bash \
    --password $(printf %s "+code+" |openssl passwd -1 -stdin) "+name+"")
 
    print("Done.")     

def addME(): 
    """Add user to Linux OS."""
    
    root_check()
    add_usr() 

if __name__ == '__main__': 
    addME()

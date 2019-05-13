#!/usr/bin/python3
import argparse, sys, os, crypt
from datetime import date, timedelta

##Create User function
def createuser(user,edays):
    user = user.lower()
    now = date.today()
    end = now + timedelta(days=edays)
    expire = end.isoformat()
    password = "Password1"
    encPassword = crypt.crypt(password,"a1")
    print("Creating user: "+ user)
    os.system("useradd -m -p " +encPassword+ " -e " +expire+" "+ user)
    for line in open("/etc/passwd"):
        if line.startswith(user + ":"):
            print(line)

##Remove users
def deluser(user):
    print ("Deleting user: " + user)
    os.system("userdel -r " + user)

##Open File function used both the add and remove users from file
def openfile(file):
    f = open(file)
    for userline in f.readlines():
        if userline == "n": #Ignore empty lines
            continue
        userline = userline.rstrip() #remove trailing newline from readlines
        if args.addfromfile:
            createuser(userline,expiredays)
        elif args.deletefromfile:
            deluser(userline)

if not os.geteuid()==0:
    sys.exit("nOnly root can create users, try sudo " +sys.argv[0]+ " n")

parser = argparse.ArgumentParser()
parser.add_argument("-e","--expire",type=int,help="Days to expire account, default 5 days")
parser.add_argument("-a","--add", nargs="+", help="Creates local Linux Accounts")
parser.add_argument("-d","--delete",nargs="+", help="Removes local Linux Accounts")
parser.add_argument("-f","--addfromfile",help="Create Local Linux Accounts from file")
parser.add_argument("-r","--deletefromfile",help="Delete Local Linux Accounts from file")
args = parser.parse_args()

if args.expire:
    expiredays = args.expire
else:
    expiredays = 5

if args.add:
    for u in args.add:
        createuser(u, expiredays)
elif args.delete:
    for u in args.delete:
        deluser(u)

elif args.addfromfile:
    openfile(args.addfromfile)
elif args.deletefromfile:
    openfile(args.deletefromfile)

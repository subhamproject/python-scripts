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

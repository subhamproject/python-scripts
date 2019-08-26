#!/usr/bin/python
user = "user"
with open("/etc/passwd") as file:
    for line in file:
        if line.split(":")[0] == user:
            if line.rstrip("\n").split(":")[6] in ["/usr/sbin/nologin", "/bin/false"]:
                print("User is not allowed to login")
            else:
                print(line.rstrip("\n").split(":")[6])


#!/usr/bin/python
from pwd import getpwnam

user = "user"
shell = getpwnam(user)[6]
if shell in ["/usr/sbin/nologin", "/bin/false"]:
    print("User is not allowed to login")
else:
    print(shell)

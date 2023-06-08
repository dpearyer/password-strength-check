#condition for strong password
#minimum 10 characters
#there should be two upper case letters
#at least 1 number
#at least one special characters

import re

password = " "
neg=0

while True:

    if not re.search("[a-z]", password):
        neg = -1
        break
    elif not re.search(["0-9"], password)
        neg
    elif(len(password)<=10):
        neg=-1
        break
    elif not re.search("[_@$]", password)
        neg=-1
        break
    else:
        neg=0
        print("Strong Password")
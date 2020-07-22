from userAccount import *
from actions import *

usr = input("Enter your account name: ")

if (not isAccountCreated(usr)):
    createAccount(usr)
    print('Your account has been created!')
else:
    printActions()
    print(getAction(usr, int(input("Enter the number of the action you would like to perform: "))))
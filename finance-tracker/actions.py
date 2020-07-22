from userAccount import *
names = {
        1: "Get Balance",
        2: "Deposit",
        3: "Withdraw"
    }

def printActions():
    print('What would you like to do?')
    for i,n in names.items():
        print(i,':',n)

def getAction(usr, arg):
    if arg == 1:
        return getBalance(usr)
    elif arg == 2:
        return updateBalance(usr,float(input('Enter the amount to deposit: ')))
    elif arg == 3:
        return updateBalance(usr,-float(input('Enter the amount to withdraw: ')))
    else:
        printActions()
        getAction(usr, input("Enter the number of the action you would like to perform: "))
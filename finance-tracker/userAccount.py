# create-account.py
# creates JSON file with users information

import json
import os.path

path = './accounts/'
ext = '.json'

def isAccountCreated(name):
    if os.path.isfile(path+name+ext):
        return 1
    else:
        return 0

def createAccount(name):
    if isAccountCreated(name):
        print('An account with that name already exists.')
        return 0
    data = {}
    data['bank'] = []
    data['bank'].append({
        'name': input('Enter your full name: '),
        'bank': input('Which financial institution do you use: '),
        'website':input('Enter your financial institutions website: '),
        'account-num':input('Enter your account number: '),
        'routing-num':input('Enter your routing number: '),
        'balance':(input('Enter your balance: '))
    })
    with open(path+name+ext, 'w') as outfile:
        json.dump(data,outfile,indent=4)
    return data

def getBalance(name):
    if isAccountCreated(name):
        with open(path+name+ext) as json_file:
            data = json.load(json_file)
            for d in data['bank']:
                return d['balance']

def getAccountRouteNumbers(name):
    if isAccountCreated(name):
        with open(path+name+ext) as json_file:
            data = json.load(json_file)
            for d in data['bank']:
                print('Routing Number:',d['routing-num'])
                print('Account Number:', d['account-num'])

def accountToString(name):
    if isAccountCreated(name):
        with open(path+name+ext) as json_file:
            data = json.load(json_file)
            for d in data['bank']:
                print('Name: ', d['name'])
                print('Bank: ', d['bank'])
                print('Website: ', d['website'])
                print('Account Number:', d['account-num'])
                print('Routing Number:', d['routing-num'])
                print('Balance:',d['balance'])
    else:
        return 0

def updateBalance(name, value):
    if isAccountCreated(name):
        with open(path+name+ext) as json_file:
            data = json.load(json_file)
            
        with open(path+name+ext,'w') as outfile:
            json.dump(data, outfile)
        return 'Transaction sucessful'
    else:
        return 'Transaction unsucessful'
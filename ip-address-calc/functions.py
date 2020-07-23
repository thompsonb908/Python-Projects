def convertToBinary(num, pre='', length=8, spacer=0):
    return '{0}{{:{1}>{2}}}'.format(pre, spacer, length).format(bin(num)[2:])

def binaryToString(binaryString:str):
    octects = binaryString.split('.')
    decimal = list()
    outString = ''
    dotCount = 0
    for o in octects:
        decimal.append(int('0b' + o, base = 2))
    for d in decimal:
        if dotCount < 3:
            outString = outString + str(d) + '.'
            dotCount += 1
        else:
            outString = outString + str(d)
    return outString

def stringToBinary(usrIn: str):
    octects = usrIn.split('.')
    binary = list()
    for o in octects:
        binary.append(convertToBinary(int(o)))
    return binary

def splitInput(usrIn: str):
    return usrIn.split('/')

def calcNetworkAddress(binary, mask):
    dotCount = 0
    string = ''
    for b in binary:
        string = string + b
    
    for i in range(len(string)):
        if i >= int(mask):
            string = string[:i] + '0' + string[i+1:]
    
    for i in range(32):
        if i > 0 and i % 8 == 0 and dotCount < 3:
            string = string[:i+dotCount] + '.' + string[i+dotCount:]
            dotCount += 1
    return binaryToString(string)

def calcBroadcastAddress(binary, mask):
    dotCount = 0
    string = ''
    for b in binary:
        string = string + b
    
    for i in range(len(string)):
        if i >= int(mask):
            string = string[:i] + '1' + string[i+1:]
    
    for i in range(32):
        if i > 0 and i % 8 == 0 and dotCount < 3:
            string = string[:i+dotCount] + '.' + string[i+dotCount:]
            dotCount += 1
    return binaryToString(string)

def calcSubnetMask(mask:str):
    dotCount = 0
    subnet = ''
    dotCount = 0
    for i in range(32):
        if i != 0 and i % 8 == 0 and dotCount < 3:
            subnet = subnet + '.'
        if i < int(mask):
            subnet = subnet + '1'
        else:
            subnet = subnet + '0'
    return binaryToString(subnet), ((2 ** (32 - int(mask))) -2)
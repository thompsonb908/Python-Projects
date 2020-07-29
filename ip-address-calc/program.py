from functions import splitInput, stringToBinary,calcBroadcastAddress,calcNetworkAddress,calcSubnetMask

ip, mask = splitInput(input('Enter a ip and mask with noataion a.b.c.d/e: '))

octects = stringToBinary(ip)

# print(octects)
# print(mask)

networkAddress = calcNetworkAddress(octects,mask)
print('The network address is: ', networkAddress)

broadcastAddress = calcBroadcastAddress(octects,mask)
print('The broadcast address is: ', broadcastAddress)

subnetMask, availableIP = calcSubnetMask(mask)
print('The subnet mask is: ', subnetMask)
print('Number of available host IP\'s is: ', availableIP)

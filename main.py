# 203.206.46.58

def binaryToDecimal(binaryAddress):
  decimalAddress = ""
  for index, i in enumerate(binaryAddress.split('.')):
    decimalAddress += str(int(i, 2))
    if index != 3:
      decimalAddress += '.'
  return decimalAddress

ip = input("Enter ip address: ")
mask = int(input("Enter mask: "))

splittedAddress = ip.split('.')
binaryAddress = []
binaryAddressStr = ""
for i in range(0, len(splittedAddress)):
  binaryAddress.append(str(format(int(splittedAddress[i]), '#010b'))[2:])
  binaryAddressStr += str(format(int(splittedAddress[i]), '#010b'))[2:]
  if i != 3:
    binaryAddressStr += '.'
  

binaryMask = []
binaryMaskStr = ""
binaryMaskItem = ""
for i in range(1, 33):
  if i <= mask:
    binaryMaskItem += "1"
  else: 
    binaryMaskItem += "0"
  if i % 8 == 0:
    binaryMask.append(binaryMaskItem)
    binaryMaskStr += binaryMaskItem
    binaryMaskItem = ""
    if i != 32:
      binaryMaskStr += '.'

binaryRootAddress = []
binaryRootAddressStr = ""
binaryRootAddressItem = ""
for i in range(0, 4):
  for j in range(0, 8):
    # print(binaryAddress[i][j], binaryMask[i][j])
    if binaryAddress[i][j] == binaryMask[i][j] and binaryAddress[i][j] == '1':
      binaryRootAddressItem += '1'
    else:
      binaryRootAddressItem += '0'
  binaryRootAddress.append(binaryRootAddressItem)
  binaryRootAddressStr += binaryRootAddressItem
  binaryRootAddressItem = ""
  if i != 3:
    binaryRootAddressStr += '.'

binaryFirstAddress = ""
for i in range(0, 4):
  for j in range(0, 8):
    maskCounter = 8 * i + j + 1
    if maskCounter <= mask:
      binaryFirstAddress += binaryRootAddress[i][j]
    elif maskCounter == 32:
      binaryFirstAddress += '1'
    else:
      binaryFirstAddress += '0'
  if i != 3:
    binaryFirstAddress += '.'
firstAddress = binaryToDecimal(binaryFirstAddress)

binaryLastAddress = ""
for i in range(0, 4):
  for j in range(0, 8):
    maskCounter = 8 * i + j + 1
    if maskCounter <= mask:
      binaryLastAddress += binaryRootAddress[i][j]
    elif maskCounter == 32:
      binaryLastAddress += '0'
    else:
      binaryLastAddress += '1'
  if i != 3:
    binaryLastAddress += '.'
lastAddress = binaryToDecimal(binaryLastAddress)

binaryBroadcastAddress = ""
for i in range(0, 4):
  for j in range(0, 8):
    maskCounter = 8 * i + j + 1
    if maskCounter <= mask:
      binaryBroadcastAddress += binaryRootAddress[i][j]
    else:
      binaryBroadcastAddress += '1'
  if i != 3:
    binaryBroadcastAddress += '.'
broadcastAddress = binaryToDecimal(binaryBroadcastAddress)

print("Binary address: " + binaryAddressStr)
print("Binary mask: " + binaryMaskStr)
print("Binary root address: " + binaryRootAddressStr)
print("First address: " + binaryFirstAddress + " => " + firstAddress)
print("Last address: " + binaryLastAddress + " => " + lastAddress)
print("Broadcast address: " + binaryBroadcastAddress + " => " + broadcastAddress)

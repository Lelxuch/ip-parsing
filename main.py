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
binaryMask = []

binaryMaskItem = ""
for i in range(1, 33):
  if i <= mask:
    binaryMaskItem += "1"
  else: 
    binaryMaskItem += "0"
  if(i % 8 == 0):
    binaryMask.append(binaryMaskItem)
    binaryMaskItem = ""

for i in splittedAddress:
  binaryAddress.append(str(format(int(i), '#010b'))[2:])

binaryRootAddress = []
binaryRootAddressItem = ""
for i in range(0, 4):
  for j in range(0, 8):
    # print(binaryAddress[i][j], binaryMask[i][j])
    if binaryAddress[i][j] == binaryMask[i][j] and binaryAddress[i][j] == '1':
      binaryRootAddressItem += '1'
    else:
      binaryRootAddressItem += '0'
  binaryRootAddress.append(binaryRootAddressItem)
  binaryRootAddressItem = ""

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

print("First address: " + binaryFirstAddress + " => " + firstAddress)
print("Last address: " + binaryLastAddress + " => " + lastAddress)
print("Broadcast address: " + binaryBroadcastAddress + " => " + broadcastAddress)
import atexit
import random
from bit import *
from bit.format import bytes_to_wif

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

my_colours = [W, R, G, O, B, P]
colour = random.choice(my_colours)
print(colour + "Loading Bitcoin list TXT Please Wait and Good Luck...")  
filename ='btc.txt'
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    add = file.read().split()
add = set(add)
print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))
x=int(input("'Start range in BITs (Puzzle StartNumber) -> "))
a = 2**x
y=int(input("Stop range Max in BITs (Puzzle StopNumber) -> "))
b = 2**y
print("Starting search... Please Wait min range: " + str(a))
print("Max range: " + str(b))
print("==========================================================")
print('Total Bitcoin Addresses Loaded and Checking : ',str (line_count))
count=0
total=0
while True:
    count+=1
    total+=4
    colour = random.choice(my_colours)
    key = Key.from_int(random.randint(a,b))
    wif = bytes_to_wif(key.to_bytes(), compressed=False) # Uncompressed WIF
    wif1 = bytes_to_wif(key.to_bytes(), compressed=True) # Compressed WIF
    key1 = Key(wif)
    caddr = key.address #Legacy compressed address
    uaddr = key1.address #Legacy uncompressed address
    saddr = key.segwit_address
    multisig = MultiSig(key, {key.public_key, key1.public_key}, 2)  #multisig Segwit address
    Multi= multisig.address
    print(colour + 'Scan : ', count , ' : Total : ', total, ' : HEX : ', key.to_hex(), end='\r')
    if caddr in add or uaddr in add or saddr in add or Multi in add:
        print(colour + '\nMatch Found')
        f=open(u"winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key.to_hex())
        f.write('\nBitcoin Compressed Address : ' + caddr)
        f.write('\nBitcoin Uncompressed Address : ' + uaddr)
        f.write('\nBitcoin  Segwit Address : ' + saddr)
        f.write('\nBitcoin Multisig Segwit Address: ' + Multi)
        f.write('\nPrivateKey (wif): ' + wif)
        f.write('\nPrivateKey (wif): ' + wif1)
        f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' ) 
        f.close()
        break
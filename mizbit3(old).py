# mizbit3.py Random Bitcoin Legacy compressed/uncompresses address and Segwit address. Check for Total Received Ammount 06/07/2021
# Good Luck and Happy Hunting. Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
import itertools
from bit import *
from bit.format import bytes_to_wif
import random
import urllib.request
import threading
import atexit
from time import time
from datetime import timedelta, datetime


colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'
colour_green='\033[0;32m'
colour_yellow='\033[0;33m'
colour_purple='\033[0;35m'



def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))


def log(txt, elapsed=None):
    print('\n ' + colour_cyan + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' + colour_reset)
    if elapsed:
        print("\n " + colour_red + " [TIMING]> Elapsed time ==> " + elapsed + "\n" + colour_reset)


def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))


start = time()
atexit.register(end_log)
log("Start Program")


print(colour_cyan + "mizbit3.py---" + colour_red + "Random Scan for bitcoin Addresses Total Received Ammount---------mizogg.co.uk" + colour_cyan + "---mizbit3.py"  + colour_reset + seconds_to_str())
threadCount = input('Best Run on 1 thread to not block API but you can try more : How many threads to run?:  ')
print(colour_yellow+ "Start search... Pick Range to start (Example Puzzle 64 starting Range 18446744073709551615 ):"+ colour_reset)
x=int(input("'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
print(colour_purple +"Starting search... Please Wait "+ colour_reset)
print("==========================================================")

def seek():
    count=0
    total=0
    while True:
        try:
            ran= random.randint(x,y)
            key = Key.from_int(ran)
            seed=str(ran)
            wif = bytes_to_wif(key.to_bytes(), compressed=False)
            wif2 = bytes_to_wif(key.to_bytes(), compressed=True)
            key1 = Key(wif)
            caddr = key.address #Legacy compressed address
            uaddr = key1.address #Legacy uncompressed address
            saddr = key.segwit_address  #Segwit address
            count+=1*int(threadCount)
            total+=3*int(threadCount)

            contents1 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + caddr).read()
            contents2 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + uaddr).read()
            contents3 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + saddr).read()
            if int(contents1) > 0 or int(contents2) > 0 or int(contents3) > 0:
                print (colour_purple +  ' <================================= WINNER Total Received Ammount WINNER =================================>' + '\n' +  colour_reset)
                print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + caddr + colour_green + ' : Balance : ' + str(contents1.decode('UTF8')) + colour_reset)
                print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + uaddr + colour_green + ' : Balance : ' + str(contents2.decode('UTF8')) + colour_reset)
                print (colour_yellow + 'Congraz you have found wallet with a balance : ' + colour_reset + saddr + colour_green + ' : Balance : ' + str(contents3.decode('UTF8')) + colour_reset)
                print(colour_red + ' PrivateKey (wif) Compressed : ' + colour_yellow + wif2 + colour_reset)
                print(colour_red + ' PrivateKey (wif) UnCompressed : ' + colour_yellow + wif + colour_reset)
                print(colour_green + "\nMatching Key ==== Found!!!\n PrivateKey  (hex): " + colour_yellow + key.to_hex() + colour_reset)
                print(colour_green + "\nMatching Key ==== Found!!!\n PrivateKey  (dec): " + colour_yellow + seed + colour_reset)
                print (colour_purple +  ' <================================= WINNER Total Received Ammount WINNER =================================>' + '\n' +  colour_reset)
                f=open(u"winner.txt","a")
                f.write('\n=============Bitcoin Address with Total Received Ammount=====================')
                f.write('\nPrivateKey (hex): ' + key.to_hex())
                f.write('\nBitcoin Address Compressed : ' + caddr)
                f.write('\nBitcoin Address UnCompressed :' + uaddr)
                f.write('\nBitcoin Segwit Address :' + saddr)
                f.write('\nPrivateKey (wif) Compressed : ' + wif2)
                f.write('\nPrivateKey (wif) UnCompressed : ' + wif)
                f.write('\n=============Bitcoin Address with Total Received Ammount=====================')
                f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' ) 
                f.close()
                continue

                pass
            else:
                print(colour_cyan + "mizbit3.py---" + colour_red + "Random Scan for bitcoin Addresses Total Received Ammount------Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD" + colour_cyan + "---mizbit3.py"  + colour_reset + seconds_to_str())
                print (colour_green + "Scan Number" + ' : ' + colour_reset + str (count) + ' : ' + colour_green + "Total Wallets Checked" + ' : ' + colour_reset + str (total))
                print(colour_red + ' PrivateKey (hex) : ' + colour_yellow + key.to_hex() + colour_reset)
                print(colour_red + ' PrivateKey (dec) : ' + colour_yellow + seed + colour_reset)
                print(colour_red + ' PrivateKey (wif) Compressed : ' + colour_yellow + wif2 + colour_reset)
                print(colour_red + ' PrivateKey (wif) UnCompressed : ' + colour_yellow + wif + colour_reset)
                print (colour_green +  ' <================================= Bitcoin Addresses Checked for Total Received Ammount =================================>' + '\n' +  colour_reset)
                print(colour_green + "COMPRESSED   BTC:  " + caddr + colour_yellow + ' : ' + key.to_hex() + ' : ' + colour_red + str(contents1.decode('UTF8')) + colour_reset)
                print(colour_green + "UNCOMPRESSED BTC:  " + uaddr + colour_yellow + ' : ' + key1.to_hex() + ' : ' + colour_red + str(contents2.decode('UTF8')) + colour_reset)
                print(colour_green + "Segwit Address BTC:  " + saddr + colour_yellow + ' : ' + key.to_hex() + ' : ' + colour_red + str(contents3.decode('UTF8')) + colour_reset)
                print (colour_green +  ' <================================= Bitcoin Addresses Checked for Total Received Ammount =================================>' + '\n' +  colour_reset)

        except:
            pass


threads = []


for i in range(int(threadCount)):
    t = threading.Thread(target=seek)
    threads.append(t)
    t.start()
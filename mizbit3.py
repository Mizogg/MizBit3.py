# mizbit3.py Random Bitcoin Legacy compressed/uncompresses address and Segwit address. Check for Total Received Ammount Using blockchain.info API 08/08/2021
# Good Luck and Happy Hunting. Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
from bit import *
from bit.format import bytes_to_wif
import random
import urllib.request
import atexit
from time import time
from datetime import timedelta, datetime
import colorama
from colorama import Fore, Back, Style
colorama.init()

def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))


def log(txt, elapsed=None):
    print('\n ' + Fore.BLUE + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' )
    if elapsed:
        print("\n " + Fore.RED + " [TIMING]> Elapsed time ==> " + elapsed + "\n" )


def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))


start = time()
atexit.register(end_log)
log("Start Program")

x=1
y=115792089237316195423570985008687907852837564279074904382605163141518161494336
print(Fore.RED + "Starting search... Please Wait ")
print("=====================================================")

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
        count+=1
        total+=3
        contents1 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + caddr).read()
        contents2 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + uaddr).read()
        contents3 = urllib.request.urlopen("https://blockchain.info/q/getreceivedbyaddress/" + saddr).read()
        if int(contents1) > 0 or int(contents2) > 0 or int(contents3) > 0:
            print (Fore.BLUE +  ' <================================= WINNER Total Received Ammount WINNER =================================>' + '\n' +  Style.RESET_ALL)
            print (Fore.YELLOW + 'Congraz you have found wallet with a balance : ' + Style.RESET_ALL + caddr + Fore.GREEN + ' : Balance : ' + str(contents1.decode('UTF8')) + Style.RESET_ALL)
            print (Fore.YELLOW + 'Congraz you have found wallet with a balance : ' + Style.RESET_ALL + uaddr + Fore.GREEN + ' : Balance : ' + str(contents2.decode('UTF8')) + Style.RESET_ALL)
            print (Fore.YELLOW + 'Congraz you have found wallet with a balance : ' + Style.RESET_ALL + saddr + Fore.GREEN + ' : Balance : ' + str(contents3.decode('UTF8')) + Style.RESET_ALL)
            print(Fore.RED + ' PrivateKey (wif) Compressed : ' + Fore.YELLOW + wif2 + Style.RESET_ALL)
            print(Fore.RED + ' PrivateKey (wif) UnCompressed : ' + Fore.YELLOW + wif + Style.RESET_ALL)
            print(Fore.GREEN + "\nMatching Key ==== Found!!!\n PrivateKey  (hex): " + Fore.YELLOW + key.to_hex() + Style.RESET_ALL)
            print(Fore.GREEN + "\nMatching Key ==== Found!!!\n PrivateKey  (dec): " + Fore.YELLOW + seed + Style.RESET_ALL)
            print (Fore.BLUE +  ' <================================= WINNER Total Received Ammount WINNER =================================>' + '\n' +  Style.RESET_ALL)
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
            print(Fore.BLUE + "mizbit3.py---" + Fore.RED + "Random Scan for bitcoin Addresses Total Received Ammount------Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD" + Fore.BLUE + "---mizbit3.py"  + Style.RESET_ALL + seconds_to_str())
            print (Fore.GREEN + "Scan Number" + ' : ' + Style.RESET_ALL + str (count) + ' : ' + Fore.GREEN + "Total Wallets Checked" + ' : ' + Style.RESET_ALL + str (total))
            print(Fore.RED + ' PrivateKey (hex) : ' + Fore.YELLOW + key.to_hex() + Style.RESET_ALL)
            print(Fore.RED + ' PrivateKey (dec) : ' + Fore.YELLOW + seed + Style.RESET_ALL)
            print(Fore.RED + ' PrivateKey (wif) Compressed : ' + Fore.YELLOW + wif2 + Style.RESET_ALL)
            print(Fore.RED + ' PrivateKey (wif) UnCompressed : ' + Fore.YELLOW + wif + Style.RESET_ALL)
            print (Fore.GREEN +  ' <================================= Bitcoin Addresses Checked for Total Received Ammount =================================>' + '\n' +  Style.RESET_ALL)
            print(Fore.GREEN + "COMPRESSED   BTC:  " + caddr + Fore.YELLOW + ' : ' + key.to_hex() + ' : ' + Fore.RED + str(contents1.decode('UTF8')) + Style.RESET_ALL)
            print(Fore.GREEN + "UNCOMPRESSED BTC:  " + uaddr + Fore.YELLOW + ' : ' + key1.to_hex() + ' : ' + Fore.RED + str(contents2.decode('UTF8')) + Style.RESET_ALL)
            print(Fore.GREEN + "Segwit Address BTC:  " + saddr + Fore.YELLOW + ' : ' + key.to_hex() + ' : ' + Fore.RED + str(contents3.decode('UTF8')) + Style.RESET_ALL)
            print (Fore.GREEN +  ' <================================= Bitcoin Addresses Checked for Total Received Ammount =================================>' + '\n' +  Style.RESET_ALL)

    except:
        pass
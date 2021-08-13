# mizbit5.py Random Bitcoin Legacy compressed/uncompresses address and Segwit address. BTC/ETH/BNB Check for Transactions/Balance/Received Ammount Using blockchain.info, ethplorer.io and bscscan.com API 13/08/2021
# Good Luck and Happy Hunting. Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
from bit import *
from bit.format import bytes_to_wif
import eth_keys
from eth_keys import keys
import random
import urllib.request
import requests
import atexit
from time import time
from datetime import timedelta, datetime
import colorama
from colorama import Fore, Back, Style
colorama.init()

def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    else:
        return str(timedelta(seconds=elapsed))


def log(txt, elapsed=None):
    print('\n ' + Fore.BLUE + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' )
    if elapsed:
        print('\n ' + Fore.RED + ' [TIMING]> Elapsed time ==> ' + elapsed + '\n' )


def end_log():
    end = time()
    elapsed = end-start
    log('End Program', seconds_to_str(elapsed))


start = time()
atexit.register(end_log)
log('Start Program')

x=1
y=115792089237316195423570985008687907852837564279074904382605163141518161494336
print(Fore.RED + 'Starting search... Please Wait ')
print('=====================================================')

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
        myhex = '%064x' % ran
        private_key = myhex[:64]
        private_key_bytes = bytes.fromhex(private_key)
        public_key_hex = keys.PrivateKey(private_key_bytes).public_key
        public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
        ethadd = keys.PublicKey(public_key_bytes).to_address()			#Eth address
        bnbadd = keys.PublicKey(public_key_bytes).to_address()			#BNB address
        count+=1
        total+=5
        api1='?apiKey=freekey' # Get FREE API KEY from https://ethplorer.io/
        api2='?apiKey=freekey' # Get FREE API KEY from https://ethplorer.io/
        api3='?apiKey=freekey' # Get FREE API KEY from https://ethplorer.io/
        api4='?apiKey=freekey' # Get FREE API KEY from https://ethplorer.io/
        api5='?apiKey=freekey' # Get FREE API KEY from https://ethplorer.io/
        api6='?apiKey=freekey' # Get FREE API KEY from https://ethplorer.io/
        #mylist = [str(api1), str(api2)] # 2 API KEYS
        #mylist = [str(api1), str(api2), str(api3), str(api4)] # 4 API KEYS
        mylist = [str(api1), str(api2), str(api3), str(api4), str(api5), str(api6)] # 6 API KEYS
        apikeys=random.choice(mylist)
        apibnb1= '&apikey=freekey' ## Get FREE API KEY from https://bscscan.com/
        apibnb2= '&apikey=freekey' ## Get FREE API KEY from https://bscscan.com/
        apibnb3= '&apikey=freekey' ## Get FREE API KEY from https://bscscan.com/
        apibnb4= '&apikey=freekey' ## Get FREE API KEY from https://bscscan.com/
        apibnb5= '&apikey=freekey' ## Get FREE API KEY from https://bscscan.com
        apibnb6= '&apikey=freekey' ## Get FREE API KEY from https://bscscan.com/
        #mylist1 = [str(apibnb1), str(apibnb2)] # 2 API KEYS
        #mylist1 = [str(apibnb1), str(apibnb2), str(apibnb3)] # 3 API KEYS
        #mylist1 = [str(apibnb1), str(apibnb2), str(apibnb3), str(apibnb4)] # 4 API KEYS
        mylist1 = [str(apibnb1), str(apibnb2), str(apibnb3), str(apibnb4), str(apibnb5), str(apibnb6)] # 6 API KEYS
        apikeysbnb=random.choice(mylist1)
        contents1 = urllib.request.urlopen('https://blockchain.info/q/getreceivedbyaddress/' + caddr).read()
        contents2 = urllib.request.urlopen('https://blockchain.info/q/getreceivedbyaddress/' + uaddr).read()
        contents3 = urllib.request.urlopen('https://blockchain.info/q/getreceivedbyaddress/' + saddr).read()
        blocs=requests.get('https://api.ethplorer.io/getAddressInfo/' + ethadd +apikeys)
        ress = blocs.json()
        TXS = dict(ress)['countTxs']
        blocs1 = requests.get('https://api.bscscan.com/api?module=account&action=balance&address=' + bnbadd + apikeysbnb)
        ress1 = blocs1.json()
        balancebnb = dict(ress1)['result']
        if int(contents1) > 0 or int(contents2) > 0 or int(contents3) > 0 or int(TXS) > 0 or int(balancebnb) > 0:
            print(Fore.BLUE,  ' <=========== WINNER Transactions/Balance/Received Ammount WINNER ===========>\n',  Style.RESET_ALL)
            print(Fore.YELLOW, 'Congraz found a BTC wallet with a Received  : ', Style.RESET_ALL, caddr, Fore.GREEN, '        : Received= ', str(contents1.decode('UTF8')), Style.RESET_ALL)
            print(Fore.YELLOW, 'Congraz found a BTC wallet with a Received  : ', Style.RESET_ALL, uaddr, Fore.GREEN, '        : Received= ', str(contents2.decode('UTF8')), Style.RESET_ALL)
            print(Fore.YELLOW, 'Congraz found a BTC wallet with a Received  : ', Style.RESET_ALL, saddr, Fore.GREEN, '        : Received= ', str(contents3.decode('UTF8')), Style.RESET_ALL)
            print(Fore.YELLOW, 'Congraz found a ETH wallet with Transactions:', Style.RESET_ALL, ethadd, Fore.GREEN, ' : TX      = ', str(TXS), Style.RESET_ALL)
            print(Fore.YELLOW, 'Congraz found a BNB wallet with a Balance   :', Style.RESET_ALL, bnbadd, Fore.GREEN, ' : Balance = ', str(balancebnb), Style.RESET_ALL)
            print(Fore.RED, ' PrivateKey (wif) Compressed : ', Fore.YELLOW, wif2, Style.RESET_ALL)
            print(Fore.RED, ' PrivateKey (wif) UnCompressed : ', Fore.YELLOW, wif, Style.RESET_ALL)
            print(Fore.GREEN, '\nMatching Key ==== Found!!!\n PrivateKey  (hex): ', Fore.YELLOW, key.to_hex(), Style.RESET_ALL)
            print(Fore.GREEN, '\nMatching Key ==== Found!!!\n PrivateKey  (dec): ', Fore.YELLOW, seed, Style.RESET_ALL)
            print(Fore.BLUE,  '\n <=========== WINNER Transactions/Balance/Received Ammount WINNER ===========>\n',  Style.RESET_ALL)
            f=open('winner.txt','a')
            f.write('\n=====BTC/ETH/BNB Address with Transactions/Balance/Received Ammount=====')
            f.write('\nPrivateKey (hex): ' + key.to_hex())
            f.write('\nPrivateKey (dec): ' + str(seed))
            f.write('\nBitcoin Address Compressed: ' + caddr + '  : Received = ' + str(contents1.decode('UTF8')))
            f.write('\nBitcoin Address UnCompressed:' + uaddr + '  : Received = ' + str(contents2.decode('UTF8')))
            f.write('\nBitcoin Segwit Address:' + saddr + '  : Received = ' + str(contents3.decode('UTF8')))
            f.write('\nEth Address: ' + ethadd + '  : TX = ' + str(TXS))
            f.write('\nBNB Address: ' + bnbadd + '  : Balance = ' + str(balancebnb))
            f.write('\nPrivateKey (wif) Compressed : ' + wif2)
            f.write('\nPrivateKey (wif) UnCompressed : ' + wif)
            f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====\n' ) 
            f.close()
            continue

            pass
        else:
            print(Fore.BLUE, 'mizbit5.py---', Fore.RED, 'Random Scan for BTC/ETH/BNB Addresses Transactions/Balance/Received Ammount', Fore.BLUE, '---mizbit5.py', Style.RESET_ALL)
            print (Fore.GREEN, 'Scan Number : ', Style.RESET_ALL, str (count), ' : ' + Fore.GREEN, 'Total Wallets Checked : ', Style.RESET_ALL, str (total))
            print(Fore.RED, ' PrivateKey (hex) : ', Fore.YELLOW, key.to_hex(), Style.RESET_ALL)
            print(Fore.RED, ' PrivateKey (dec) : ', Fore.YELLOW, seed, Style.RESET_ALL)
            print(Fore.RED, ' PrivateKey (wif) Compressed   : ', Fore.YELLOW, wif2, Style.RESET_ALL)
            print(Fore.RED, ' PrivateKey (wif) UnCompressed : ', Fore.YELLOW, wif, Style.RESET_ALL)
            print(Fore.GREEN, ' <====== BTC/ETH/BNB Addresses Checked for Transactions/Balance/Received Ammount ======>\n', Style.RESET_ALL)
            print(Fore.GREEN, 'COMPRESSED   BTC        :  ', caddr, Fore.YELLOW, '         : Received= ', Fore.RED, str(contents1.decode('UTF8')), Style.RESET_ALL)
            print(Fore.GREEN, 'UNCOMPRESSED BTC        :  ', uaddr, Fore.YELLOW, '         : Received= ', Fore.RED, str(contents2.decode('UTF8')), Style.RESET_ALL)
            print(Fore.GREEN, 'Segwit Address BTC      :  ', saddr, Fore.YELLOW, '         : Received= ', Fore.RED, str(contents3.decode('UTF8')), Style.RESET_ALL)
            print(Fore.GREEN, 'Ethereum Address ETH    :  ', ethadd, Fore.YELLOW, ' : TX      = ', Fore.RED, str(TXS), Style.RESET_ALL)
            print(Fore.GREEN, 'Binance Coin BNB Address:  ', bnbadd, Fore.YELLOW, ' : Balance = ', Fore.RED, str(balancebnb), Style.RESET_ALL)
            print(Fore.GREEN, '\n <====== BTC/ETH/BNB Addresses Checked for Transactions/Balance/Received Ammount ======>\n', Style.RESET_ALL)

    except:
        pass
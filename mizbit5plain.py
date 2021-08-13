# mizbit5plain.py Random Bitcoin Legacy compressed/uncompresses address and Segwit address. BTC/ETH/BNB Check for Transactions/Balance/Received Ammount Using blockchain.info, ethplorer.io and bscscan.com API 13/08/2021
from bit import *
from bit.format import bytes_to_wif
import eth_keys
from eth_keys import keys
import random
import urllib.request
import requests

x=1
y=115792089237316195423570985008687907852837564279074904382605163141518161494336
print('Starting search... Please Wait ')
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
            print(' <=========== WINNER Transactions/Balance/Received Ammount WINNER ===========>\n')
            print('Congraz found a BTC wallet with a Received  : ', caddr, '        : Received= ', str(contents1.decode('UTF8')))
            print('Congraz found a BTC wallet with a Received  : ', uaddr, '        : Received= ', str(contents2.decode('UTF8')))
            print('Congraz found a BTC wallet with a Received  : ', saddr, '        : Received= ', str(contents3.decode('UTF8')))
            print('Congraz found a ETH wallet with Transactions:', ethadd, ' : TX      = ', str(TXS))
            print('Congraz found a BNB wallet with a Balance   :', bnbadd, ' : Balance = ', str(balancebnb))
            print(' PrivateKey (wif) Compressed : ', wif2)
            print(' PrivateKey (wif) UnCompressed : ', wif)
            print('\nMatching Key ==== Found!!!\n PrivateKey  (hex): ', key.to_hex())
            print('\nMatching Key ==== Found!!!\n PrivateKey  (dec): ', seed)
            print('\n <=========== WINNER Transactions/Balance/Received Ammount WINNER ===========>\n')
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
            print ('Scan Number : ', str (count), ' : ' + 'Total Wallets Checked : ', str (total))
            print(' PrivateKey (hex) : ', key.to_hex())
            print(' PrivateKey (dec) : ', seed)
            print(' PrivateKey (wif) Compressed   : ', wif2)
            print(' PrivateKey (wif) UnCompressed : ', wif)
            print(' <====== BTC/ETH/BNB Addresses Checked for Transactions/Balance/Received Ammount ======>\n')
            print('COMPRESSED   BTC        :  ', caddr, '         : Received= ', str(contents1.decode('UTF8')))
            print('UNCOMPRESSED BTC        :  ', uaddr, '         : Received= ', str(contents2.decode('UTF8')))
            print('Segwit Address BTC      :  ', saddr, '         : Received= ', str(contents3.decode('UTF8')))
            print('Ethereum Address ETH    :  ', ethadd, ' : TX      = ', str(TXS))
            print('Binance Coin BNB Address:  ', bnbadd, ' : Balance = ', str(balancebnb))
            print('\n <====== BTC/ETH/BNB Addresses Checked for Transactions/Balance/Received Ammount ======>\n')

    except:
        pass
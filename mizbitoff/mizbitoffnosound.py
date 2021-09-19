from bit import *
from bit.format import bytes_to_wif
import random
import codecs
from rich.console import Console

import smtplib
gmail_user = 'youremail@gmail.com'
gmail_password = 'yourpassword'

console = Console()
console.clear()
console.print(" [yellow]----------------------------------------------------[/yellow]")
console.print("[yellow]                 Starting search...[/yellow]")
console.print("[yellow]                MIZBIT4 OFF-LINE...[/yellow]")
console.print(" [yellow]----------------------------------------------------[/yellow]")
console.print('[purple]Loading Bitcoin List . .. . .. . . . [/purple]')
filename ='btc.txt'
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    add = file.read().split()
add = set(add)
console.print('[purple] Total Bitcoin Addresses Loaded and Checking : [/purple]',str (line_count))
console.print("[yellow] Start search... Pick Range to start (Example Puzzle 64 starting Range 18446744073709551615 [/yellow] ):")
x=int(input("start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 ->"))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 ->"))
console.print("[purple]Starting search... Please Wait [/purple]")
console.print("==========================================================")
count=0
total=0
while True:
        ran= random.randint(x,y)
        key = Key.from_int(ran)
        seed=str(ran)
        wif = bytes_to_wif(key.to_bytes(), compressed=False)
        wif1 = bytes_to_wif(key.to_bytes(), compressed=True)
        key1 = Key(wif)
        caddr = key.address #Legacy compressed address
        uaddr = key1.address #Legacy uncompressed address
        saddr = key.segwit_address  #Segwit address
        multisig = MultiSig(key, {key.public_key, key1.public_key}, 2)  #multisig Segwit address
        Multi= multisig.address
        count+=1
        total+=4
        console.print('[red] [' + str(count) + '] ------------------------[/red]')
        console.print('[red] Total Checked [' + str(total) + '] [/red]')
        console.print('[lightblue] PrivateKey (hex) :  [' + key.to_hex() + '] [/lightblue]')
        console.print('[lightblue] PrivateKey (dec) : [' + seed + '] [/lightblue]')
        print('PrivateKey (wif) Compressed   : ' + wif1)
        print('PrivateKey (wif) UnCompressed : ' + wif)
        print('COMPRESSED   BTC: ' + caddr)
        print('UNCOMPRESSED BTC: ' + uaddr)
        print('Segwit Address BTC: ' + saddr)
        print('Multisig Segwit Address BTC:  ' + Multi)
        if caddr in add or uaddr in add or saddr in add or Multi in add:
            console.print('[green] [' + str(count) + '] ------------------------[/green]')
            console.print('[green] Total Checked [' + str(total) + '] [/green]')
            console.print('[green] \nMatching Key ==== Found!!!\n PrivateKey  (hex):  [' + key.to_hex() + '] [/green]')
            console.print('[green] \nMatching Key ==== Found!!!\n PrivateKey  (dec): [' + seed + '] [/green]')
            print('COMPRESSED   BTC:  ' + caddr)
            print('UNCOMPRESSED BTC:  ' + uaddr)
            print('Segwit Address BTC:  ' + saddr)
            print('Multisig Segwit Address BTC:  ' + Multi)
            print('PrivateKey (wif) Compressed : ' + wif1)
            print('PrivateKey (wif) UnCompressed : ' + wif)
            f=open("winner.txt","a")
            f.write('\nPrivateKey (hex): ' + key.to_hex())
            f.write('\nPrivateKey (dec): ' + str(seed))
            f.write('\nBitcoin Address Compressed : ' + caddr)
            f.write('\nBitcoin Address UnCompressed :' + uaddr)
            f.write('\nBitcoin Segwit Address :' + saddr)
            f.write('\nBitcoin Multisig Segwit Address: ' + Multi)
            f.write('\nPrivateKey (wif) Compressed : ' + wif1)
            f.write('\nPrivateKey (wif) UnCompressed : ' + wif)
            f.write('\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====' ) 
            f.close()

            sent_from = gmail_user
            to = ['youremail@gmail.com']
            subject = 'OMG Super Important Message'
            body = '\nPrivateKey (hex): ' + key.to_hex() + '\nPrivateKey (dec): ' + str(seed) + '\nBitcoin Address Compressed : ' + caddr + '\nBitcoin Address UnCompressed :' + uaddr + '\nBitcoin Segwit Address       :' + saddr + '\nBitcoin MultisigSegwit Address       :' + Multi + '\nPrivateKey (wif) Compressed : ' + wif1 + '\nPrivateKey (wif) UnCompressed : ' + wif +'\n =====Made by mizogg.co.uk Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD =====\n'
            
            email_text = """\
                From: %s
                To: %s
                Subject: %s

                %s
                """ % (sent_from, ", ".join(to), subject, body)

            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(gmail_user, gmail_password)
                server.sendmail(sent_from, to, email_text)
                server.close()
            
                console.print ('[purple] Email sent! [/purple]')
            except:
                console.print('Something went wrong...')


###How to Setup###
###Must edit Lines 8&9 Your sending email and password

###Необходимо отредактировать строки 8 и 9 Ваш адрес электронной почты и пароль для отправки.

###gmail_user = 'youremail@gmail.com'
###gmail_password = 'yourpassword'


###Must Edit Line 84 Receiving Email Address

###Необходимо изменить строку 84 Получение адреса электронной почты

###to = ['youremail@gmail.com']
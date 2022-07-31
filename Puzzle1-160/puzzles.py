import ctypes
try:
    from bloomfilter import BloomFilter, ScalableBloomFilter, SizeGrowthRate
    from pathlib import Path
    from bit import *
    from bit.format import bytes_to_wif
    from rich import print
    
except ImportError:
    import subprocess

    subprocess.check_call(["python", '-m', 'pip', 'install', 'bit'])
    subprocess.check_call(["python", '-m', 'pip', 'install', 'simplebloomfilter'])
    subprocess.check_call(["python", '-m', 'pip', 'install', 'bitarray==1.9.2'])
    subprocess.check_call(["python", '-m', 'pip', 'install', 'rich==1.0.0'])
    from bloomfilter import BloomFilter, ScalableBloomFilter, SizeGrowthRate
    from pathlib import Path
    from bit import *
    from bit.format import bytes_to_wif
    from rich import print
ctypes.windll.kernel32.SetConsoleTitleW('Mizogg Corp.(PUZZLE.py)')
mizogg= '''[red]
              ___            ___  
             (o o)          (o o) 
            (  V  ) MIZOGG (  V  )
            --m-m------------m-m--
[/red]'''
print(mizogg)
bloombtc = Path(__file__).resolve()
ressbtc = bloombtc.parents[0] / 'puzzle.bf'
with open(ressbtc, "rb") as fp:
    bloom_filterbtc = BloomFilter.load(fp)
addr_count = len(bloom_filterbtc)    
print('Total Bitcoin Addresses Loaded and Checking : ',str (addr_count))  
count=0
Start=1
Stop=730750818665451459101842416358141509827966271487
while Start < Stop:
    dec=Start
    mag = 1
    key = Key.from_int(dec)
    caddr = key.address
    print(dec, end='\r')
    count+=1
    ctypes.windll.kernel32.SetConsoleTitleW('Total : ' + str(count))
    Start+=mag
    if caddr in bloom_filterbtc:
        HEX = "%064x" % dec 
        wifc = bytes_to_wif(key.to_bytes(), compressed=True)
        print('\nMatch Found')
        print('\nPrivatekey (dec): ', dec,'\nPrivatekey (hex): ', HEX, '\nPrivatekey compressed: ', wifc, '\nPublic Address Compressed: ', caddr)
        f=open("winner.txt","a")
        f.write('\nPrivatekey (dec): ' + str(dec))
        f.write('\nPrivatekey (hex): ' + HEX)
        f.write('\nPrivatekey compressed: ' + wifc)
        f.write('\nPublic Address Compressed: ' + caddr)
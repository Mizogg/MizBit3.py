#256BIT.py Made by Mizogg (https://mizogg.co.uk)
from bit import *
from bit.format import bytes_to_wif
import random

print('Bitcoin Addresses Loading Please Wait: ')
filename ='puzzle.txt'
with open(filename) as f:
    line_count = 0
    for line in f:
        line != "\n"
        line_count += 1
with open(filename) as file:
    add = file.read().split()
add = set(add)

a = 2**0
b = 2**256

count=0
total=0
while True:
    ran = random.randrange(a,b)
    seed = str(ran)
    key = Key.from_int(ran)
    key1 = Key.from_int(ran+1)
    key2 = Key.from_int(ran+2)
    key3 = Key.from_int(ran+3)
    key4 = Key.from_int(ran+4)
    key5 = Key.from_int(ran+5)
    key6 = Key.from_int(ran+6)
    key7 = Key.from_int(ran+7)
    key8 = Key.from_int(ran+8)
    key9 = Key.from_int(ran+9)
    key10 = Key.from_int(ran+10)
    key11 = Key.from_int(ran+11)
    key12 = Key.from_int(ran+12)
    key13 = Key.from_int(ran+13)
    key14 = Key.from_int(ran+14)
    key15 = Key.from_int(ran+15)
    key16 = Key.from_int(ran+16)
    key17 = Key.from_int(ran+17)
    key18 = Key.from_int(ran+18)
    key19 = Key.from_int(ran+19)
    key20 = Key.from_int(ran+20)
    key21 = Key.from_int(ran+21)
    key22 = Key.from_int(ran+22)
    key23 = Key.from_int(ran+23)
    key24 = Key.from_int(ran+24)
    key25 = Key.from_int(ran+25)
    key26 = Key.from_int(ran+26)
    key27 = Key.from_int(ran+27)
    key28 = Key.from_int(ran+28)
    key29 = Key.from_int(ran+29)
    key30 = Key.from_int(ran+30)
    key31 = Key.from_int(ran+31)
    key32 = Key.from_int(ran+32)
    key33 = Key.from_int(ran+33)
    key34 = Key.from_int(ran+34)
    key35 = Key.from_int(ran+35)
    key36 = Key.from_int(ran+36)
    key37 = Key.from_int(ran+37)
    key38 = Key.from_int(ran+38)
    key39 = Key.from_int(ran+39)
    key40 = Key.from_int(ran+40)
    key41 = Key.from_int(ran+41)
    key42 = Key.from_int(ran+42)
    key43 = Key.from_int(ran+43)
    key44 = Key.from_int(ran+44)
    key45 = Key.from_int(ran+45)
    key46 = Key.from_int(ran+46)
    key47 = Key.from_int(ran+47)
    key48 = Key.from_int(ran+48)
    key49 = Key.from_int(ran+49)
    key50 = Key.from_int(ran+50)
    key51 = Key.from_int(ran+51)
    key52 = Key.from_int(ran+52)
    key53 = Key.from_int(ran+53)
    key54 = Key.from_int(ran+54)
    key55 = Key.from_int(ran+55)
    key56 = Key.from_int(ran+56)
    key57 = Key.from_int(ran+57)
    key58 = Key.from_int(ran+58)
    key59 = Key.from_int(ran+59)
    key60 = Key.from_int(ran+60)
    key61 = Key.from_int(ran+61)
    key62 = Key.from_int(ran+62)
    key63 = Key.from_int(ran+63)
    key64 = Key.from_int(ran+64)
    key65 = Key.from_int(ran+65)
    key66 = Key.from_int(ran+66)
    key67 = Key.from_int(ran+67)
    key68 = Key.from_int(ran+68)
    key69 = Key.from_int(ran+69)
    key70 = Key.from_int(ran+70)
    key71 = Key.from_int(ran+71)
    key72 = Key.from_int(ran+72)
    key73 = Key.from_int(ran+73)
    key74 = Key.from_int(ran+74)
    key75 = Key.from_int(ran+75)
    key76 = Key.from_int(ran+76)
    key77 = Key.from_int(ran+77)
    key78 = Key.from_int(ran+78)
    key79 = Key.from_int(ran+79)
    key80 = Key.from_int(ran+80)
    key81 = Key.from_int(ran+81)
    key82 = Key.from_int(ran+82)
    key83 = Key.from_int(ran+83)
    key84 = Key.from_int(ran+84)
    key85 = Key.from_int(ran+85)
    key86 = Key.from_int(ran+86)
    key87 = Key.from_int(ran+87)
    key88 = Key.from_int(ran+88)
    key89 = Key.from_int(ran+89)
    key90 = Key.from_int(ran+90)
    key91 = Key.from_int(ran+91)
    key92 = Key.from_int(ran+92)
    key93 = Key.from_int(ran+93)
    key94 = Key.from_int(ran+94)
    key95 = Key.from_int(ran+95)
    key96 = Key.from_int(ran+96)
    key97 = Key.from_int(ran+97)
    key98 = Key.from_int(ran+98)
    key99 = Key.from_int(ran+99)
    key100 = Key.from_int(ran+100)
    key101 = Key.from_int(ran+101)
    key102 = Key.from_int(ran+102)
    key103 = Key.from_int(ran+103)
    key104 = Key.from_int(ran+104)
    key105 = Key.from_int(ran+105)
    key106 = Key.from_int(ran+106)
    key107 = Key.from_int(ran+107)
    key108 = Key.from_int(ran+108)
    key109 = Key.from_int(ran+109)
    key110 = Key.from_int(ran+110)
    key111 = Key.from_int(ran+111)
    key112 = Key.from_int(ran+112)
    key113 = Key.from_int(ran+113)
    key114 = Key.from_int(ran+114)
    key115 = Key.from_int(ran+115)
    key116 = Key.from_int(ran+116)
    key117 = Key.from_int(ran+117)
    key118 = Key.from_int(ran+118)
    key119 = Key.from_int(ran+119)
    key120 = Key.from_int(ran+120)
    key121 = Key.from_int(ran+121)
    key122 = Key.from_int(ran+122)
    key123 = Key.from_int(ran+123)
    key124 = Key.from_int(ran+124)
    key125 = Key.from_int(ran+125)
    key126 = Key.from_int(ran+126)
    key127 = Key.from_int(ran+127)
    
    wifu = bytes_to_wif(key.to_bytes(), compressed=False) # Uncompressed WIF
    wifc = bytes_to_wif(key.to_bytes(), compressed=True) # Compressed WIF
    keyu = Key(wifu)
    wifu1 = bytes_to_wif(key1.to_bytes(), compressed=False) # Uncompressed WIF
    wifc1 = bytes_to_wif(key1.to_bytes(), compressed=True) # Compressed WIF
    keyu1 = Key(wifu1)
    wifu2 = bytes_to_wif(key2.to_bytes(), compressed=False) # Uncompressed WIF
    wifc2 = bytes_to_wif(key2.to_bytes(), compressed=True) # Compressed WIF
    keyu2 = Key(wifu2)
    wifu3 = bytes_to_wif(key3.to_bytes(), compressed=False) # Uncompressed WIF
    wifc3 = bytes_to_wif(key3.to_bytes(), compressed=True) # Compressed WIF
    keyu3 = Key(wifu3)
    wifu4 = bytes_to_wif(key4.to_bytes(), compressed=False) # Uncompressed WIF
    wifc4 = bytes_to_wif(key4.to_bytes(), compressed=True) # Compressed WIF
    keyu4 = Key(wifu4)
    wifu5 = bytes_to_wif(key5.to_bytes(), compressed=False) # Uncompressed WIF
    wifc5 = bytes_to_wif(key5.to_bytes(), compressed=True) # Compressed WIF
    keyu5 = Key(wifu5)
    wifu6 = bytes_to_wif(key6.to_bytes(), compressed=False) # Uncompressed WIF
    wifc6 = bytes_to_wif(key6.to_bytes(), compressed=True) # Compressed WIF
    keyu6 = Key(wifu6)
    wifu7 = bytes_to_wif(key7.to_bytes(), compressed=False) # Uncompressed WIF
    wifc7 = bytes_to_wif(key7.to_bytes(), compressed=True) # Compressed WIF
    keyu7 = Key(wifu7)
    wifu8 = bytes_to_wif(key8.to_bytes(), compressed=False) # Uncompressed WIF
    wifc8 = bytes_to_wif(key8.to_bytes(), compressed=True) # Compressed WIF
    keyu8 = Key(wifu8)
    wifu9 = bytes_to_wif(key9.to_bytes(), compressed=False) # Uncompressed WIF
    wifc9 = bytes_to_wif(key9.to_bytes(), compressed=True) # Compressed WIF
    keyu9 = Key(wifu9)
    wifu10 = bytes_to_wif(key10.to_bytes(), compressed=False) # Uncompressed WIF
    wifc10 = bytes_to_wif(key10.to_bytes(), compressed=True) # Compressed WIF
    keyu10 = Key(wifu10)
    wifu11 = bytes_to_wif(key11.to_bytes(), compressed=False) # Uncompressed WIF
    wifc11 = bytes_to_wif(key11.to_bytes(), compressed=True) # Compressed WIF
    keyu11 = Key(wifu11)
    wifu12 = bytes_to_wif(key12.to_bytes(), compressed=False) # Uncompressed WIF
    wifc12 = bytes_to_wif(key12.to_bytes(), compressed=True) # Compressed WIF
    keyu12 = Key(wifu12)
    wifu13 = bytes_to_wif(key13.to_bytes(), compressed=False) # Uncompressed WIF
    wifc13 = bytes_to_wif(key13.to_bytes(), compressed=True) # Compressed WIF
    keyu13 = Key(wifu13)
    wifu14 = bytes_to_wif(key14.to_bytes(), compressed=False) # Uncompressed WIF
    wifc14 = bytes_to_wif(key14.to_bytes(), compressed=True) # Compressed WIF
    keyu14 = Key(wifu14)
    wifu15 = bytes_to_wif(key15.to_bytes(), compressed=False) # Uncompressed WIF
    wifc15 = bytes_to_wif(key15.to_bytes(), compressed=True) # Compressed WIF
    keyu15 = Key(wifu15)
    wifu16 = bytes_to_wif(key16.to_bytes(), compressed=False) # Uncompressed WIF
    wifc16 = bytes_to_wif(key16.to_bytes(), compressed=True) # Compressed WIF
    keyu16 = Key(wifu16)
    wifu17 = bytes_to_wif(key17.to_bytes(), compressed=False) # Uncompressed WIF
    wifc17 = bytes_to_wif(key17.to_bytes(), compressed=True) # Compressed WIF
    keyu17 = Key(wifu17)
    wifu18 = bytes_to_wif(key18.to_bytes(), compressed=False) # Uncompressed WIF
    wifc18 = bytes_to_wif(key18.to_bytes(), compressed=True) # Compressed WIF
    keyu18 = Key(wifu18)
    wifu19 = bytes_to_wif(key19.to_bytes(), compressed=False) # Uncompressed WIF
    wifc19 = bytes_to_wif(key19.to_bytes(), compressed=True) # Compressed WIF
    keyu19 = Key(wifu19)
    wifu20 = bytes_to_wif(key20.to_bytes(), compressed=False) # Uncompressed WIF
    wifc20 = bytes_to_wif(key20.to_bytes(), compressed=True) # Compressed WIF
    keyu20 = Key(wifu20)
    wifu21 = bytes_to_wif(key21.to_bytes(), compressed=False) # Uncompressed WIF
    wifc21 = bytes_to_wif(key21.to_bytes(), compressed=True) # Compressed WIF
    keyu21 = Key(wifu21)
    wifu22 = bytes_to_wif(key22.to_bytes(), compressed=False) # Uncompressed WIF
    wifc22 = bytes_to_wif(key22.to_bytes(), compressed=True) # Compressed WIF
    keyu22 = Key(wifu22)
    wifu23 = bytes_to_wif(key23.to_bytes(), compressed=False) # Uncompressed WIF
    wifc23 = bytes_to_wif(key23.to_bytes(), compressed=True) # Compressed WIF
    keyu23 = Key(wifu23)
    wifu24 = bytes_to_wif(key24.to_bytes(), compressed=False) # Uncompressed WIF
    wifc24 = bytes_to_wif(key24.to_bytes(), compressed=True) # Compressed WIF
    keyu24 = Key(wifu24)
    wifu25 = bytes_to_wif(key25.to_bytes(), compressed=False) # Uncompressed WIF
    wifc25 = bytes_to_wif(key25.to_bytes(), compressed=True) # Compressed WIF
    keyu25 = Key(wifu25)
    wifu26 = bytes_to_wif(key26.to_bytes(), compressed=False) # Uncompressed WIF
    wifc26 = bytes_to_wif(key26.to_bytes(), compressed=True) # Compressed WIF
    keyu26 = Key(wifu26)
    wifu27 = bytes_to_wif(key27.to_bytes(), compressed=False) # Uncompressed WIF
    wifc27 = bytes_to_wif(key27.to_bytes(), compressed=True) # Compressed WIF
    keyu27 = Key(wifu27)
    wifu28 = bytes_to_wif(key28.to_bytes(), compressed=False) # Uncompressed WIF
    wifc28 = bytes_to_wif(key28.to_bytes(), compressed=True) # Compressed WIF
    keyu28 = Key(wifu28)
    wifu29 = bytes_to_wif(key29.to_bytes(), compressed=False) # Uncompressed WIF
    wifc29 = bytes_to_wif(key29.to_bytes(), compressed=True) # Compressed WIF
    keyu29 = Key(wifu29)
    wifu30 = bytes_to_wif(key30.to_bytes(), compressed=False) # Uncompressed WIF
    wifc30 = bytes_to_wif(key30.to_bytes(), compressed=True) # Compressed WIF
    keyu30 = Key(wifu30)
    wifu31 = bytes_to_wif(key31.to_bytes(), compressed=False) # Uncompressed WIF
    wifc31 = bytes_to_wif(key31.to_bytes(), compressed=True) # Compressed WIF
    keyu31 = Key(wifu31)
    wifu32 = bytes_to_wif(key32.to_bytes(), compressed=False) # Uncompressed WIF
    wifc32 = bytes_to_wif(key32.to_bytes(), compressed=True) # Compressed WIF
    keyu32 = Key(wifu32)
    wifu33 = bytes_to_wif(key33.to_bytes(), compressed=False) # Uncompressed WIF
    wifc33 = bytes_to_wif(key33.to_bytes(), compressed=True) # Compressed WIF
    keyu33 = Key(wifu33)
    wifu34 = bytes_to_wif(key34.to_bytes(), compressed=False) # Uncompressed WIF
    wifc34 = bytes_to_wif(key34.to_bytes(), compressed=True) # Compressed WIF
    keyu34 = Key(wifu34)
    wifu35 = bytes_to_wif(key35.to_bytes(), compressed=False) # Uncompressed WIF
    wifc35 = bytes_to_wif(key35.to_bytes(), compressed=True) # Compressed WIF
    keyu35 = Key(wifu35)
    wifu36 = bytes_to_wif(key36.to_bytes(), compressed=False) # Uncompressed WIF
    wifc36 = bytes_to_wif(key36.to_bytes(), compressed=True) # Compressed WIF
    keyu36 = Key(wifu36)
    wifu37 = bytes_to_wif(key37.to_bytes(), compressed=False) # Uncompressed WIF
    wifc37 = bytes_to_wif(key37.to_bytes(), compressed=True) # Compressed WIF
    keyu37 = Key(wifu37)
    wifu38 = bytes_to_wif(key38.to_bytes(), compressed=False) # Uncompressed WIF
    wifc38 = bytes_to_wif(key38.to_bytes(), compressed=True) # Compressed WIF
    keyu38 = Key(wifu38)
    wifu39 = bytes_to_wif(key39.to_bytes(), compressed=False) # Uncompressed WIF
    wifc39 = bytes_to_wif(key39.to_bytes(), compressed=True) # Compressed WIF
    keyu39 = Key(wifu39)
    wifu40 = bytes_to_wif(key40.to_bytes(), compressed=False) # Uncompressed WIF
    wifc40 = bytes_to_wif(key40.to_bytes(), compressed=True) # Compressed WIF
    keyu40 = Key(wifu40)
    wifu41 = bytes_to_wif(key41.to_bytes(), compressed=False) # Uncompressed WIF
    wifc41 = bytes_to_wif(key41.to_bytes(), compressed=True) # Compressed WIF
    keyu41 = Key(wifu41)
    wifu42 = bytes_to_wif(key42.to_bytes(), compressed=False) # Uncompressed WIF
    wifc42 = bytes_to_wif(key42.to_bytes(), compressed=True) # Compressed WIF
    keyu42 = Key(wifu42)
    wifu43 = bytes_to_wif(key43.to_bytes(), compressed=False) # Uncompressed WIF
    wifc43 = bytes_to_wif(key43.to_bytes(), compressed=True) # Compressed WIF
    keyu43 = Key(wifu43)
    wifu44 = bytes_to_wif(key44.to_bytes(), compressed=False) # Uncompressed WIF
    wifc44 = bytes_to_wif(key44.to_bytes(), compressed=True) # Compressed WIF
    keyu44 = Key(wifu44)
    wifu45 = bytes_to_wif(key45.to_bytes(), compressed=False) # Uncompressed WIF
    wifc45 = bytes_to_wif(key45.to_bytes(), compressed=True) # Compressed WIF
    keyu45 = Key(wifu45)
    wifu46 = bytes_to_wif(key46.to_bytes(), compressed=False) # Uncompressed WIF
    wifc46 = bytes_to_wif(key46.to_bytes(), compressed=True) # Compressed WIF
    keyu46 = Key(wifu46)
    wifu47 = bytes_to_wif(key47.to_bytes(), compressed=False) # Uncompressed WIF
    wifc47 = bytes_to_wif(key47.to_bytes(), compressed=True) # Compressed WIF
    keyu47 = Key(wifu47)
    wifu48 = bytes_to_wif(key48.to_bytes(), compressed=False) # Uncompressed WIF
    wifc48 = bytes_to_wif(key48.to_bytes(), compressed=True) # Compressed WIF
    keyu48 = Key(wifu48)
    wifu49 = bytes_to_wif(key49.to_bytes(), compressed=False) # Uncompressed WIF
    wifc49 = bytes_to_wif(key49.to_bytes(), compressed=True) # Compressed WIF
    keyu49 = Key(wifu49)
    wifu50 = bytes_to_wif(key50.to_bytes(), compressed=False) # Uncompressed WIF
    wifc50 = bytes_to_wif(key50.to_bytes(), compressed=True) # Compressed WIF
    keyu50 = Key(wifu50)
    wifu51 = bytes_to_wif(key51.to_bytes(), compressed=False) # Uncompressed WIF
    wifc51 = bytes_to_wif(key51.to_bytes(), compressed=True) # Compressed WIF
    keyu51 = Key(wifu51)
    wifu52 = bytes_to_wif(key52.to_bytes(), compressed=False) # Uncompressed WIF
    wifc52 = bytes_to_wif(key52.to_bytes(), compressed=True) # Compressed WIF
    keyu52 = Key(wifu52)
    wifu53 = bytes_to_wif(key53.to_bytes(), compressed=False) # Uncompressed WIF
    wifc53 = bytes_to_wif(key53.to_bytes(), compressed=True) # Compressed WIF
    keyu53 = Key(wifu53)
    wifu54 = bytes_to_wif(key54.to_bytes(), compressed=False) # Uncompressed WIF
    wifc54 = bytes_to_wif(key54.to_bytes(), compressed=True) # Compressed WIF
    keyu54 = Key(wifu54)
    wifu55 = bytes_to_wif(key55.to_bytes(), compressed=False) # Uncompressed WIF
    wifc55 = bytes_to_wif(key55.to_bytes(), compressed=True) # Compressed WIF
    keyu55 = Key(wifu55)
    wifu56 = bytes_to_wif(key56.to_bytes(), compressed=False) # Uncompressed WIF
    wifc56 = bytes_to_wif(key56.to_bytes(), compressed=True) # Compressed WIF
    keyu56 = Key(wifu56)
    wifu57 = bytes_to_wif(key57.to_bytes(), compressed=False) # Uncompressed WIF
    wifc57 = bytes_to_wif(key57.to_bytes(), compressed=True) # Compressed WIF
    keyu57 = Key(wifu57)
    wifu58 = bytes_to_wif(key58.to_bytes(), compressed=False) # Uncompressed WIF
    wifc58 = bytes_to_wif(key58.to_bytes(), compressed=True) # Compressed WIF
    keyu58 = Key(wifu58)
    wifu59 = bytes_to_wif(key59.to_bytes(), compressed=False) # Uncompressed WIF
    wifc59 = bytes_to_wif(key59.to_bytes(), compressed=True) # Compressed WIF
    keyu59 = Key(wifu59)
    wifu60 = bytes_to_wif(key60.to_bytes(), compressed=False) # Uncompressed WIF
    wifc60 = bytes_to_wif(key60.to_bytes(), compressed=True) # Compressed WIF
    keyu60 = Key(wifu60)
    wifu61 = bytes_to_wif(key61.to_bytes(), compressed=False) # Uncompressed WIF
    wifc61 = bytes_to_wif(key61.to_bytes(), compressed=True) # Compressed WIF
    keyu61 = Key(wifu61)
    wifu62 = bytes_to_wif(key62.to_bytes(), compressed=False) # Uncompressed WIF
    wifc62 = bytes_to_wif(key62.to_bytes(), compressed=True) # Compressed WIF
    keyu62 = Key(wifu62)
    wifu63 = bytes_to_wif(key63.to_bytes(), compressed=False) # Uncompressed WIF
    wifc63 = bytes_to_wif(key63.to_bytes(), compressed=True) # Compressed WIF
    keyu63 = Key(wifu63)
    wifu64 = bytes_to_wif(key64.to_bytes(), compressed=False) # Uncompressed WIF
    wifc64 = bytes_to_wif(key64.to_bytes(), compressed=True) # Compressed WIF
    keyu64 = Key(wifu64)
    wifu65 = bytes_to_wif(key65.to_bytes(), compressed=False) # Uncompressed WIF
    wifc65 = bytes_to_wif(key65.to_bytes(), compressed=True) # Compressed WIF
    keyu65 = Key(wifu65)
    wifu66 = bytes_to_wif(key66.to_bytes(), compressed=False) # Uncompressed WIF
    wifc66 = bytes_to_wif(key66.to_bytes(), compressed=True) # Compressed WIF
    keyu66 = Key(wifu66)
    wifu67 = bytes_to_wif(key67.to_bytes(), compressed=False) # Uncompressed WIF
    wifc67 = bytes_to_wif(key67.to_bytes(), compressed=True) # Compressed WIF
    keyu67 = Key(wifu67)
    wifu68 = bytes_to_wif(key68.to_bytes(), compressed=False) # Uncompressed WIF
    wifc68 = bytes_to_wif(key68.to_bytes(), compressed=True) # Compressed WIF
    keyu68 = Key(wifu68)
    wifu69 = bytes_to_wif(key69.to_bytes(), compressed=False) # Uncompressed WIF
    wifc69 = bytes_to_wif(key69.to_bytes(), compressed=True) # Compressed WIF
    keyu69 = Key(wifu69)
    wifu70 = bytes_to_wif(key70.to_bytes(), compressed=False) # Uncompressed WIF
    wifc70 = bytes_to_wif(key70.to_bytes(), compressed=True) # Compressed WIF
    keyu70 = Key(wifu70)
    wifu71 = bytes_to_wif(key71.to_bytes(), compressed=False) # Uncompressed WIF
    wifc71 = bytes_to_wif(key71.to_bytes(), compressed=True) # Compressed WIF
    keyu71 = Key(wifu71)
    wifu72 = bytes_to_wif(key72.to_bytes(), compressed=False) # Uncompressed WIF
    wifc72 = bytes_to_wif(key72.to_bytes(), compressed=True) # Compressed WIF
    keyu72 = Key(wifu72)
    wifu73 = bytes_to_wif(key73.to_bytes(), compressed=False) # Uncompressed WIF
    wifc73 = bytes_to_wif(key73.to_bytes(), compressed=True) # Compressed WIF
    keyu73 = Key(wifu73)
    wifu74 = bytes_to_wif(key74.to_bytes(), compressed=False) # Uncompressed WIF
    wifc74 = bytes_to_wif(key74.to_bytes(), compressed=True) # Compressed WIF
    keyu74 = Key(wifu74)
    wifu75 = bytes_to_wif(key75.to_bytes(), compressed=False) # Uncompressed WIF
    wifc75 = bytes_to_wif(key75.to_bytes(), compressed=True) # Compressed WIF
    keyu75 = Key(wifu75)
    wifu76 = bytes_to_wif(key76.to_bytes(), compressed=False) # Uncompressed WIF
    wifc76 = bytes_to_wif(key76.to_bytes(), compressed=True) # Compressed WIF
    keyu76 = Key(wifu76)
    wifu77 = bytes_to_wif(key77.to_bytes(), compressed=False) # Uncompressed WIF
    wifc77 = bytes_to_wif(key77.to_bytes(), compressed=True) # Compressed WIF
    keyu77 = Key(wifu77)
    wifu78 = bytes_to_wif(key78.to_bytes(), compressed=False) # Uncompressed WIF
    wifc78 = bytes_to_wif(key78.to_bytes(), compressed=True) # Compressed WIF
    keyu78 = Key(wifu78)
    wifu79 = bytes_to_wif(key79.to_bytes(), compressed=False) # Uncompressed WIF
    wifc79 = bytes_to_wif(key79.to_bytes(), compressed=True) # Compressed WIF
    keyu79 = Key(wifu79)
    wifu80 = bytes_to_wif(key80.to_bytes(), compressed=False) # Uncompressed WIF
    wifc80 = bytes_to_wif(key80.to_bytes(), compressed=True) # Compressed WIF
    keyu80 = Key(wifu80)
    wifu81 = bytes_to_wif(key81.to_bytes(), compressed=False) # Uncompressed WIF
    wifc81 = bytes_to_wif(key81.to_bytes(), compressed=True) # Compressed WIF
    keyu81 = Key(wifu81)
    wifu82 = bytes_to_wif(key82.to_bytes(), compressed=False) # Uncompressed WIF
    wifc82 = bytes_to_wif(key82.to_bytes(), compressed=True) # Compressed WIF
    keyu82 = Key(wifu82)
    wifu83 = bytes_to_wif(key83.to_bytes(), compressed=False) # Uncompressed WIF
    wifc83 = bytes_to_wif(key83.to_bytes(), compressed=True) # Compressed WIF
    keyu83 = Key(wifu83)
    wifu84 = bytes_to_wif(key84.to_bytes(), compressed=False) # Uncompressed WIF
    wifc84 = bytes_to_wif(key84.to_bytes(), compressed=True) # Compressed WIF
    keyu84 = Key(wifu84)
    wifu85 = bytes_to_wif(key85.to_bytes(), compressed=False) # Uncompressed WIF
    wifc85 = bytes_to_wif(key85.to_bytes(), compressed=True) # Compressed WIF
    keyu85 = Key(wifu85)
    wifu86 = bytes_to_wif(key86.to_bytes(), compressed=False) # Uncompressed WIF
    wifc86 = bytes_to_wif(key86.to_bytes(), compressed=True) # Compressed WIF
    keyu86 = Key(wifu86)
    wifu87 = bytes_to_wif(key87.to_bytes(), compressed=False) # Uncompressed WIF
    wifc87 = bytes_to_wif(key87.to_bytes(), compressed=True) # Compressed WIF
    keyu87 = Key(wifu87)
    wifu88 = bytes_to_wif(key88.to_bytes(), compressed=False) # Uncompressed WIF
    wifc88 = bytes_to_wif(key88.to_bytes(), compressed=True) # Compressed WIF
    keyu88 = Key(wifu88)
    wifu89 = bytes_to_wif(key89.to_bytes(), compressed=False) # Uncompressed WIF
    wifc89 = bytes_to_wif(key89.to_bytes(), compressed=True) # Compressed WIF
    keyu89 = Key(wifu89)
    wifu90 = bytes_to_wif(key90.to_bytes(), compressed=False) # Uncompressed WIF
    wifc90 = bytes_to_wif(key90.to_bytes(), compressed=True) # Compressed WIF
    keyu90 = Key(wifu90)
    wifu91 = bytes_to_wif(key91.to_bytes(), compressed=False) # Uncompressed WIF
    wifc91 = bytes_to_wif(key91.to_bytes(), compressed=True) # Compressed WIF
    keyu91 = Key(wifu91)
    wifu92 = bytes_to_wif(key92.to_bytes(), compressed=False) # Uncompressed WIF
    wifc92 = bytes_to_wif(key92.to_bytes(), compressed=True) # Compressed WIF
    keyu92 = Key(wifu92)
    wifu93 = bytes_to_wif(key93.to_bytes(), compressed=False) # Uncompressed WIF
    wifc93 = bytes_to_wif(key93.to_bytes(), compressed=True) # Compressed WIF
    keyu93 = Key(wifu93)
    wifu94 = bytes_to_wif(key94.to_bytes(), compressed=False) # Uncompressed WIF
    wifc94 = bytes_to_wif(key94.to_bytes(), compressed=True) # Compressed WIF
    keyu94 = Key(wifu94)
    wifu95 = bytes_to_wif(key95.to_bytes(), compressed=False) # Uncompressed WIF
    wifc95 = bytes_to_wif(key95.to_bytes(), compressed=True) # Compressed WIF
    keyu95 = Key(wifu95)
    wifu96 = bytes_to_wif(key96.to_bytes(), compressed=False) # Uncompressed WIF
    wifc96 = bytes_to_wif(key96.to_bytes(), compressed=True) # Compressed WIF
    keyu96 = Key(wifu96)
    wifu97 = bytes_to_wif(key97.to_bytes(), compressed=False) # Uncompressed WIF
    wifc97 = bytes_to_wif(key97.to_bytes(), compressed=True) # Compressed WIF
    keyu97 = Key(wifu97)
    wifu98 = bytes_to_wif(key98.to_bytes(), compressed=False) # Uncompressed WIF
    wifc98 = bytes_to_wif(key98.to_bytes(), compressed=True) # Compressed WIF
    keyu98 = Key(wifu98)
    wifu99 = bytes_to_wif(key99.to_bytes(), compressed=False) # Uncompressed WIF
    wifc99 = bytes_to_wif(key99.to_bytes(), compressed=True) # Compressed WIF
    keyu99 = Key(wifu99)
    wifu100 = bytes_to_wif(key100.to_bytes(), compressed=False) # Uncompressed WIF
    wifc100 = bytes_to_wif(key100.to_bytes(), compressed=True) # Compressed WIF
    keyu100 = Key(wifu100)
    wifu101 = bytes_to_wif(key101.to_bytes(), compressed=False) # Uncompressed WIF
    wifc101 = bytes_to_wif(key101.to_bytes(), compressed=True) # Compressed WIF
    keyu101 = Key(wifu101)
    wifu102 = bytes_to_wif(key102.to_bytes(), compressed=False) # Uncompressed WIF
    wifc102 = bytes_to_wif(key102.to_bytes(), compressed=True) # Compressed WIF
    keyu102 = Key(wifu102)
    wifu103 = bytes_to_wif(key103.to_bytes(), compressed=False) # Uncompressed WIF
    wifc103 = bytes_to_wif(key103.to_bytes(), compressed=True) # Compressed WIF
    keyu103 = Key(wifu103)
    wifu104 = bytes_to_wif(key104.to_bytes(), compressed=False) # Uncompressed WIF
    wifc104 = bytes_to_wif(key104.to_bytes(), compressed=True) # Compressed WIF
    keyu104 = Key(wifu104)
    wifu105 = bytes_to_wif(key105.to_bytes(), compressed=False) # Uncompressed WIF
    wifc105 = bytes_to_wif(key105.to_bytes(), compressed=True) # Compressed WIF
    keyu105 = Key(wifu105)
    wifu106 = bytes_to_wif(key106.to_bytes(), compressed=False) # Uncompressed WIF
    wifc106 = bytes_to_wif(key106.to_bytes(), compressed=True) # Compressed WIF
    keyu106 = Key(wifu106)
    wifu107 = bytes_to_wif(key107.to_bytes(), compressed=False) # Uncompressed WIF
    wifc107 = bytes_to_wif(key107.to_bytes(), compressed=True) # Compressed WIF
    keyu107 = Key(wifu107)
    wifu108 = bytes_to_wif(key108.to_bytes(), compressed=False) # Uncompressed WIF
    wifc108 = bytes_to_wif(key108.to_bytes(), compressed=True) # Compressed WIF
    keyu108 = Key(wifu108)
    wifu109 = bytes_to_wif(key109.to_bytes(), compressed=False) # Uncompressed WIF
    wifc109 = bytes_to_wif(key109.to_bytes(), compressed=True) # Compressed WIF
    keyu109 = Key(wifu109)
    wifu110 = bytes_to_wif(key110.to_bytes(), compressed=False) # Uncompressed WIF
    wifc110 = bytes_to_wif(key110.to_bytes(), compressed=True) # Compressed WIF
    keyu110 = Key(wifu110)
    wifu111 = bytes_to_wif(key111.to_bytes(), compressed=False) # Uncompressed WIF
    wifc111 = bytes_to_wif(key111.to_bytes(), compressed=True) # Compressed WIF
    keyu111 = Key(wifu111)
    wifu112 = bytes_to_wif(key112.to_bytes(), compressed=False) # Uncompressed WIF
    wifc112 = bytes_to_wif(key112.to_bytes(), compressed=True) # Compressed WIF
    keyu112 = Key(wifu112)
    wifu113 = bytes_to_wif(key113.to_bytes(), compressed=False) # Uncompressed WIF
    wifc113 = bytes_to_wif(key113.to_bytes(), compressed=True) # Compressed WIF
    keyu113 = Key(wifu113)
    wifu114 = bytes_to_wif(key114.to_bytes(), compressed=False) # Uncompressed WIF
    wifc114 = bytes_to_wif(key114.to_bytes(), compressed=True) # Compressed WIF
    keyu114 = Key(wifu114)
    wifu115 = bytes_to_wif(key115.to_bytes(), compressed=False) # Uncompressed WIF
    wifc115 = bytes_to_wif(key115.to_bytes(), compressed=True) # Compressed WIF
    keyu115 = Key(wifu115)
    wifu116 = bytes_to_wif(key116.to_bytes(), compressed=False) # Uncompressed WIF
    wifc116 = bytes_to_wif(key116.to_bytes(), compressed=True) # Compressed WIF
    keyu116 = Key(wifu116)
    wifu117 = bytes_to_wif(key117.to_bytes(), compressed=False) # Uncompressed WIF
    wifc117 = bytes_to_wif(key117.to_bytes(), compressed=True) # Compressed WIF
    keyu117 = Key(wifu117)
    wifu118 = bytes_to_wif(key118.to_bytes(), compressed=False) # Uncompressed WIF
    wifc118 = bytes_to_wif(key118.to_bytes(), compressed=True) # Compressed WIF
    keyu118 = Key(wifu118)
    wifu119 = bytes_to_wif(key119.to_bytes(), compressed=False) # Uncompressed WIF
    wifc119 = bytes_to_wif(key119.to_bytes(), compressed=True) # Compressed WIF
    keyu119 = Key(wifu119)
    wifu120 = bytes_to_wif(key120.to_bytes(), compressed=False) # Uncompressed WIF
    wifc120 = bytes_to_wif(key120.to_bytes(), compressed=True) # Compressed WIF
    keyu120 = Key(wifu120)
    wifu121 = bytes_to_wif(key121.to_bytes(), compressed=False) # Uncompressed WIF
    wifc121 = bytes_to_wif(key121.to_bytes(), compressed=True) # Compressed WIF
    keyu121 = Key(wifu121)
    wifu122 = bytes_to_wif(key122.to_bytes(), compressed=False) # Uncompressed WIF
    wifc122 = bytes_to_wif(key122.to_bytes(), compressed=True) # Compressed WIF
    keyu122 = Key(wifu122)
    wifu123 = bytes_to_wif(key123.to_bytes(), compressed=False) # Uncompressed WIF
    wifc123 = bytes_to_wif(key123.to_bytes(), compressed=True) # Compressed WIF
    keyu123 = Key(wifu123)
    wifu124 = bytes_to_wif(key124.to_bytes(), compressed=False) # Uncompressed WIF
    wifc124 = bytes_to_wif(key124.to_bytes(), compressed=True) # Compressed WIF
    keyu124 = Key(wifu124)
    wifu125 = bytes_to_wif(key125.to_bytes(), compressed=False) # Uncompressed WIF
    wifc125 = bytes_to_wif(key125.to_bytes(), compressed=True) # Compressed WIF
    keyu125 = Key(wifu125)
    wifu126 = bytes_to_wif(key126.to_bytes(), compressed=False) # Uncompressed WIF
    wifc126 = bytes_to_wif(key126.to_bytes(), compressed=True) # Compressed WIF
    keyu126 = Key(wifu126)
    wifu127 = bytes_to_wif(key127.to_bytes(), compressed=False) # Uncompressed WIF
    wifc127 = bytes_to_wif(key127.to_bytes(), compressed=True) # Compressed WIF
    keyu127 = Key(wifu127)
    

    caddr = key.address
    caddr1 = key1.address
    caddr2 = key2.address
    caddr3 = key3.address
    caddr4 = key4.address
    caddr5 = key5.address
    caddr6 = key6.address
    caddr7 = key7.address
    caddr8 = key8.address
    caddr9 = key9.address
    caddr10 = key10.address
    caddr11 = key11.address
    caddr12 = key12.address
    caddr13 = key13.address
    caddr14 = key14.address
    caddr15 = key15.address
    caddr16 = key16.address
    caddr17 = key17.address
    caddr18 = key18.address
    caddr19 = key19.address
    caddr20 = key20.address
    caddr21 = key21.address
    caddr22 = key22.address
    caddr23 = key23.address
    caddr24 = key24.address
    caddr25 = key25.address
    caddr26 = key26.address
    caddr27 = key27.address
    caddr28 = key28.address
    caddr29 = key29.address
    caddr30 = key30.address
    caddr31 = key31.address
    caddr32 = key32.address
    caddr33 = key33.address
    caddr34 = key34.address
    caddr35 = key35.address
    caddr36 = key36.address
    caddr37 = key37.address
    caddr38 = key38.address
    caddr39 = key39.address
    caddr40 = key40.address
    caddr41 = key41.address
    caddr42 = key42.address
    caddr43 = key43.address
    caddr44 = key44.address
    caddr45 = key45.address
    caddr46 = key46.address
    caddr47 = key47.address
    caddr48 = key48.address
    caddr49 = key49.address
    caddr50 = key50.address
    caddr51 = key51.address
    caddr52 = key52.address
    caddr53 = key53.address
    caddr54 = key54.address
    caddr55 = key55.address
    caddr56 = key56.address
    caddr57 = key57.address
    caddr58 = key58.address
    caddr59 = key59.address
    caddr60 = key60.address
    caddr61 = key61.address
    caddr62 = key62.address
    caddr63 = key63.address
    caddr64 = key64.address
    caddr65 = key65.address
    caddr66 = key66.address
    caddr67 = key67.address
    caddr68 = key68.address
    caddr69 = key69.address
    caddr70 = key70.address
    caddr71 = key71.address
    caddr72 = key72.address
    caddr73 = key73.address
    caddr74 = key74.address
    caddr75 = key75.address
    caddr76 = key76.address
    caddr77 = key77.address
    caddr78 = key78.address
    caddr79 = key79.address
    caddr80 = key80.address
    caddr81 = key81.address
    caddr82 = key82.address
    caddr83 = key83.address
    caddr84 = key84.address
    caddr85 = key85.address
    caddr86 = key86.address
    caddr87 = key87.address
    caddr88 = key88.address
    caddr89 = key89.address
    caddr90 = key90.address
    caddr91 = key91.address
    caddr92 = key92.address
    caddr93 = key93.address
    caddr94 = key94.address
    caddr95 = key95.address
    caddr96 = key96.address
    caddr97 = key97.address
    caddr98 = key98.address
    caddr99 = key99.address
    caddr100 = key100.address
    caddr101 = key101.address
    caddr102 = key102.address
    caddr103 = key103.address
    caddr104 = key104.address
    caddr105 = key105.address
    caddr106 = key106.address
    caddr107 = key107.address
    caddr108 = key108.address
    caddr109 = key109.address
    caddr110 = key110.address
    caddr111 = key111.address
    caddr112 = key112.address
    caddr113 = key113.address
    caddr114 = key114.address
    caddr115 = key115.address
    caddr116 = key116.address
    caddr117 = key117.address
    caddr118 = key118.address
    caddr119 = key119.address
    caddr120 = key120.address
    caddr121 = key121.address
    caddr122 = key122.address
    caddr123 = key123.address
    caddr124 = key124.address
    caddr125 = key125.address
    caddr126 = key126.address
    caddr127 = key127.address
    
    uaddr = keyu.address
    uaddr1 = keyu1.address
    uaddr2 = keyu2.address
    uaddr3 = keyu3.address
    uaddr4 = keyu4.address
    uaddr5 = keyu5.address
    uaddr6 = keyu6.address
    uaddr7 = keyu7.address
    uaddr8 = keyu8.address
    uaddr9 = keyu9.address
    uaddr10 = keyu10.address
    uaddr11 = keyu11.address
    uaddr12 = keyu12.address
    uaddr13 = keyu13.address
    uaddr14 = keyu14.address
    uaddr15 = keyu15.address
    uaddr16 = keyu16.address
    uaddr17 = keyu17.address
    uaddr18 = keyu18.address
    uaddr19 = keyu19.address
    uaddr20 = keyu20.address
    uaddr21 = keyu21.address
    uaddr22 = keyu22.address
    uaddr23 = keyu23.address
    uaddr24 = keyu24.address
    uaddr25 = keyu25.address
    uaddr26 = keyu26.address
    uaddr27 = keyu27.address
    uaddr28 = keyu28.address
    uaddr29 = keyu29.address
    uaddr30 = keyu30.address
    uaddr31 = keyu31.address
    uaddr32 = keyu32.address
    uaddr33 = keyu33.address
    uaddr34 = keyu34.address
    uaddr35 = keyu35.address
    uaddr36 = keyu36.address
    uaddr37 = keyu37.address
    uaddr38 = keyu38.address
    uaddr39 = keyu39.address
    uaddr40 = keyu40.address
    uaddr41 = keyu41.address
    uaddr42 = keyu42.address
    uaddr43 = keyu43.address
    uaddr44 = keyu44.address
    uaddr45 = keyu45.address
    uaddr46 = keyu46.address
    uaddr47 = keyu47.address
    uaddr48 = keyu48.address
    uaddr49 = keyu49.address
    uaddr50 = keyu50.address
    uaddr51 = keyu51.address
    uaddr52 = keyu52.address
    uaddr53 = keyu53.address
    uaddr54 = keyu54.address
    uaddr55 = keyu55.address
    uaddr56 = keyu56.address
    uaddr57 = keyu57.address
    uaddr58 = keyu58.address
    uaddr59 = keyu59.address
    uaddr60 = keyu60.address
    uaddr61 = keyu61.address
    uaddr62 = keyu62.address
    uaddr63 = keyu63.address
    uaddr64 = keyu64.address
    uaddr65 = keyu65.address
    uaddr66 = keyu66.address
    uaddr67 = keyu67.address
    uaddr68 = keyu68.address
    uaddr69 = keyu69.address
    uaddr70 = keyu70.address
    uaddr71 = keyu71.address
    uaddr72 = keyu72.address
    uaddr73 = keyu73.address
    uaddr74 = keyu74.address
    uaddr75 = keyu75.address
    uaddr76 = keyu76.address
    uaddr77 = keyu77.address
    uaddr78 = keyu78.address
    uaddr79 = keyu79.address
    uaddr80 = keyu80.address
    uaddr81 = keyu81.address
    uaddr82 = keyu82.address
    uaddr83 = keyu83.address
    uaddr84 = keyu84.address
    uaddr85 = keyu85.address
    uaddr86 = keyu86.address
    uaddr87 = keyu87.address
    uaddr88 = keyu88.address
    uaddr89 = keyu89.address
    uaddr90 = keyu90.address
    uaddr91 = keyu91.address
    uaddr92 = keyu92.address
    uaddr93 = keyu93.address
    uaddr94 = keyu94.address
    uaddr95 = keyu95.address
    uaddr96 = keyu96.address
    uaddr97 = keyu97.address
    uaddr98 = keyu98.address
    uaddr99 = keyu99.address
    uaddr100 = keyu100.address
    uaddr101 = keyu101.address
    uaddr102 = keyu102.address
    uaddr103 = keyu103.address
    uaddr104 = keyu104.address
    uaddr105 = keyu105.address
    uaddr106 = keyu106.address
    uaddr107 = keyu107.address
    uaddr108 = keyu108.address
    uaddr109 = keyu109.address
    uaddr110 = keyu110.address
    uaddr111 = keyu111.address
    uaddr112 = keyu112.address
    uaddr113 = keyu113.address
    uaddr114 = keyu114.address
    uaddr115 = keyu115.address
    uaddr116 = keyu116.address
    uaddr117 = keyu117.address
    uaddr118 = keyu118.address
    uaddr119 = keyu119.address
    uaddr120 = keyu120.address
    uaddr121 = keyu121.address
    uaddr122 = keyu122.address
    uaddr123 = keyu123.address
    uaddr124 = keyu124.address
    uaddr125 = keyu125.address
    uaddr126 = keyu126.address
    uaddr127 = keyu127.address
    count+=1
    total+=256
    print ('Scan= ', count, 'Total= ',total, key.to_hex(), end='\r')
    if caddr in add or uaddr in add:
        print ('Matching Key ==== Found!!!\n PrivateKey DEC: ',seed, '\nMatching Key ==== Found!!!\n PrivateKey HEX: ', key.to_hex(), '\nBitcoin Address Compressed : ', caddr, '\nBitcoin Address UnCompressed :', uaddr, '\nPrivateKey (wif) Compressed : ', wifc, '\nPrivateKey (wif) UnCompressed : ', wifu)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr)
        f.write('\nBitcoin Address UnCompressed :' + uaddr)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu)
        f.close()
    if caddr1 in add or uaddr1 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key1.to_hex(), '\nBitcoin Address Compressed : ', caddr1, '\nBitcoin Address UnCompressed :', uaddr1, '\nPrivateKey (wif) Compressed : ', wifc1, '\nPrivateKey (wif) UnCompressed : ', wifu1)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key1.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr1)
        f.write('\nBitcoin Address UnCompressed :' + uaddr1)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc1)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu1)
        f.close() 
    if caddr2 in add or uaddr2 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key2.to_hex(), '\nBitcoin Address Compressed : ', caddr2, '\nBitcoin Address UnCompressed :', uaddr2, '\nPrivateKey (wif) Compressed : ', wifc2, '\nPrivateKey (wif) UnCompressed : ', wifu2)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key2.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr2)
        f.write('\nBitcoin Address UnCompressed :' + uaddr2)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc2)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu2)
        f.close()         
    if caddr3 in add or uaddr3 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key3.to_hex(), '\nBitcoin Address Compressed : ', caddr3, '\nBitcoin Address UnCompressed :', uaddr3, '\nPrivateKey (wif) Compressed : ', wifc3, '\nPrivateKey (wif) UnCompressed : ', wifu3)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key3.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr3)
        f.write('\nBitcoin Address UnCompressed :' + uaddr3)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc3)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu3)
        f.close()    
    if caddr4 in add or uaddr4 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key4.to_hex(), '\nBitcoin Address Compressed : ', caddr4, '\nBitcoin Address UnCompressed :', uaddr4, '\nPrivateKey (wif) Compressed : ', wifc4, '\nPrivateKey (wif) UnCompressed : ', wifu4)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key4.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr4)
        f.write('\nBitcoin Address UnCompressed :' + uaddr4)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc4)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu4)
        f.close() 
    if caddr5 in add or uaddr5 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key5.to_hex(), '\nBitcoin Address Compressed : ', caddr5, '\nBitcoin Address UnCompressed :', uaddr5, '\nPrivateKey (wif) Compressed : ', wifc5, '\nPrivateKey (wif) UnCompressed : ', wifu5)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key5.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr5)
        f.write('\nBitcoin Address UnCompressed :' + uaddr5)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc5)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu5)
        f.close() 
    if caddr6 in add or uaddr6 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key6.to_hex(), '\nBitcoin Address Compressed : ', caddr6, '\nBitcoin Address UnCompressed :', uaddr6, '\nPrivateKey (wif) Compressed : ', wifc6, '\nPrivateKey (wif) UnCompressed : ', wifu6)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key6.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr6)
        f.write('\nBitcoin Address UnCompressed :' + uaddr6)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc6)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu6)
        f.close() 
    if caddr7 in add or uaddr7 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key7.to_hex(), '\nBitcoin Address Compressed : ', caddr7, '\nBitcoin Address UnCompressed :', uaddr7, '\nPrivateKey (wif) Compressed : ', wifc7, '\nPrivateKey (wif) UnCompressed : ', wifu7)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key7.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr7)
        f.write('\nBitcoin Address UnCompressed :' + uaddr7)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc7)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu7)
        f.close() 
    if caddr8 in add or uaddr8 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key8.to_hex(), '\nBitcoin Address Compressed : ', caddr8, '\nBitcoin Address UnCompressed :', uaddr8, '\nPrivateKey (wif) Compressed : ', wifc8, '\nPrivateKey (wif) UnCompressed : ', wifu8)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key8.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr8)
        f.write('\nBitcoin Address UnCompressed :' + uaddr8)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc8)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu8)
        f.close() 
    if caddr9 in add or uaddr9 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key9.to_hex(), '\nBitcoin Address Compressed : ', caddr9, '\nBitcoin Address UnCompressed :', uaddr9, '\nPrivateKey (wif) Compressed : ', wifc9, '\nPrivateKey (wif) UnCompressed : ', wifu9)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key9.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr9)
        f.write('\nBitcoin Address UnCompressed :' + uaddr9)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc9)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu9)
        f.close() 
    if caddr10 in add or uaddr10 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key10.to_hex(), '\nBitcoin Address Compressed : ', caddr10, '\nBitcoin Address UnCompressed :', uaddr10, '\nPrivateKey (wif) Compressed : ', wifc10, '\nPrivateKey (wif) UnCompressed : ', wifu10)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key10.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr10)
        f.write('\nBitcoin Address UnCompressed :' + uaddr10)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc10)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu10)
        f.close() 
    if caddr11 in add or uaddr11 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key11.to_hex(), '\nBitcoin Address Compressed : ', caddr11, '\nBitcoin Address UnCompressed :', uaddr11, '\nPrivateKey (wif) Compressed : ', wifc11, '\nPrivateKey (wif) UnCompressed : ', wifu11)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key11.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr11)
        f.write('\nBitcoin Address UnCompressed :' + uaddr11)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc11)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu11)
        f.close() 
    if caddr12 in add or uaddr12 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key12.to_hex(), '\nBitcoin Address Compressed : ', caddr12, '\nBitcoin Address UnCompressed :', uaddr12, '\nPrivateKey (wif) Compressed : ', wifc12, '\nPrivateKey (wif) UnCompressed : ', wifu12)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key12.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr12)
        f.write('\nBitcoin Address UnCompressed :' + uaddr12)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc12)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu12)
        f.close() 
    if caddr13 in add or uaddr13 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key13.to_hex(), '\nBitcoin Address Compressed : ', caddr13, '\nBitcoin Address UnCompressed :', uaddr13, '\nPrivateKey (wif) Compressed : ', wifc13, '\nPrivateKey (wif) UnCompressed : ', wifu13)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key13.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr13)
        f.write('\nBitcoin Address UnCompressed :' + uaddr13)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc13)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu13)
        f.close() 
    if caddr14 in add or uaddr14 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key14.to_hex(), '\nBitcoin Address Compressed : ', caddr14, '\nBitcoin Address UnCompressed :', uaddr14, '\nPrivateKey (wif) Compressed : ', wifc14, '\nPrivateKey (wif) UnCompressed : ', wifu14)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key14.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr14)
        f.write('\nBitcoin Address UnCompressed :' + uaddr14)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc14)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu14)
        f.close() 
    if caddr15 in add or uaddr15 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key15.to_hex(), '\nBitcoin Address Compressed : ', caddr15, '\nBitcoin Address UnCompressed :', uaddr15, '\nPrivateKey (wif) Compressed : ', wifc15, '\nPrivateKey (wif) UnCompressed : ', wifu15)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key15.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr15)
        f.write('\nBitcoin Address UnCompressed :' + uaddr15)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc15)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu15)
        f.close() 
    if caddr16 in add or uaddr16 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key16.to_hex(), '\nBitcoin Address Compressed : ', caddr16, '\nBitcoin Address UnCompressed :', uaddr16, '\nPrivateKey (wif) Compressed : ', wifc16, '\nPrivateKey (wif) UnCompressed : ', wifu16)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key16.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr16)
        f.write('\nBitcoin Address UnCompressed :' + uaddr16)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc16)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu16)
        f.close() 
    if caddr17 in add or uaddr17 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key17.to_hex(), '\nBitcoin Address Compressed : ', caddr17, '\nBitcoin Address UnCompressed :', uaddr17, '\nPrivateKey (wif) Compressed : ', wifc17, '\nPrivateKey (wif) UnCompressed : ', wifu17)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key17.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr17)
        f.write('\nBitcoin Address UnCompressed :' + uaddr17)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc17)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu17)
        f.close() 
    if caddr18 in add or uaddr18 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key18.to_hex(), '\nBitcoin Address Compressed : ', caddr18, '\nBitcoin Address UnCompressed :', uaddr18, '\nPrivateKey (wif) Compressed : ', wifc18, '\nPrivateKey (wif) UnCompressed : ', wifu18)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key18.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr18)
        f.write('\nBitcoin Address UnCompressed :' + uaddr18)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc18)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu18)
        f.close() 
    if caddr19 in add or uaddr19 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key19.to_hex(), '\nBitcoin Address Compressed : ', caddr19, '\nBitcoin Address UnCompressed :', uaddr19, '\nPrivateKey (wif) Compressed : ', wifc19, '\nPrivateKey (wif) UnCompressed : ', wifu19)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key19.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr19)
        f.write('\nBitcoin Address UnCompressed :' + uaddr19)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc19)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu19)
        f.close() 
    if caddr20 in add or uaddr20 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key20.to_hex(), '\nBitcoin Address Compressed : ', caddr20, '\nBitcoin Address UnCompressed :', uaddr20, '\nPrivateKey (wif) Compressed : ', wifc20, '\nPrivateKey (wif) UnCompressed : ', wifu20)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key20.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr20)
        f.write('\nBitcoin Address UnCompressed :' + uaddr20)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc20)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu20)
        f.close() 
    if caddr21 in add or uaddr21 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key21.to_hex(), '\nBitcoin Address Compressed : ', caddr21, '\nBitcoin Address UnCompressed :', uaddr21, '\nPrivateKey (wif) Compressed : ', wifc21, '\nPrivateKey (wif) UnCompressed : ', wifu21)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key21.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr21)
        f.write('\nBitcoin Address UnCompressed :' + uaddr21)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc21)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu21)
        f.close() 
    if caddr22 in add or uaddr22 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key22.to_hex(), '\nBitcoin Address Compressed : ', caddr22, '\nBitcoin Address UnCompressed :', uaddr22, '\nPrivateKey (wif) Compressed : ', wifc22, '\nPrivateKey (wif) UnCompressed : ', wifu22)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key22.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr22)
        f.write('\nBitcoin Address UnCompressed :' + uaddr22)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc22)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu22)
        f.close() 
    if caddr23 in add or uaddr23 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key23.to_hex(), '\nBitcoin Address Compressed : ', caddr23, '\nBitcoin Address UnCompressed :', uaddr23, '\nPrivateKey (wif) Compressed : ', wifc23, '\nPrivateKey (wif) UnCompressed : ', wifu23)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key23.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr23)
        f.write('\nBitcoin Address UnCompressed :' + uaddr23)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc23)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu23)
        f.close() 
    if caddr24 in add or uaddr24 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key24.to_hex(), '\nBitcoin Address Compressed : ', caddr24, '\nBitcoin Address UnCompressed :', uaddr24, '\nPrivateKey (wif) Compressed : ', wifc24, '\nPrivateKey (wif) UnCompressed : ', wifu24)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key24.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr24)
        f.write('\nBitcoin Address UnCompressed :' + uaddr24)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc24)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu24)
        f.close() 
    if caddr25 in add or uaddr25 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key25.to_hex(), '\nBitcoin Address Compressed : ', caddr25, '\nBitcoin Address UnCompressed :', uaddr25, '\nPrivateKey (wif) Compressed : ', wifc25, '\nPrivateKey (wif) UnCompressed : ', wifu25)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key25.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr25)
        f.write('\nBitcoin Address UnCompressed :' + uaddr25)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc25)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu25)
        f.close() 
    if caddr26 in add or uaddr26 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key26.to_hex(), '\nBitcoin Address Compressed : ', caddr26, '\nBitcoin Address UnCompressed :', uaddr26, '\nPrivateKey (wif) Compressed : ', wifc26, '\nPrivateKey (wif) UnCompressed : ', wifu26)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key26.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr26)
        f.write('\nBitcoin Address UnCompressed :' + uaddr26)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc26)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu26)
        f.close() 
    if caddr27 in add or uaddr27 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key27.to_hex(), '\nBitcoin Address Compressed : ', caddr27, '\nBitcoin Address UnCompressed :', uaddr27, '\nPrivateKey (wif) Compressed : ', wifc27, '\nPrivateKey (wif) UnCompressed : ', wifu27)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key27.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr27)
        f.write('\nBitcoin Address UnCompressed :' + uaddr27)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc27)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu27)
        f.close() 
    if caddr28 in add or uaddr28 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key28.to_hex(), '\nBitcoin Address Compressed : ', caddr28, '\nBitcoin Address UnCompressed :', uaddr28, '\nPrivateKey (wif) Compressed : ', wifc28, '\nPrivateKey (wif) UnCompressed : ', wifu28)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key28.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr28)
        f.write('\nBitcoin Address UnCompressed :' + uaddr28)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc28)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu28)
        f.close() 
    if caddr29 in add or uaddr29 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key29.to_hex(), '\nBitcoin Address Compressed : ', caddr29, '\nBitcoin Address UnCompressed :', uaddr29, '\nPrivateKey (wif) Compressed : ', wifc29, '\nPrivateKey (wif) UnCompressed : ', wifu29)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key29.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr29)
        f.write('\nBitcoin Address UnCompressed :' + uaddr29)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc29)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu29)
        f.close() 
    if caddr30 in add or uaddr30 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key30.to_hex(), '\nBitcoin Address Compressed : ', caddr30, '\nBitcoin Address UnCompressed :', uaddr30, '\nPrivateKey (wif) Compressed : ', wifc30, '\nPrivateKey (wif) UnCompressed : ', wifu30)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key30.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr30)
        f.write('\nBitcoin Address UnCompressed :' + uaddr30)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc30)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu30)
        f.close() 
    if caddr31 in add or uaddr31 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key31.to_hex(), '\nBitcoin Address Compressed : ', caddr31, '\nBitcoin Address UnCompressed :', uaddr31, '\nPrivateKey (wif) Compressed : ', wifc31, '\nPrivateKey (wif) UnCompressed : ', wifu31)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key31.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr31)
        f.write('\nBitcoin Address UnCompressed :' + uaddr31)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc31)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu31)
        f.close() 
    if caddr32 in add or uaddr32 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key32.to_hex(), '\nBitcoin Address Compressed : ', caddr32, '\nBitcoin Address UnCompressed :', uaddr32, '\nPrivateKey (wif) Compressed : ', wifc32, '\nPrivateKey (wif) UnCompressed : ', wifu32)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key32.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr32)
        f.write('\nBitcoin Address UnCompressed :' + uaddr32)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc32)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu32)
        f.close() 
    if caddr33 in add or uaddr33 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key33.to_hex(), '\nBitcoin Address Compressed : ', caddr33, '\nBitcoin Address UnCompressed :', uaddr33, '\nPrivateKey (wif) Compressed : ', wifc33, '\nPrivateKey (wif) UnCompressed : ', wifu33)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key33.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr33)
        f.write('\nBitcoin Address UnCompressed :' + uaddr33)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc33)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu33)
        f.close() 
    if caddr34 in add or uaddr34 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key34.to_hex(), '\nBitcoin Address Compressed : ', caddr34, '\nBitcoin Address UnCompressed :', uaddr34, '\nPrivateKey (wif) Compressed : ', wifc34, '\nPrivateKey (wif) UnCompressed : ', wifu34)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key34.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr34)
        f.write('\nBitcoin Address UnCompressed :' + uaddr34)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc34)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu34)
        f.close() 
    if caddr35 in add or uaddr35 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key35.to_hex(), '\nBitcoin Address Compressed : ', caddr35, '\nBitcoin Address UnCompressed :', uaddr35, '\nPrivateKey (wif) Compressed : ', wifc35, '\nPrivateKey (wif) UnCompressed : ', wifu35)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key35.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr35)
        f.write('\nBitcoin Address UnCompressed :' + uaddr35)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc35)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu35)
        f.close() 
    if caddr36 in add or uaddr36 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key36.to_hex(), '\nBitcoin Address Compressed : ', caddr36, '\nBitcoin Address UnCompressed :', uaddr36, '\nPrivateKey (wif) Compressed : ', wifc36, '\nPrivateKey (wif) UnCompressed : ', wifu36)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key36.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr36)
        f.write('\nBitcoin Address UnCompressed :' + uaddr36)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc36)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu36)
        f.close() 
    if caddr37 in add or uaddr37 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key37.to_hex(), '\nBitcoin Address Compressed : ', caddr37, '\nBitcoin Address UnCompressed :', uaddr37, '\nPrivateKey (wif) Compressed : ', wifc37, '\nPrivateKey (wif) UnCompressed : ', wifu37)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key37.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr37)
        f.write('\nBitcoin Address UnCompressed :' + uaddr37)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc37)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu37)
        f.close() 
    if caddr38 in add or uaddr38 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key38.to_hex(), '\nBitcoin Address Compressed : ', caddr38, '\nBitcoin Address UnCompressed :', uaddr38, '\nPrivateKey (wif) Compressed : ', wifc38, '\nPrivateKey (wif) UnCompressed : ', wifu38)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key38.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr38)
        f.write('\nBitcoin Address UnCompressed :' + uaddr38)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc38)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu38)
        f.close() 
    if caddr39 in add or uaddr39 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key39.to_hex(), '\nBitcoin Address Compressed : ', caddr39, '\nBitcoin Address UnCompressed :', uaddr39, '\nPrivateKey (wif) Compressed : ', wifc39, '\nPrivateKey (wif) UnCompressed : ', wifu39)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key39.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr39)
        f.write('\nBitcoin Address UnCompressed :' + uaddr39)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc39)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu39)
        f.close() 
    if caddr40 in add or uaddr40 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key40.to_hex(), '\nBitcoin Address Compressed : ', caddr40, '\nBitcoin Address UnCompressed :', uaddr40, '\nPrivateKey (wif) Compressed : ', wifc40, '\nPrivateKey (wif) UnCompressed : ', wifu40)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key40.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr40)
        f.write('\nBitcoin Address UnCompressed :' + uaddr40)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc40)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu40)
        f.close() 
    if caddr41 in add or uaddr41 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key41.to_hex(), '\nBitcoin Address Compressed : ', caddr41, '\nBitcoin Address UnCompressed :', uaddr41, '\nPrivateKey (wif) Compressed : ', wifc41, '\nPrivateKey (wif) UnCompressed : ', wifu41)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key41.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr41)
        f.write('\nBitcoin Address UnCompressed :' + uaddr41)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc41)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu41)
        f.close() 
    if caddr42 in add or uaddr42 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key42.to_hex(), '\nBitcoin Address Compressed : ', caddr42, '\nBitcoin Address UnCompressed :', uaddr42, '\nPrivateKey (wif) Compressed : ', wifc42, '\nPrivateKey (wif) UnCompressed : ', wifu42)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key42.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr42)
        f.write('\nBitcoin Address UnCompressed :' + uaddr42)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc42)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu42)
        f.close() 
    if caddr43 in add or uaddr43 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key43.to_hex(), '\nBitcoin Address Compressed : ', caddr43, '\nBitcoin Address UnCompressed :', uaddr43, '\nPrivateKey (wif) Compressed : ', wifc43, '\nPrivateKey (wif) UnCompressed : ', wifu43)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key43.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr43)
        f.write('\nBitcoin Address UnCompressed :' + uaddr43)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc43)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu43)
        f.close() 
    if caddr44 in add or uaddr44 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key44.to_hex(), '\nBitcoin Address Compressed : ', caddr44, '\nBitcoin Address UnCompressed :', uaddr44, '\nPrivateKey (wif) Compressed : ', wifc44, '\nPrivateKey (wif) UnCompressed : ', wifu44)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key44.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr44)
        f.write('\nBitcoin Address UnCompressed :' + uaddr44)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc44)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu44)
        f.close() 
    if caddr45 in add or uaddr45 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key45.to_hex(), '\nBitcoin Address Compressed : ', caddr45, '\nBitcoin Address UnCompressed :', uaddr45, '\nPrivateKey (wif) Compressed : ', wifc45, '\nPrivateKey (wif) UnCompressed : ', wifu45)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key45.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr45)
        f.write('\nBitcoin Address UnCompressed :' + uaddr45)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc45)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu45)
        f.close() 
    if caddr46 in add or uaddr46 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key46.to_hex(), '\nBitcoin Address Compressed : ', caddr46, '\nBitcoin Address UnCompressed :', uaddr46, '\nPrivateKey (wif) Compressed : ', wifc46, '\nPrivateKey (wif) UnCompressed : ', wifu46)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key46.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr46)
        f.write('\nBitcoin Address UnCompressed :' + uaddr46)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc46)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu46)
        f.close() 
    if caddr47 in add or uaddr47 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key47.to_hex(), '\nBitcoin Address Compressed : ', caddr47, '\nBitcoin Address UnCompressed :', uaddr47, '\nPrivateKey (wif) Compressed : ', wifc47, '\nPrivateKey (wif) UnCompressed : ', wifu47)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key47.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr47)
        f.write('\nBitcoin Address UnCompressed :' + uaddr47)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc47)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu47)
        f.close() 
    if caddr48 in add or uaddr48 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key48.to_hex(), '\nBitcoin Address Compressed : ', caddr48, '\nBitcoin Address UnCompressed :', uaddr48, '\nPrivateKey (wif) Compressed : ', wifc48, '\nPrivateKey (wif) UnCompressed : ', wifu48)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key48.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr48)
        f.write('\nBitcoin Address UnCompressed :' + uaddr48)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc48)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu48)
        f.close() 
    if caddr49 in add or uaddr49 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key49.to_hex(), '\nBitcoin Address Compressed : ', caddr49, '\nBitcoin Address UnCompressed :', uaddr49, '\nPrivateKey (wif) Compressed : ', wifc49, '\nPrivateKey (wif) UnCompressed : ', wifu49)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key49.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr49)
        f.write('\nBitcoin Address UnCompressed :' + uaddr49)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc49)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu49)
        f.close() 
    if caddr50 in add or uaddr50 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key50.to_hex(), '\nBitcoin Address Compressed : ', caddr50, '\nBitcoin Address UnCompressed :', uaddr50, '\nPrivateKey (wif) Compressed : ', wifc50, '\nPrivateKey (wif) UnCompressed : ', wifu50)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key50.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr50)
        f.write('\nBitcoin Address UnCompressed :' + uaddr50)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc50)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu50)
        f.close() 
    if caddr51 in add or uaddr51 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key51.to_hex(), '\nBitcoin Address Compressed : ', caddr51, '\nBitcoin Address UnCompressed :', uaddr51, '\nPrivateKey (wif) Compressed : ', wifc51, '\nPrivateKey (wif) UnCompressed : ', wifu51)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key51.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr51)
        f.write('\nBitcoin Address UnCompressed :' + uaddr51)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc51)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu51)
        f.close() 
    if caddr52 in add or uaddr52 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key52.to_hex(), '\nBitcoin Address Compressed : ', caddr52, '\nBitcoin Address UnCompressed :', uaddr52, '\nPrivateKey (wif) Compressed : ', wifc52, '\nPrivateKey (wif) UnCompressed : ', wifu52)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key52.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr52)
        f.write('\nBitcoin Address UnCompressed :' + uaddr52)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc52)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu52)
        f.close() 
    if caddr53 in add or uaddr53 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key53.to_hex(), '\nBitcoin Address Compressed : ', caddr53, '\nBitcoin Address UnCompressed :', uaddr53, '\nPrivateKey (wif) Compressed : ', wifc53, '\nPrivateKey (wif) UnCompressed : ', wifu53)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key53.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr53)
        f.write('\nBitcoin Address UnCompressed :' + uaddr53)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc53)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu53)
        f.close() 
    if caddr54 in add or uaddr54 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key54.to_hex(), '\nBitcoin Address Compressed : ', caddr54, '\nBitcoin Address UnCompressed :', uaddr54, '\nPrivateKey (wif) Compressed : ', wifc54, '\nPrivateKey (wif) UnCompressed : ', wifu54)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key54.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr54)
        f.write('\nBitcoin Address UnCompressed :' + uaddr54)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc54)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu54)
        f.close() 
    if caddr55 in add or uaddr55 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key55.to_hex(), '\nBitcoin Address Compressed : ', caddr55, '\nBitcoin Address UnCompressed :', uaddr55, '\nPrivateKey (wif) Compressed : ', wifc55, '\nPrivateKey (wif) UnCompressed : ', wifu55)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key55.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr55)
        f.write('\nBitcoin Address UnCompressed :' + uaddr55)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc55)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu55)
        f.close() 
    if caddr56 in add or uaddr56 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key56.to_hex(), '\nBitcoin Address Compressed : ', caddr56, '\nBitcoin Address UnCompressed :', uaddr56, '\nPrivateKey (wif) Compressed : ', wifc56, '\nPrivateKey (wif) UnCompressed : ', wifu56)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key56.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr56)
        f.write('\nBitcoin Address UnCompressed :' + uaddr56)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc56)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu56)
        f.close() 
    if caddr57 in add or uaddr57 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key57.to_hex(), '\nBitcoin Address Compressed : ', caddr57, '\nBitcoin Address UnCompressed :', uaddr57, '\nPrivateKey (wif) Compressed : ', wifc57, '\nPrivateKey (wif) UnCompressed : ', wifu57)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key57.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr57)
        f.write('\nBitcoin Address UnCompressed :' + uaddr57)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc57)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu57)
        f.close() 
    if caddr58 in add or uaddr58 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key58.to_hex(), '\nBitcoin Address Compressed : ', caddr58, '\nBitcoin Address UnCompressed :', uaddr58, '\nPrivateKey (wif) Compressed : ', wifc58, '\nPrivateKey (wif) UnCompressed : ', wifu58)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key58.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr58)
        f.write('\nBitcoin Address UnCompressed :' + uaddr58)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc58)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu58)
        f.close() 
    if caddr59 in add or uaddr59 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key59.to_hex(), '\nBitcoin Address Compressed : ', caddr59, '\nBitcoin Address UnCompressed :', uaddr59, '\nPrivateKey (wif) Compressed : ', wifc59, '\nPrivateKey (wif) UnCompressed : ', wifu59)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key59.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr59)
        f.write('\nBitcoin Address UnCompressed :' + uaddr59)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc59)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu59)
        f.close() 
    if caddr60 in add or uaddr60 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key60.to_hex(), '\nBitcoin Address Compressed : ', caddr60, '\nBitcoin Address UnCompressed :', uaddr60, '\nPrivateKey (wif) Compressed : ', wifc60, '\nPrivateKey (wif) UnCompressed : ', wifu60)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key60.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr60)
        f.write('\nBitcoin Address UnCompressed :' + uaddr60)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc60)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu60)
        f.close() 
    if caddr61 in add or uaddr61 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key61.to_hex(), '\nBitcoin Address Compressed : ', caddr61, '\nBitcoin Address UnCompressed :', uaddr61, '\nPrivateKey (wif) Compressed : ', wifc61, '\nPrivateKey (wif) UnCompressed : ', wifu61)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key61.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr61)
        f.write('\nBitcoin Address UnCompressed :' + uaddr61)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc61)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu61)
        f.close() 
    if caddr62 in add or uaddr62 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key62.to_hex(), '\nBitcoin Address Compressed : ', caddr62, '\nBitcoin Address UnCompressed :', uaddr62, '\nPrivateKey (wif) Compressed : ', wifc62, '\nPrivateKey (wif) UnCompressed : ', wifu62)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key62.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr62)
        f.write('\nBitcoin Address UnCompressed :' + uaddr62)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc62)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu62)
        f.close() 
    if caddr63 in add or uaddr63 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key63.to_hex(), '\nBitcoin Address Compressed : ', caddr63, '\nBitcoin Address UnCompressed :', uaddr63, '\nPrivateKey (wif) Compressed : ', wifc63, '\nPrivateKey (wif) UnCompressed : ', wifu63)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key63.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr63)
        f.write('\nBitcoin Address UnCompressed :' + uaddr63)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc63)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu63)
        f.close() 
    if caddr64 in add or uaddr64 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key64.to_hex(), '\nBitcoin Address Compressed : ', caddr64, '\nBitcoin Address UnCompressed :', uaddr64, '\nPrivateKey (wif) Compressed : ', wifc64, '\nPrivateKey (wif) UnCompressed : ', wifu64)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key64.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr64)
        f.write('\nBitcoin Address UnCompressed :' + uaddr64)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc64)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu64)
        f.close() 
    if caddr65 in add or uaddr65 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key65.to_hex(), '\nBitcoin Address Compressed : ', caddr65, '\nBitcoin Address UnCompressed :', uaddr65, '\nPrivateKey (wif) Compressed : ', wifc65, '\nPrivateKey (wif) UnCompressed : ', wifu65)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key65.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr65)
        f.write('\nBitcoin Address UnCompressed :' + uaddr65)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc65)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu65)
        f.close()         
    if caddr66 in add or uaddr66 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key66.to_hex(), '\nBitcoin Address Compressed : ', caddr66, '\nBitcoin Address UnCompressed :', uaddr66, '\nPrivateKey (wif) Compressed : ', wifc66, '\nPrivateKey (wif) UnCompressed : ', wifu66)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key66.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr66)
        f.write('\nBitcoin Address UnCompressed :' + uaddr66)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc66)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu66)
        f.close()  
    if caddr67 in add or uaddr67 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key67.to_hex(), '\nBitcoin Address Compressed : ', caddr67, '\nBitcoin Address UnCompressed :', uaddr67, '\nPrivateKey (wif) Compressed : ', wifc67, '\nPrivateKey (wif) UnCompressed : ', wifu67)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key67.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr67)
        f.write('\nBitcoin Address UnCompressed :' + uaddr67)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc67)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu67)
        f.close()  
    if caddr68 in add or uaddr68 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key68.to_hex(), '\nBitcoin Address Compressed : ', caddr68, '\nBitcoin Address UnCompressed :', uaddr68, '\nPrivateKey (wif) Compressed : ', wifc68, '\nPrivateKey (wif) UnCompressed : ', wifu68)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key68.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr68)
        f.write('\nBitcoin Address UnCompressed :' + uaddr68)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc68)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu68)
        f.close()  
    if caddr69 in add or uaddr69 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key69.to_hex(), '\nBitcoin Address Compressed : ', caddr69, '\nBitcoin Address UnCompressed :', uaddr69, '\nPrivateKey (wif) Compressed : ', wifc69, '\nPrivateKey (wif) UnCompressed : ', wifu69)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key69.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr69)
        f.write('\nBitcoin Address UnCompressed :' + uaddr69)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc69)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu69)
        f.close()  
    if caddr70 in add or uaddr70 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key70.to_hex(), '\nBitcoin Address Compressed : ', caddr70, '\nBitcoin Address UnCompressed :', uaddr70, '\nPrivateKey (wif) Compressed : ', wifc70, '\nPrivateKey (wif) UnCompressed : ', wifu70)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key70.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr70)
        f.write('\nBitcoin Address UnCompressed :' + uaddr70)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc70)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu70)
        f.close()  
    if caddr71 in add or uaddr71 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key71.to_hex(), '\nBitcoin Address Compressed : ', caddr71, '\nBitcoin Address UnCompressed :', uaddr71, '\nPrivateKey (wif) Compressed : ', wifc71, '\nPrivateKey (wif) UnCompressed : ', wifu71)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key71.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr71)
        f.write('\nBitcoin Address UnCompressed :' + uaddr71)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc71)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu71)
        f.close()  
    if caddr72 in add or uaddr72 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key72.to_hex(), '\nBitcoin Address Compressed : ', caddr72, '\nBitcoin Address UnCompressed :', uaddr72, '\nPrivateKey (wif) Compressed : ', wifc72, '\nPrivateKey (wif) UnCompressed : ', wifu72)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key72.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr72)
        f.write('\nBitcoin Address UnCompressed :' + uaddr72)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc72)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu72)
        f.close()  
    if caddr73 in add or uaddr73 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key73.to_hex(), '\nBitcoin Address Compressed : ', caddr73, '\nBitcoin Address UnCompressed :', uaddr73, '\nPrivateKey (wif) Compressed : ', wifc73, '\nPrivateKey (wif) UnCompressed : ', wifu73)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key73.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr73)
        f.write('\nBitcoin Address UnCompressed :' + uaddr73)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc73)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu73)
        f.close()  
    if caddr74 in add or uaddr74 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key74.to_hex(), '\nBitcoin Address Compressed : ', caddr74, '\nBitcoin Address UnCompressed :', uaddr74, '\nPrivateKey (wif) Compressed : ', wifc74, '\nPrivateKey (wif) UnCompressed : ', wifu74)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key74.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr74)
        f.write('\nBitcoin Address UnCompressed :' + uaddr74)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc74)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu74)
        f.close()  
    if caddr75 in add or uaddr75 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key75.to_hex(), '\nBitcoin Address Compressed : ', caddr75, '\nBitcoin Address UnCompressed :', uaddr75, '\nPrivateKey (wif) Compressed : ', wifc75, '\nPrivateKey (wif) UnCompressed : ', wifu75)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key75.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr75)
        f.write('\nBitcoin Address UnCompressed :' + uaddr75)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc75)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu75)
        f.close()  
    if caddr76 in add or uaddr76 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key76.to_hex(), '\nBitcoin Address Compressed : ', caddr76, '\nBitcoin Address UnCompressed :', uaddr76, '\nPrivateKey (wif) Compressed : ', wifc76, '\nPrivateKey (wif) UnCompressed : ', wifu76)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key76.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr76)
        f.write('\nBitcoin Address UnCompressed :' + uaddr76)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc76)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu76)
        f.close()  
    if caddr77 in add or uaddr77 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key77.to_hex(), '\nBitcoin Address Compressed : ', caddr77, '\nBitcoin Address UnCompressed :', uaddr77, '\nPrivateKey (wif) Compressed : ', wifc77, '\nPrivateKey (wif) UnCompressed : ', wifu77)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key77.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr77)
        f.write('\nBitcoin Address UnCompressed :' + uaddr77)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc77)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu77)
        f.close()  
    if caddr78 in add or uaddr78 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key78.to_hex(), '\nBitcoin Address Compressed : ', caddr78, '\nBitcoin Address UnCompressed :', uaddr78, '\nPrivateKey (wif) Compressed : ', wifc78, '\nPrivateKey (wif) UnCompressed : ', wifu78)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key78.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr78)
        f.write('\nBitcoin Address UnCompressed :' + uaddr78)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc78)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu78)
        f.close()  
    if caddr79 in add or uaddr79 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key79.to_hex(), '\nBitcoin Address Compressed : ', caddr79, '\nBitcoin Address UnCompressed :', uaddr79, '\nPrivateKey (wif) Compressed : ', wifc79, '\nPrivateKey (wif) UnCompressed : ', wifu79)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key79.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr79)
        f.write('\nBitcoin Address UnCompressed :' + uaddr79)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc79)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu79)
        f.close()  
    if caddr80 in add or uaddr80 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key80.to_hex(), '\nBitcoin Address Compressed : ', caddr80, '\nBitcoin Address UnCompressed :', uaddr80, '\nPrivateKey (wif) Compressed : ', wifc80, '\nPrivateKey (wif) UnCompressed : ', wifu80)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key80.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr80)
        f.write('\nBitcoin Address UnCompressed :' + uaddr80)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc80)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu80)
        f.close()  
    if caddr81 in add or uaddr81 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key81.to_hex(), '\nBitcoin Address Compressed : ', caddr81, '\nBitcoin Address UnCompressed :', uaddr81, '\nPrivateKey (wif) Compressed : ', wifc81, '\nPrivateKey (wif) UnCompressed : ', wifu81)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key81.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr81)
        f.write('\nBitcoin Address UnCompressed :' + uaddr81)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc81)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu81)
        f.close()  
    if caddr82 in add or uaddr82 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key82.to_hex(), '\nBitcoin Address Compressed : ', caddr82, '\nBitcoin Address UnCompressed :', uaddr82, '\nPrivateKey (wif) Compressed : ', wifc82, '\nPrivateKey (wif) UnCompressed : ', wifu82)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key82.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr82)
        f.write('\nBitcoin Address UnCompressed :' + uaddr82)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc82)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu82)
        f.close()  
    if caddr83 in add or uaddr83 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key83.to_hex(), '\nBitcoin Address Compressed : ', caddr83, '\nBitcoin Address UnCompressed :', uaddr83, '\nPrivateKey (wif) Compressed : ', wifc83, '\nPrivateKey (wif) UnCompressed : ', wifu83)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key83.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr83)
        f.write('\nBitcoin Address UnCompressed :' + uaddr83)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc83)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu83)
        f.close()  
    if caddr84 in add or uaddr84 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key84.to_hex(), '\nBitcoin Address Compressed : ', caddr84, '\nBitcoin Address UnCompressed :', uaddr84, '\nPrivateKey (wif) Compressed : ', wifc84, '\nPrivateKey (wif) UnCompressed : ', wifu84)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key84.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr84)
        f.write('\nBitcoin Address UnCompressed :' + uaddr84)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc84)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu84)
        f.close()  
    if caddr85 in add or uaddr85 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key85.to_hex(), '\nBitcoin Address Compressed : ', caddr85, '\nBitcoin Address UnCompressed :', uaddr85, '\nPrivateKey (wif) Compressed : ', wifc85, '\nPrivateKey (wif) UnCompressed : ', wifu85)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key85.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr85)
        f.write('\nBitcoin Address UnCompressed :' + uaddr85)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc85)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu85)
        f.close()  
    if caddr86 in add or uaddr86 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key86.to_hex(), '\nBitcoin Address Compressed : ', caddr86, '\nBitcoin Address UnCompressed :', uaddr86, '\nPrivateKey (wif) Compressed : ', wifc86, '\nPrivateKey (wif) UnCompressed : ', wifu86)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key86.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr86)
        f.write('\nBitcoin Address UnCompressed :' + uaddr86)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc86)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu86)
        f.close()  
    if caddr87 in add or uaddr87 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key87.to_hex(), '\nBitcoin Address Compressed : ', caddr87, '\nBitcoin Address UnCompressed :', uaddr87, '\nPrivateKey (wif) Compressed : ', wifc87, '\nPrivateKey (wif) UnCompressed : ', wifu87)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key87.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr87)
        f.write('\nBitcoin Address UnCompressed :' + uaddr87)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc87)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu87)
        f.close()  
    if caddr88 in add or uaddr88 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key88.to_hex(), '\nBitcoin Address Compressed : ', caddr88, '\nBitcoin Address UnCompressed :', uaddr88, '\nPrivateKey (wif) Compressed : ', wifc88, '\nPrivateKey (wif) UnCompressed : ', wifu88)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key88.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr88)
        f.write('\nBitcoin Address UnCompressed :' + uaddr88)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc88)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu88)
        f.close()  
    if caddr89 in add or uaddr89 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key89.to_hex(), '\nBitcoin Address Compressed : ', caddr89, '\nBitcoin Address UnCompressed :', uaddr89, '\nPrivateKey (wif) Compressed : ', wifc89, '\nPrivateKey (wif) UnCompressed : ', wifu89)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key89.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr89)
        f.write('\nBitcoin Address UnCompressed :' + uaddr89)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc89)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu89)
        f.close()  
    if caddr90 in add or uaddr90 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key90.to_hex(), '\nBitcoin Address Compressed : ', caddr90, '\nBitcoin Address UnCompressed :', uaddr90, '\nPrivateKey (wif) Compressed : ', wifc90, '\nPrivateKey (wif) UnCompressed : ', wifu90)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key90.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr90)
        f.write('\nBitcoin Address UnCompressed :' + uaddr90)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc90)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu90)
        f.close()  
    if caddr91 in add or uaddr91 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key91.to_hex(), '\nBitcoin Address Compressed : ', caddr91, '\nBitcoin Address UnCompressed :', uaddr91, '\nPrivateKey (wif) Compressed : ', wifc91, '\nPrivateKey (wif) UnCompressed : ', wifu91)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key91.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr91)
        f.write('\nBitcoin Address UnCompressed :' + uaddr91)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc91)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu91)
        f.close()  
    if caddr92 in add or uaddr92 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key92.to_hex(), '\nBitcoin Address Compressed : ', caddr92, '\nBitcoin Address UnCompressed :', uaddr92, '\nPrivateKey (wif) Compressed : ', wifc92, '\nPrivateKey (wif) UnCompressed : ', wifu92)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key92.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr92)
        f.write('\nBitcoin Address UnCompressed :' + uaddr92)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc92)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu92)
        f.close()  
    if caddr93 in add or uaddr93 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key93.to_hex(), '\nBitcoin Address Compressed : ', caddr93, '\nBitcoin Address UnCompressed :', uaddr93, '\nPrivateKey (wif) Compressed : ', wifc93, '\nPrivateKey (wif) UnCompressed : ', wifu93)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key93.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr93)
        f.write('\nBitcoin Address UnCompressed :' + uaddr93)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc93)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu93)
        f.close()  
    if caddr94 in add or uaddr94 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key94.to_hex(), '\nBitcoin Address Compressed : ', caddr94, '\nBitcoin Address UnCompressed :', uaddr94, '\nPrivateKey (wif) Compressed : ', wifc94, '\nPrivateKey (wif) UnCompressed : ', wifu94)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key94.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr94)
        f.write('\nBitcoin Address UnCompressed :' + uaddr94)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc94)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu94)
        f.close()  
    if caddr95 in add or uaddr95 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key95.to_hex(), '\nBitcoin Address Compressed : ', caddr95, '\nBitcoin Address UnCompressed :', uaddr95, '\nPrivateKey (wif) Compressed : ', wifc95, '\nPrivateKey (wif) UnCompressed : ', wifu95)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key95.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr95)
        f.write('\nBitcoin Address UnCompressed :' + uaddr95)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc95)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu95)
        f.close()   
    if caddr96 in add or uaddr96 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key96.to_hex(), '\nBitcoin Address Compressed : ', caddr96, '\nBitcoin Address UnCompressed :', uaddr96, '\nPrivateKey (wif) Compressed : ', wifc96, '\nPrivateKey (wif) UnCompressed : ', wifu96)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key96.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr96)
        f.write('\nBitcoin Address UnCompressed :' + uaddr96)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc96)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu96)
        f.close()  
    if caddr97 in add or uaddr97 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key97.to_hex(), '\nBitcoin Address Compressed : ', caddr97, '\nBitcoin Address UnCompressed :', uaddr97, '\nPrivateKey (wif) Compressed : ', wifc97, '\nPrivateKey (wif) UnCompressed : ', wifu97)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key97.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr97)
        f.write('\nBitcoin Address UnCompressed :' + uaddr97)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc97)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu97)
        f.close()  
    if caddr98 in add or uaddr98 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key98.to_hex(), '\nBitcoin Address Compressed : ', caddr98, '\nBitcoin Address UnCompressed :', uaddr98, '\nPrivateKey (wif) Compressed : ', wifc98, '\nPrivateKey (wif) UnCompressed : ', wifu98)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key98.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr98)
        f.write('\nBitcoin Address UnCompressed :' + uaddr98)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc98)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu98)
        f.close()  
    if caddr99 in add or uaddr99 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key99.to_hex(), '\nBitcoin Address Compressed : ', caddr99, '\nBitcoin Address UnCompressed :', uaddr99, '\nPrivateKey (wif) Compressed : ', wifc99, '\nPrivateKey (wif) UnCompressed : ', wifu99)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key99.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr99)
        f.write('\nBitcoin Address UnCompressed :' + uaddr99)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc99)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu99)
        f.close()  
    if caddr100 in add or uaddr100 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key100.to_hex(), '\nBitcoin Address Compressed : ', caddr100, '\nBitcoin Address UnCompressed :', uaddr100, '\nPrivateKey (wif) Compressed : ', wifc100, '\nPrivateKey (wif) UnCompressed : ', wifu100)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key100.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr100)
        f.write('\nBitcoin Address UnCompressed :' + uaddr100)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc100)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu100)
        f.close()  
    if caddr101 in add or uaddr101 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key101.to_hex(), '\nBitcoin Address Compressed : ', caddr101, '\nBitcoin Address UnCompressed :', uaddr101, '\nPrivateKey (wif) Compressed : ', wifc101, '\nPrivateKey (wif) UnCompressed : ', wifu101)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key101.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr101)
        f.write('\nBitcoin Address UnCompressed :' + uaddr101)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc101)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu101)
        f.close()  
    if caddr102 in add or uaddr102 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key102.to_hex(), '\nBitcoin Address Compressed : ', caddr102, '\nBitcoin Address UnCompressed :', uaddr102, '\nPrivateKey (wif) Compressed : ', wifc102, '\nPrivateKey (wif) UnCompressed : ', wifu102)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key102.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr102)
        f.write('\nBitcoin Address UnCompressed :' + uaddr102)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc102)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu102)
        f.close()  
    if caddr103 in add or uaddr103 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key103.to_hex(), '\nBitcoin Address Compressed : ', caddr103, '\nBitcoin Address UnCompressed :', uaddr103, '\nPrivateKey (wif) Compressed : ', wifc103, '\nPrivateKey (wif) UnCompressed : ', wifu103)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key103.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr103)
        f.write('\nBitcoin Address UnCompressed :' + uaddr103)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc103)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu103)
        f.close()  
    if caddr104 in add or uaddr104 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key104.to_hex(), '\nBitcoin Address Compressed : ', caddr104, '\nBitcoin Address UnCompressed :', uaddr104, '\nPrivateKey (wif) Compressed : ', wifc104, '\nPrivateKey (wif) UnCompressed : ', wifu104)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key104.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr104)
        f.write('\nBitcoin Address UnCompressed :' + uaddr104)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc104)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu104)
        f.close()  
    if caddr105 in add or uaddr105 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key105.to_hex(), '\nBitcoin Address Compressed : ', caddr105, '\nBitcoin Address UnCompressed :', uaddr105, '\nPrivateKey (wif) Compressed : ', wifc105, '\nPrivateKey (wif) UnCompressed : ', wifu105)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key105.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr105)
        f.write('\nBitcoin Address UnCompressed :' + uaddr105)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc105)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu105)
        f.close()  
    if caddr106 in add or uaddr106 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key106.to_hex(), '\nBitcoin Address Compressed : ', caddr106, '\nBitcoin Address UnCompressed :', uaddr106, '\nPrivateKey (wif) Compressed : ', wifc106, '\nPrivateKey (wif) UnCompressed : ', wifu106)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key106.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr106)
        f.write('\nBitcoin Address UnCompressed :' + uaddr106)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc106)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu106)
        f.close()  
    if caddr107 in add or uaddr107 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key107.to_hex(), '\nBitcoin Address Compressed : ', caddr107, '\nBitcoin Address UnCompressed :', uaddr107, '\nPrivateKey (wif) Compressed : ', wifc107, '\nPrivateKey (wif) UnCompressed : ', wifu107)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key107.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr107)
        f.write('\nBitcoin Address UnCompressed :' + uaddr107)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc107)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu107)
        f.close()  
    if caddr108 in add or uaddr108 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key108.to_hex(), '\nBitcoin Address Compressed : ', caddr108, '\nBitcoin Address UnCompressed :', uaddr108, '\nPrivateKey (wif) Compressed : ', wifc108, '\nPrivateKey (wif) UnCompressed : ', wifu108)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key108.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr108)
        f.write('\nBitcoin Address UnCompressed :' + uaddr108)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc108)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu108)
        f.close()  
    if caddr109 in add or uaddr109 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key109.to_hex(), '\nBitcoin Address Compressed : ', caddr109, '\nBitcoin Address UnCompressed :', uaddr109, '\nPrivateKey (wif) Compressed : ', wifc109, '\nPrivateKey (wif) UnCompressed : ', wifu109)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key109.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr109)
        f.write('\nBitcoin Address UnCompressed :' + uaddr109)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc109)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu109)
        f.close()  
    if caddr110 in add or uaddr110 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key110.to_hex(), '\nBitcoin Address Compressed : ', caddr110, '\nBitcoin Address UnCompressed :', uaddr110, '\nPrivateKey (wif) Compressed : ', wifc110, '\nPrivateKey (wif) UnCompressed : ', wifu110)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key110.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr110)
        f.write('\nBitcoin Address UnCompressed :' + uaddr110)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc110)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu110)
        f.close()  
    if caddr111 in add or uaddr111 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key111.to_hex(), '\nBitcoin Address Compressed : ', caddr111, '\nBitcoin Address UnCompressed :', uaddr111, '\nPrivateKey (wif) Compressed : ', wifc111, '\nPrivateKey (wif) UnCompressed : ', wifu111)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key111.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr111)
        f.write('\nBitcoin Address UnCompressed :' + uaddr111)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc111)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu111)
        f.close()  
    if caddr112 in add or uaddr112 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key112.to_hex(), '\nBitcoin Address Compressed : ', caddr112, '\nBitcoin Address UnCompressed :', uaddr112, '\nPrivateKey (wif) Compressed : ', wifc112, '\nPrivateKey (wif) UnCompressed : ', wifu112)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key112.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr112)
        f.write('\nBitcoin Address UnCompressed :' + uaddr112)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc112)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu112)
        f.close()  
    if caddr113 in add or uaddr113 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key113.to_hex(), '\nBitcoin Address Compressed : ', caddr113, '\nBitcoin Address UnCompressed :', uaddr113, '\nPrivateKey (wif) Compressed : ', wifc113, '\nPrivateKey (wif) UnCompressed : ', wifu113)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key113.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr113)
        f.write('\nBitcoin Address UnCompressed :' + uaddr113)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc113)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu113)
        f.close()  
    if caddr114 in add or uaddr114 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key114.to_hex(), '\nBitcoin Address Compressed : ', caddr114, '\nBitcoin Address UnCompressed :', uaddr114, '\nPrivateKey (wif) Compressed : ', wifc114, '\nPrivateKey (wif) UnCompressed : ', wifu114)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key114.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr114)
        f.write('\nBitcoin Address UnCompressed :' + uaddr114)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc114)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu114)
        f.close()  
    if caddr115 in add or uaddr115 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key115.to_hex(), '\nBitcoin Address Compressed : ', caddr115, '\nBitcoin Address UnCompressed :', uaddr115, '\nPrivateKey (wif) Compressed : ', wifc115, '\nPrivateKey (wif) UnCompressed : ', wifu115)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key115.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr115)
        f.write('\nBitcoin Address UnCompressed :' + uaddr115)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc115)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu115)
        f.close()  
    if caddr116 in add or uaddr116 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key116.to_hex(), '\nBitcoin Address Compressed : ', caddr116, '\nBitcoin Address UnCompressed :', uaddr116, '\nPrivateKey (wif) Compressed : ', wifc116, '\nPrivateKey (wif) UnCompressed : ', wifu116)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key116.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr116)
        f.write('\nBitcoin Address UnCompressed :' + uaddr116)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc116)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu116)
        f.close()  
    if caddr117 in add or uaddr117 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key117.to_hex(), '\nBitcoin Address Compressed : ', caddr117, '\nBitcoin Address UnCompressed :', uaddr117, '\nPrivateKey (wif) Compressed : ', wifc117, '\nPrivateKey (wif) UnCompressed : ', wifu117)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key117.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr117)
        f.write('\nBitcoin Address UnCompressed :' + uaddr117)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc117)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu117)
        f.close()  
    if caddr118 in add or uaddr118 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key118.to_hex(), '\nBitcoin Address Compressed : ', caddr118, '\nBitcoin Address UnCompressed :', uaddr118, '\nPrivateKey (wif) Compressed : ', wifc118, '\nPrivateKey (wif) UnCompressed : ', wifu118)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key118.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr118)
        f.write('\nBitcoin Address UnCompressed :' + uaddr118)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc118)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu118)
        f.close()       
    if caddr119 in add or uaddr119 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key119.to_hex(), '\nBitcoin Address Compressed : ', caddr119, '\nBitcoin Address UnCompressed :', uaddr119, '\nPrivateKey (wif) Compressed : ', wifc119, '\nPrivateKey (wif) UnCompressed : ', wifu119)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key119.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr119)
        f.write('\nBitcoin Address UnCompressed :' + uaddr119)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc119)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu119)
        f.close()  
    if caddr120 in add or uaddr120 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key120.to_hex(), '\nBitcoin Address Compressed : ', caddr120, '\nBitcoin Address UnCompressed :', uaddr120, '\nPrivateKey (wif) Compressed : ', wifc120, '\nPrivateKey (wif) UnCompressed : ', wifu120)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key120.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr120)
        f.write('\nBitcoin Address UnCompressed :' + uaddr120)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc120)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu120)
        f.close()  
    if caddr121 in add or uaddr121 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key121.to_hex(), '\nBitcoin Address Compressed : ', caddr121, '\nBitcoin Address UnCompressed :', uaddr121, '\nPrivateKey (wif) Compressed : ', wifc121, '\nPrivateKey (wif) UnCompressed : ', wifu121)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key121.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr121)
        f.write('\nBitcoin Address UnCompressed :' + uaddr121)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc121)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu121)
        f.close()  
    if caddr122 in add or uaddr122 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key122.to_hex(), '\nBitcoin Address Compressed : ', caddr122, '\nBitcoin Address UnCompressed :', uaddr122, '\nPrivateKey (wif) Compressed : ', wifc122, '\nPrivateKey (wif) UnCompressed : ', wifu122)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key122.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr122)
        f.write('\nBitcoin Address UnCompressed :' + uaddr122)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc122)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu122)
        f.close()  
    if caddr123 in add or uaddr123 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key123.to_hex(), '\nBitcoin Address Compressed : ', caddr123, '\nBitcoin Address UnCompressed :', uaddr123, '\nPrivateKey (wif) Compressed : ', wifc123, '\nPrivateKey (wif) UnCompressed : ', wifu123)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key123.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr123)
        f.write('\nBitcoin Address UnCompressed :' + uaddr123)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc123)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu123)
        f.close()  
    if caddr124 in add or uaddr124 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key124.to_hex(), '\nBitcoin Address Compressed : ', caddr124, '\nBitcoin Address UnCompressed :', uaddr124, '\nPrivateKey (wif) Compressed : ', wifc124, '\nPrivateKey (wif) UnCompressed : ', wifu124)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key124.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr124)
        f.write('\nBitcoin Address UnCompressed :' + uaddr124)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc124)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu124)
        f.close()  
    if caddr125 in add or uaddr125 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key125.to_hex(), '\nBitcoin Address Compressed : ', caddr125, '\nBitcoin Address UnCompressed :', uaddr125, '\nPrivateKey (wif) Compressed : ', wifc125, '\nPrivateKey (wif) UnCompressed : ', wifu125)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key125.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr125)
        f.write('\nBitcoin Address UnCompressed :' + uaddr125)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc125)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu125)
        f.close()  
    if caddr126 in add or uaddr126 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key126.to_hex(), '\nBitcoin Address Compressed : ', caddr126, '\nBitcoin Address UnCompressed :', uaddr126, '\nPrivateKey (wif) Compressed : ', wifc126, '\nPrivateKey (wif) UnCompressed : ', wifu126)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key126.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr126)
        f.write('\nBitcoin Address UnCompressed :' + uaddr126)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc126)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu126)
        f.close()     
    if caddr127 in add or uaddr127 in add:
        print ('Matching Key ==== Found!!!\n PrivateKey HEX: ', key127.to_hex(), '\nBitcoin Address Compressed : ', caddr127, '\nBitcoin Address UnCompressed :', uaddr127, '\nPrivateKey (wif) Compressed : ', wifc127, '\nPrivateKey (wif) UnCompressed : ', wifu127)
        f=open("winner.txt","a")
        f.write('\nPrivateKey (hex): ' + key127.to_hex())
        f.write('\nBitcoin Address Compressed : ' + caddr127)
        f.write('\nBitcoin Address UnCompressed :' + uaddr127)
        f.write('\nPrivateKey (wif) Compressed : ' + wifc127)
        f.write('\nPrivateKey (wif) UnCompressed : ' + wifu127)
        f.close()          
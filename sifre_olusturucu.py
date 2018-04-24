print("Bu program, en az bir küçük harf, bir büyük harf, bir rakam ve bir \
sembolden oluşan 10 karakterlik şifreler üretir.")
kucuk_harfler = "abcdefghijklmnopqrstuvwxyz"
buyuk_harfler = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rakamlar = "0123456789"
semboller = "!@€#$%&=_-/+*"

def karistir(item):
    item2 = ""    
    for j in range(len(item)):
        konum = random.randint(1,len(item)-1)
        karakter = item[konum]
        item2 += karakter
    return item2

import random
sifre = ""
while len(sifre) <= 10:
    for i in range(10):
        konum = random.randint(1, 4)
        if konum == 1:
            konum2 = karistir(kucuk_harfler)[random.randint(1, \
    len(kucuk_harfler)-1)]
            sifre += konum2
        elif konum == 2:
            konum2 = karistir(buyuk_harfler)[random.randint(1, \
    len(buyuk_harfler)-1)]
            sifre += konum2
        elif konum == 3:
            konum2 = karistir(rakamlar)[random.randint(1, len(rakamlar)-1)]
            sifre += konum2
        else:
            konum2 = karistir(semboller)[random.randint(1, len(semboller)-1)]
            sifre += konum2
    for j in sifre:
        if j in kucuk_harfler:
            ok1 = 1
        elif j in buyuk_harfler:
            ok2 = 1
        elif j in rakamlar: 
            ok3 = 1
        elif j in semboller:
            ok4 = 1
    if ok1 == 1 and ok2 ==1 and ok3 == 1 and ok4 == 1:
        print("Sifreniz: ",sifre)
        devam = input("Başka bir şifre oluşturmak istiyor musunuz (E/H)? ")
        if devam == "E" or devam == "e":
            sifre = ""            
            continue
        else:        
            break

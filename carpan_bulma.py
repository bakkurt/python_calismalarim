#Bu program bir sayının çarpanlarını bulur.
sayi = int(input("Lütfen bir sayı giriniz: "))
i = 2
orijinal_sayi = sayi
carpanlar = []
while i <= sayi:
    if sayi % i == 0:
        carpanlar.append(i)
        sayi /= i
    else:
        i += 1
print("%s sayısının çarpanları: %s"%(orijinal_sayi, carpanlar))

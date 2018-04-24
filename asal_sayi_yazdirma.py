print("Bu program, 1 ile 20000 arasındaki asal sayıları bir dosyaya yazdırır.")
dosya = open("asal_sayilar.txt", "w")

def carpan_bul(item):
    bolenler = []
    for j in range (2, item+1):
        if item % j == 0:
            bolenler.append(j)
    return bolenler
for i in range(1,20000):
    carpanlar = carpan_bul(i)
    if len(carpanlar) < 2:
        dosya.write(str(i) + "; ")
dosya.close()

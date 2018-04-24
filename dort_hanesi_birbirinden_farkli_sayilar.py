print("Bu program 1000'den başlayarak her hanesi birbirinden farklı 4 haneli\
 sayıları  bulur ve yazdırır.")
bulunanlar = open("bulunanlar.txt","w")
for i in range(1000,20000):
    if str(i).count(str(i)[0]) == 1 and str(i).count(str(i)[1]) == 1\
    and str(i).count(str(i)[2]) == 1 and str(i).count(str(i)[3]) == 1:
        bulunanlar.write(str(i)+"; ")
bulunanlar.close()
print("İşlem tamamlandı...")

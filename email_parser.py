#bu program, isim <e-posta>, isim <e-posta> biçimindeki belgeden
#e-posta adreslerini ayıklayıp yeni bir belgeye yapıştırır.
e_posta_giris = input("E-posta adreslerinin bulunduğu dosyanın adını giriniz: ")
dosya_oku = open(e_posta_giris, "r")
dosya_yaz = open("e-posta_yaz.txt","w")
metin = dosya_oku.readline()
eposta =""
for i in range (0, len(metin)):
    if metin[i] == "<":
        for j in range(i+1, len(metin)):
            if metin[j] == ">":
                break
            else:
                eposta += metin[j]
        eposta += ", "
print(eposta)
dosya_yaz.write(eposta)
dosya_oku.close()
dosya_yaz.close()

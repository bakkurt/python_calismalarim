"""Bu program FTIR verilerinin yer aldığı dosyalardan FTIR için X-Y verilerini
çeker ve başka bir dosyaya yazar."""
kaynak_dosya = input("Kaynak dosyanın adını giriniz: ")
hedef_dosya = input("Hedef dosyanın adını giriniz: ")
kaynak = open(kaynak_dosya, "r")
hedef = open(hedef_dosya, "w")
for satir in kaynak:
    if ".000000\t" in satir:
        satir = satir.replace(".000000","")
        satir = satir.replace("\t", ";")
        satir = satir.replace("; ", ";")
        hedef.write(satir)
print("Program sona erdi.")
kaynak.close()
hedef.close()

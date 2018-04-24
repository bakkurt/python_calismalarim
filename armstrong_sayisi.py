metin1 = "Armstrong sayısı bulma programı"
metin2 = """Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin
toplamı (3 basamaklı sayılar için 3.kuvveti) o sayıya eşitse bu sayıya *Armstrong sayısı* denir."""
metin3 = """Örnek: 1634 = 1^4 + 6^4 + 3^4 + 4^4"""
print("*"*20+metin1+"*"*20+"\n"+metin2+"\n"+metin3)
while True:
    sayi = int(input("Bir sayı giriniz (Çıkış için '0'): "))
    sayi_karakter = []
    toplam = 0
    if sayi == 0:
        break
    else:
        for i in str(sayi):
            sayi_karakter.append(i)
            kuvvet = len(sayi_karakter)
        print("Girdiğiniz sayi {} basamaklıdır...".format(kuvvet))
        for j in range(len(sayi_karakter)):
            toplam += int(sayi_karakter[j]) ** kuvvet
            print(int(sayi_karakter[j]),"^",kuvvet)
            print("Toplam: ",toplam)
        for k in range(1, kuvvet+1):
            if toplam == sayi:
                print("Girdiğiniz sayı bir Armstrong sayısıdır...")
            else:
                print("Girdiğiniz sayı bir Armstrong sayısı değildir...")
print("Çıkış yapılıyor...")

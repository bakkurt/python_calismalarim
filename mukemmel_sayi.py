"""Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)"""
print("*"*10, "Bu program bir sayının mükemmel sayı olup olmadığını bulur.\nMükemmel sayı, \
bir sayının kendisi hariç bölenlerinin toplamı kendisine eşit olan sayıdır.","*"*10)
      
while True:
    bolenler = []
    toplam = 0
    sayi = int(input("Bir sayı giriniz (Çıkış için '0'): "))
    if sayi == 0:
        break
    else:
        orijinal_sayi = sayi
        for i in range(1, orijinal_sayi):
            if sayi % i == 0:
                bolenler.append(i)
                sayi /= i
        for j in bolenler:
            toplam += j
        print("{} sayısının bölenleri: {}".format(orijinal_sayi, bolenler))
        if toplam == orijinal_sayi:
            print("{} bir mükemmel sayıdır...".format(orijinal_sayi))
        else:
            print("{} mükemmel bir sayı değildir...".format(orijinal_sayi))
print("Çıkış yapılıyor...")

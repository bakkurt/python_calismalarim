"""Braille alfabesindeki harfleri üç satır olarak belirtiyoruz. Soldan sağa ve yukarıdan aşağıya doğru\
inerek dolu noktaları belirtiyoruz. a, b, c, d, e ve f olarak yazıyoruz. Her seferde bir harf soruluyor.\
Başarıyla girdiğimiz harfler bir listeye yazılıyor. 0 ile çıkış yapılıyor, -1 ile yanlış harf siliniyor"""
harfler = {"a":"a", "ac": "b", "ab": "c", "af": "ç", "abd": "d", "ad": "e", "abc": "f", "abcd": "g",\
"acf": "ğ", "acd": "h", "de": "ı", "bc": "i", "bcd": "j", "ae": "k", "ace": "l", "abe": "m", "abde": "n",\
"ade": "o", "bcf": "ö", "abce": "p", "acde": "r", "bce": "s", "abf": "ş", "bcde": "t", "aef": "u", "acdf": "ü",\
"acef": "v", "abdef": "y", "adef": "z", "c":",", "ce": ";", "cd": ":", "cdf": ".", "cef": "?", "cde": "!",\
"cdef":"()", "f": "[Büyük harf: ]", "bdef": "[Rakam: ]", "bf": "[İtalik: ]"}
cozum = []
while True:
    harf_sor = input("Braille harfi giriniz (İki sütun ve üç satır olarak, noktalı yerleri abcdef sırasına \
göre yazınız. \nÖrnek: abce --> p\nÇıkış için '0'\nSilmek için '-1'): ")
    if harf_sor == "0":
        break
    elif harf_sor == "-1":
        cozum.pop()
    else:
        if harf_sor in harfler.keys():
            cozum.append(harfler[harf_sor])
        else:
            print("Böyle bir harf bulamadım... Lütfen tekrar giriniz.")
    print(cozum)

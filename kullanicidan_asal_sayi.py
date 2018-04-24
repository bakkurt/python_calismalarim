print("Bu program, kullanıcıdan alınan sayının asal sayı olup olmadığını \
test eder. ")
def hesapla(sayi):
    test_sayi = sayi
    carpanlar = [1]
    i = 2
    while sayi != 1:
        if sayi % i == 0:
            carpanlar.append(i)
            sayi /= i
        else:
            i += 1
    if len(carpanlar) == 2:
        print("\n{} sayısı asaldır...".format(test_sayi))
    else:
        print("\n{} sayısı asal değildir..".format(test_sayi))
    return "Çarpanları: {}".format(carpanlar)
while True:
    sorgu = int(input("Lutfen bir sayı giriniz (çıkış için -1): "))
    if sorgu == -1:
        print("\nProgram sona erdi...")
        break
    elif sorgu < 0 and sorgu != -1:
        sorgu = -sorgu
        print(hesapla(sorgu))
        continue
    else:
        print(hesapla(sorgu))
        continue

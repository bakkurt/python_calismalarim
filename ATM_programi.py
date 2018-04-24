print("""Bu program bir ATM makinesini taklit ederek para yatırma, bakiye sorma ve para çekme işlemlerini
yapar. q tuşu ile veya menüden 4 seçilerek programdan çıkılabilir.""")

print("""******MENÜ******\n1. Bakiye Sorma\n2. Para Yatırma\n3. Para Çekme\n4. Çıkış\n****************""")
bakiye = 1000
cep = 1000
while True:
    menu_secenek = input("Menü seçeneğini giriniz: ")
    if menu_secenek == "1":
        print("Bakiyeniz {} TL'dir... Cebinizde {} TL var...".format(bakiye, cep))
    elif menu_secenek == "2":
        print("Para yatırma seçeneğini seçtiniz. Yatırılacak miktarı giriniz: ")
        miktar = int(input())
        if miktar > cep:
            print("Bu kadar para yatıramazsınız...")
            continue
        else:
            bakiye += miktar
            cep -= miktar
        print("{} TL bakiyenize eklendi... Bakiyenizin son durumu: {} TL'dir. Cebinizde {} TL kaldı. ".format(miktar, bakiye, cep))
    elif menu_secenek == "3":
        print("Para çekme seçeneğini seçtiniz. Çekilecek miktarı giriniz: ")
        miktar = int(input())
        if bakiye - miktar < 0:
            print("Bakiyenizden {} TL çekemezsiniz! Güncel bakiyeniz {} TL'dir. Cebinizde {} TL var. ".format(miktar, bakiye, cep))
            continue
        else:
            bakiye -= miktar
            cep += miktar
            print("{} TL bakiyenizden düşüldü... Bakiyenizin son durumu: {} TL'dir. Cebinizde {} TL var. ".format(miktar, bakiye, cep))
    elif menu_secenek == "4" or menu_secenek == "q":
        print("İyi günler dileriz...")
        break

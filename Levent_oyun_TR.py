#Bu program 1'den 100'e kadar sayilari iki dugme ile ileri-geri oynatir.
global index
index = 0
sayilar = [i for i in range(0,101,1)]
aciklama = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi",
"sekiz", "dokuz", "on", "on bir", "on iki", "on üç", "on dört", "on beş",
"on altı", "on yedi", "on sekiz", "on dokuz" , "yirmi", "yirmi bir", 
"yirmi iki", "yirmi üç", "yirmi dört", "yirmi beş", "yirmi altı", "yirmi yedi", "yirmi sekiz", "yirmi dokuz", "otuz", "otuz bir", "otuz iki", "otuz üç", "otuz dört", "otuz beş", "otuz altı", "otuz yedi", "otuz sekiz", "otuz dokuz", "kırk", "kırk bir", "kırk iki", "kırk üç", "kırk dört", "kırk beş", "kırk altı", "kırk yedi", "kırk sekiz", "kırk dokuz", "elli", "elli bir", "elli iki", "elli üç", "elli dört", "elli beş", "elli altı", "elli yedi", "elli sekiz", "elli dokuz", "altmış", "altmış bir", "altmış iki", "altmış üç", "altmış dört", "altmış beş", "altmış altı", "altmış yedi", "altmış sekiz", "altmış dokuz", "yetmiş", "yetmiş bir", "yetmiş iki", "yetmiş üç", "yetmiş dört", "yetmiş beş", "yetmiş altı", "yetmiş yedi", "yetmiş sekiz", "yetmiş dokuz", "seksen", "seksen bir", "seksen iki", "seksen üç", "seksen dört", "seksen beş", "seksen altı", "seksen yedi", "seksen sekiz", "seksen dokuz", "doksan", "doksan bir", "doksan iki", "doksan üç", "doksan dört", "doksan beş", "doksan altı", "doksan yedi", "doksan sekiz", "doksan dokuz", "yüz"]
from tkinter import *

def geri():
    global index
    index = index -1
    if index < 0:
        index = 0
    etiket["text"] = str(sayilar[index])+"\n"+str(aciklama[index])

def ileri():
    global index 
    index = index + 1
    if index >100:
        index = 100
    etiket["text"] = str(sayilar[index])+"\n"+str(aciklama[index])

def sifirla():
    global index
    index = 0
    etiket["text"] = str(sayilar[index])+"\n"+str(aciklama[index])

pencere = Tk()
pencere.title("Levent oyun")

pencere.geometry("450x200")
pencere.resizable(width = "false", height = "false")

etiket = Label(text = str(sayilar[index])+"\n"+str(aciklama[index]), fg = "yellow", bg = "red", font = 
"Verdana 30 bold")
etiket.pack()

cerceve = Frame()
cerceve.pack()

dugme_geri = Button(cerceve, text = "Geri", font = "Verdana 16 bold", command = 
geri)
dugme_geri.pack(side = "left")

dugme_sifirla = Button(cerceve, text = "Sıfırla", font = "Verdana 16 bold", command = sifirla)
dugme_sifirla.pack(side= "left")

dugme_ileri = Button(cerceve, text = "İleri", font = "Verdana 16 bold", command 
= ileri)
dugme_ileri.pack(side = "left")

mainloop()

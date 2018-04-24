#Bu program 1'den 100'e kadar sayilari iki dugme ile ileri geri oynatir.
global index
index=0
sayilar=[i for i in range(0,101,1)]
aciklama=["zero", "one", "two", "three", "four", "five", "six", "seven", 
"eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
"sixteen", "seventeen", "eighteen", "nineteen","twenty", "twenty-one", 
"twenty-two", "twenty-three", "twenty-four", "twenty-five", "twenty-six", 
"twenty-seven", "twenty-eight", "twenty-nine", "thirty", "thirty-one", "thirty-two", 
"thirty-three", "thirty-four", "thirty-five", "thirty-six", "thirty-seven", "thirty-eight", 
"thirty-nine", "forty", "forty-one", "forty-two", "forty-three", "forty-four", 
"forty-five", "forty-six", "forty-seven", "forty-eight", "forty-nine", "fifty", "fifty-one", 
"fifty-two", "fifty-three", "fifty-four", "fifty-five", "fifty-six", "fifty-seven", "fifty-eight", 
"fifty-nine", "sixty", "sixty-one", "sixty-two", "sixty-three", "sixty-four", "sixty-five", 
"sixty-six", "sixty-seven", "sixty-eight", "sixty-nine", "seventy", "seventy-one", 
"seventy-two", "seventy-three", "seventy-four", "seventy-five", "seventy-six", 
"seventy-seven", "seventy-eight", "seventy-nine", "eighty", "eighty-one", 
"eighty-two", "eighty-three", "eighty-four", "eighty-five", "eighty-six", 
"eighty-seven", "eighty-eight", "eighty-nine", "ninety", "ninety-one", "ninety-two", 
"ninety-three", "ninety-four", "ninety-five", "ninety-six", "ninety-seven", 
"ninety-eight", "ninety-nine", "one hundred"]
from tkinter import*

def geri():
    global index
    index-=1
    if index < 0:
        index = 0
    etiket["text"]=str(sayilar[index])+"\n"+str(aciklama[index])

def ileri():
    global index 
    index += 1
    if index > 100:
        index = 100
    etiket["text"]=str(sayilar[index])+"\n"+str(aciklama[index])

def sifirla():
	global index
	index=0
	etiket["text"]=str(sayilar[index])+"\n"+str(aciklama[index])

pencere=Tk()
pencere.title("Levent's number game")

pencere.geometry("300x100")
pencere.resizable(width="false", height="false")

etiket=Label(text=str(sayilar[index])+"\n"+str(aciklama[index]), fg="yellow", bg="red", font="Arial 20 bold")
etiket.pack()

cerceve=Frame()
cerceve.pack()

dugme_geri=Button(cerceve,text="Back", font="Verdana-16-bold", command=geri)
dugme_geri.pack(side="left")

dugme_sifirla=Button(cerceve,text="Reset", font="Verdana-16-bold", command=sifirla)
dugme_sifirla.pack(side="left")

dugme_ileri=Button(cerceve,text="Forward", font="Verdana-16-bold", command=ileri)
dugme_ileri.pack(side="left")

mainloop()

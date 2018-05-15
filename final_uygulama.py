from tkinter import *
import random
import time
pencere=Tk()
pencere.resizable(width=FALSE, height=FALSE)
etiket=pencere.title("Simon Oyunu")
global seviye
seviye = 1

listeSecilecek = ("red", "blue", "yellow", "green")
listeSecilen = []# sistemin seçtiği öğeler bu listeye ekleniyor ama ekranda gösterimde sıkıntı yaşandığı için daha sonra siliniyor
listeSecilen1=[]# sistemin seçtiği öğeler aynı zamanda bu listeye de ekleniyor bu listeden döngü tamamlandığında siliniyor
listeOlusan = []#kullanıcının yaptıgı seçimler bu listeye ekleniyor


def doldur1():
    listeOlusan.append("green")
    if listeOlusan==listeSecilen1:
        Label(pencere, text="Seviye "+str(seviye),font="Times 18 bold").grid(row=0, column=0, sticky=W)
        if len(listeOlusan) + 1 > seviye-1:
            basla()
        else:
            print("hata")
    if len(listeSecilen1) == len(listeOlusan):
        if listeSecilen1 != listeOlusan:
            yenipencere = Tk()
            yenipencere.title("")
            yenipencere.geometry("300x100")
            pencere.after(2000, pencere.destroy)
            Label(yenipencere, text= "Hatalı seçim yaptınız. \n \n Skorunuz=" + str(seviye-2)).grid(padx=100, pady=25)

def doldur2():
    listeOlusan.append("yellow")
    if listeOlusan==listeSecilen1:
        Label(pencere, text="Seviye "+str(seviye),font="Times 18 bold").grid(row=0, column=0, sticky=W)
        if len(listeOlusan) + 1 > seviye-1:
            basla()
        else:
            print("hata")
    if len(listeSecilen1) == len(listeOlusan):
        if listeSecilen1 != listeOlusan:
            yenipencere = Tk()
            yenipencere.title("")
            yenipencere.geometry("300x100")
            pencere.after(2000, pencere.destroy)
            Label(yenipencere, text= "Hatalı seçim yaptınız. \n \n Skorunuz=" + str(seviye-2)).grid(padx=100, pady=25)

def doldur3():
    listeOlusan.append("blue")
    if listeOlusan==listeSecilen1:
        Label(pencere, text="Seviye "+str(seviye),font="Times 18 bold").grid(row=0, column=0, sticky=W)
        if len(listeOlusan) + 1 > seviye-1:
            basla()
        else:
            print("hata")
    if len(listeSecilen1) == len(listeOlusan):
        if listeSecilen1 != listeOlusan:
            yenipencere = Tk()
            yenipencere.title("")
            yenipencere.geometry("300x100")
            pencere.after(2000, pencere.destroy)
            Label(yenipencere, text= "Hatalı seçim yaptınız. \n \n Skorunuz=" + str(seviye-2)).grid(padx=100, pady=25)

def doldur4():
    listeOlusan.append("red")
    if listeOlusan==listeSecilen1:
        Label(pencere, text="Seviye "+str(seviye),font="Times 18 bold").grid(row=0, column=0, sticky=W)
        if len(listeOlusan) + 1 > seviye-1:
            basla()
        else:
            print("hata")
    if len(listeSecilen1) == len(listeOlusan):
        if listeSecilen1 != listeOlusan:
            yenipencere = Tk()
            yenipencere.title("")
            yenipencere.geometry("300x100")
            pencere.after(3000, pencere.destroy)
            Label(yenipencere, text= "Hatalı seçim yaptınız. \n \n Skorunuz=" + str(seviye-2)).grid(padx=100, pady=25)

def green():
    pencere.update()
    time.sleep(1)
    butonGreen.configure(bg="white")
    butonGreen.after(100, lambda: butonGreen.configure(bg="green"))
    pencere.update()
    time.sleep(1)
    butonGreen.configure(bg="green")
def yellow():
    pencere.update()
    time.sleep(1)
    butonYellow.configure(bg="white")
    butonYellow.after(100, lambda: butonYellow.configure(bg="yellow"))
    pencere.update()
    time.sleep(1)
    butonYellow.configure(bg="yellow")
def blue():
    pencere.update()
    time.sleep(1)
    butonBlue.configure(bg="white")
    butonBlue.after(100, lambda: butonBlue.configure(bg="blue"))
    pencere.update()
    time.sleep(1)
    butonBlue.configure(bg="blue")
def red():
    pencere.update()
    time.sleep(1)
    butonRed.configure(bg="white")
    butonRed.after(100, lambda: butonRed.configure(bg="red"))
    pencere.update()
    time.sleep(1)
    butonRed.configure(bg="red")


def göster():
    for x in listeSecilen:
        if "red" in listeSecilen:
            red()
            listeSecilen.pop(0)
        if "blue" in listeSecilen:
            blue()
            listeSecilen.pop(0)
        if "yellow" in listeSecilen:
            yellow()
            listeSecilen.pop(0)
        if "green" in listeSecilen:
            green()
            listeSecilen.pop(0)

def basla():
    i = 0
    butonBasla["state"]=DISABLED
    global butonNormal
    global listeOlusan
    listeOlusan.clear()
    listeSecilen.clear()
    listeSecilen1.clear()
    global seviye
    while i < seviye:
        secilen = random.choice(listeSecilecek)
        listeSecilen.append(secilen)
        listeSecilen1.append(secilen)
        göster()
        i +=1
    seviye +=1
    butonNormal()


butonGreen = Button(pencere, height=10, width=15, bg="green", command=doldur1)
butonGreen.grid(row=1, column=0)
butonYellow=Button(pencere, height=10, width=15,bg="yellow",command=doldur2)
butonYellow.grid(row=1,column=1)
butonBlue=Button(pencere,height=10,width=15,bg="blue",command=doldur3)
butonBlue.grid(row=2,column=0)
butonRed=Button(pencere ,height=10,width=15,bg="red",command=doldur4)
butonRed.grid(row=2,column=1)
butonBasla = Button(pencere, text="Oyna",font="Times 16 bold",width=9,command=basla)
butonBasla.grid(row=0, column=1, sticky=E)
Label(pencere, text="Seviye "+str(seviye),font="Times 18 bold").grid(row=0, column=0, sticky=W)

def butonNormal():
    butonGreen["state"] = NORMAL
    butonYellow["state"] = NORMAL
    butonBlue["state"] = NORMAL
    butonRed["state"] = NORMAL
def butonDisabled():
    butonGreen["state"] = DISABLED
    butonYellow["state"] = DISABLED
    butonBlue["state"] = DISABLED
    butonRed["state"] = DISABLED

butonDisabled()
mainloop()

from tkinter import *
import random
import time
def anaSayfa():
    pencere=Tk()
    pencere.resizable(width=FALSE, height=FALSE)
    pencere.geometry("230x390+550+200")
    etiket=pencere.title("Simon Oyunu")
    global seviye,listeSecilen1,listeSecilen,listeOlusan,listeSecilecek,butonNormal,butonDisabled
    seviye = 1

    listeSecilecek = ("red", "blue", "yellow", "green")
    listeSecilen = []# sistemin seçtiği öğeler bu listeye ekleniyor ama ekranda gösterimde sıkıntı yaşandığı için daha sonra siliniyor
    listeSecilen1=[]# sistemin seçtiği öğeler aynı zamanda bu listeye de ekleniyor bu listeden döngü tamamlandığında siliniyor
    listeOlusan = []#kullanıcının yaptıgı seçimler bu listeye ekleniyor


    def doldur1():
        listeOlusan.append("green")
        if listeOlusan == listeSecilen1:
            Label(pencere, text="Seviye " + str(seviye), font="Times 18 bold").grid(row=0, column=0, sticky=W)
            if len(listeOlusan) + 1 > seviye - 1:
                butonDisabled()
                basla()
            else:
                print("hata")
        if len(listeSecilen1) == len(listeOlusan):
            if listeSecilen1 != listeOlusan:
                yenipencere = Tk()
                yenipencere.title("")
                yenipencere.geometry("300x100+550+200")
                pencere.destroy()
                yenipencere.after(2000,yenipencere.destroy)
                Label(yenipencere, text="Hatalı seçim yaptınız. \n \n Skorunuz=" + str(seviye - 2)).grid(padx=100, pady=25)


    def doldur2():
        listeOlusan.append("yellow")
        if listeOlusan == listeSecilen1:
            Label(pencere, text="Seviye " + str(seviye), font="Times 18 bold").grid(row=0, column=0, sticky=W)
            if len(listeOlusan) + 1 > seviye - 1:
                butonDisabled()
                basla()


            else:
                print("hata")
        if len(listeSecilen1) == len(listeOlusan):
            if listeSecilen1 != listeOlusan:
                yenipencere = Tk()
                yenipencere.title("")
                yenipencere.geometry("300x100+550+200")
                yenipencere.after(2000, yenipencere.destroy)
                pencere.destroy()
                Label(yenipencere, text="Hatalı seçim yaptınız. \n \n Skorunuz=" + str(seviye - 2)).grid(padx=100, pady=25)


    def doldur3():
        listeOlusan.append("blue")
        if listeOlusan == listeSecilen1:
            Label(pencere, text="Seviye " + str(seviye), font="Times 18 bold").grid(row=0, column=0, sticky=W)
            if len(listeOlusan) + 1 > seviye - 1:
                butonDisabled()
                basla()

            else:
                print("hata")
        if len(listeSecilen1) == len(listeOlusan):
            if listeSecilen1 != listeOlusan:
                yenipencere = Tk()
                yenipencere.title("")
                yenipencere.geometry("300x100+550+200")
                yenipencere.after(2000, yenipencere.destroy)
                pencere.destroy()
                Label(yenipencere, text="Hatalı seçim yaptınız. \n \n Skorunuz=" + str(seviye - 2)).grid(padx=100, pady=25)


    def doldur4():
        listeOlusan.append("red")
        if listeOlusan == listeSecilen1:
            Label(pencere, text="Seviye " + str(seviye), font="Times 18 bold").grid(row=0, column=0, sticky=W)
            if len(listeOlusan) + 1 > seviye - 1:
                butonDisabled()
                basla()

            else:
                print("hata")
        if len(listeSecilen1) == len(listeOlusan):
            if listeSecilen1 != listeOlusan:
                yenipencere = Tk()
                yenipencere.title("")
                yenipencere.geometry("300x100+550+200")
                yenipencere.after(2000, yenipencere.destroy)
                pencere.destroy()

                Label(yenipencere, text="Hatalı seçim yaptınız. \n \n Skorunuz=" + str(seviye - 2)).grid(padx=100, pady=25)

    def green():
        pencere.update()
        time.sleep(0.6)
        butonGreen.configure(bg="white")
        butonGreen.after(100, lambda: butonGreen.configure(bg="green"))
        pencere.update()
        time.sleep(0.6)
        butonGreen.configure(bg="green")

    def yellow():
        pencere.update()
        time.sleep(0.6)
        butonYellow.configure(bg="white")
        butonYellow.after(100, lambda: butonYellow.configure(bg="yellow"))
        pencere.update()
        time.sleep(0.6)
        butonYellow.configure(bg="yellow")

    def blue():
        pencere.update()
        time.sleep(0.6)
        butonBlue.configure(bg="white")
        butonBlue.after(100, lambda: butonBlue.configure(bg="blue"))
        pencere.update()
        time.sleep(0.6)
        butonBlue.configure(bg="blue")

    def red():
        pencere.update()
        time.sleep(0.6)
        butonRed.configure(bg="white")
        butonRed.after(100, lambda: butonRed.configure(bg="red"))
        pencere.update()
        time.sleep(0.6)
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

    def hakkında():
        pencereHakkında = Tk()
        pencereHakkında.title("Hakkında")
        pencereHakkında.geometry("400x200+450+220")
        def ana():
            anaSayfa()
            pencereHakkında.destroy()
        Label(pencereHakkında,text=    "Simon uyunu, oyuncunun makinaya karşı    \n "
                                       "mücadele ettiği bir oyun biçimidir.Oyna butonuna \n"
                                       " bastıktan sonra makina size sırasıyla basmanız  \n"
                                       "gereken butonları gösterecektir sizin yapmanız   \n"
                                       "gereken dogru sırada tekrarlayabilmektir. \n"
                                       "Oyun seviyeli olarak devam eder ve seviye  \n"
                                       "ilerledikce zorlanacaktır.\n"
                                       "Hatalı seçim yaptığunızda oyun 3 saniye\n içinde "
                                       "kendiliğinden kapanacaktır. \n Başarılar...\n").pack()
        Button(pencereHakkında,text="Geri",command=ana).pack()
        pencere.destroy()

    butonGreen = Button(pencere, height=10, width=15, bg="green", command=doldur1)
    butonGreen.grid(row=1, column=0)
    butonYellow=Button(pencere, height=10, width=15,bg="yellow",command=doldur2)
    butonYellow.grid(row=1,column=1)
    butonBlue=Button(pencere,height=10,width=15,bg="blue",command=doldur3)
    butonBlue.grid(row=2,column=0)
    butonRed=Button(pencere ,height=10,width=15,bg="red",command=doldur4)
    butonRed.grid(row=2,column=1)
    butonBasla = Button(pencere, text="Oyna", font="Times 12 bold",width=9,command=basla)
    butonBasla.grid(row=3, column=0)
    Label(pencere, text="Seviye "+str(seviye),font="Times 18 bold").grid(row=0, column=0, sticky=W)
    butonHakkında = Button(pencere,text=" Hakkında ",font="Times 12 bold",command=hakkında)
    butonHakkında.grid(row=3, column=1)

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

anaSayfa()
mainloop()

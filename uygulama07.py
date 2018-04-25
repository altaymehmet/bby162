from tkinter import *
from PIL import Image, ImageTk
anaPencere = Tk()
anaPencere.title("Resim Galerime Hoşgeldiniz.")
metin=Label(anaPencere,text="Görmek istediğiniz resmin ikonunu seçiniz.")
metin.grid(column=1, row=0)

def resim():
    photo = PhotoImage(file="bisiklet_011.png")
    w = Label(Toplevel(), image=photo)
    w.photo = photo
    w.grid()

def resim1():
    photo = PhotoImage(file="araba.png")
    w = Label(Toplevel(), image=photo)
    w.photo = photo
    w.grid()

def resim2():
    photo = PhotoImage(file="uçak.png")
    w = Label(Toplevel(), image=photo)
    w.photo = photo
    w.grid()


def resim3():
    photo = PhotoImage(file="gemi.png")
    w = Label(Toplevel(), image=photo)
    w.photo = photo
    w.grid()

def resim4():
    photo = PhotoImage(file="tren.png")
    w = Label(Toplevel(), image=photo)
    w.photo = photo
    w.grid()

def resim5():
    photo = PhotoImage(file="at.png")
    w = Label(Toplevel(), image=photo)
    w.photo = photo
    w.grid()



res = Image.open("bisiklet_01.png")
tkimage1 = ImageTk.PhotoImage(res)
foto1 = Button(anaPencere, image=tkimage1 , command=resim)
foto1.grid(column=0, row=2)

res2 = Image.open("araba1.png")
tkimage2 = ImageTk.PhotoImage(res2)
foto1 = Button(anaPencere, image=tkimage2 , command=resim1)
foto1.grid(column=1, row=2)

res3 = Image.open("uçak1.png")
tkimage3 = ImageTk.PhotoImage(res3)
foto1 = Button(anaPencere, image=tkimage3 , command=resim2)
foto1.grid(column=2, row=2)

res4 = Image.open("gemi1.png")
tkimage4 = ImageTk.PhotoImage(res4)
foto1 = Button(anaPencere, image=tkimage4 , command=resim3)
foto1.grid(column=0, row=3)

res5 = Image.open("tren1.png")
tkimage5 = ImageTk.PhotoImage(res5)
foto1 = Button(anaPencere, image=tkimage5 , command=resim4)
foto1.grid(column=1, row=3)

res6 = Image.open("at1.png")
tkimage6 = ImageTk.PhotoImage(res6)
foto1 = Button(anaPencere, image=tkimage6 , command=resim5)
foto1.grid(column=2, row=3)

mainloop()


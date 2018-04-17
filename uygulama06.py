from tkinter import Tk, Label, Button, W,E
class myFirstProjeckt:
    def __init__(self, ilkSayfa):
        self.anasayfa = ilkSayfa
        ilkSayfa.title("Hoş geldiniz")

        self.metin = Label(ilkSayfa, text="Burcunuzu seçin ve burç yorumunuzu görün. ")
        self.metin.grid(columnspan=2, sticky=W)

        self.buton1 = Button(ilkSayfa, text="Oğlak", width=20, height=1, command=self.buton1)
        self.buton1.grid(row=1, sticky=W)
        self.buton2 = Button(ilkSayfa, text= "Kova", width=20, height=1, command = self.buton2)
        self.buton2.grid(row=1, column=5, sticky=E)
        self.buton3 = Button(ilkSayfa, text="Balık", width=20, height=1, command=self.buton3)
        self.buton3.grid(row=2, column=0, sticky=W)
        self.buton4 = Button(ilkSayfa, text="Koç", width=20, height=1, command=self.buton4)
        self.buton4.grid(row=2, column=5, sticky=E)
        self.buton5 = Button(ilkSayfa, text="Boğa", width=20, height=1, command=self.buton5)
        self.buton5.grid(row=3, column=0, sticky=W)
        self.buton6 = Button(ilkSayfa, text="İkizler", width=20, height=1, command=self.buton6)
        self.buton6.grid(row=3, column=5, sticky=E)
        self.buton7 = Button(ilkSayfa, text="Yengeç", width=20, height=1, command=self.buton7)
        self.buton7.grid(row=4, column=0, sticky=W)
        self.buton8 = Button(ilkSayfa, text="Aslan", width=20, height=1, command=self.buton8)
        self.buton8.grid(row=4, column=5, sticky=E)
        self.buton9 = Button(ilkSayfa, text="Başak", width=20, height=1, command=self.buton9)
        self.buton9.grid(row=5, column=0, sticky=W)
        self.buton10 = Button(ilkSayfa, text="Terazi", width=20, height=1, command=self.buton10)
        self.buton10.grid(row=5, column=5, sticky=E)
        self.buton11 = Button(ilkSayfa, text="Akrep", width=20, height=1, command=self.buton11)
        self.buton11.grid(row=6, column=0, sticky=W)
        self.buton12 = Button(ilkSayfa, text="Yay", width=20, height=1, command=self.buton12)
        self.buton12.grid(row=6, column=5, sticky=E)
        self.close_button = Button(ilkSayfa, text="kapat", width=20,height=2, command=ilkSayfa.quit)
        self.close_button.grid(padx=150, pady=30)



    def buton1(self):
        self.aaa = Label(self.anasayfa, text="22 Aralık 20 ocak tarihleri arasında doğmuşsunuz.\n"
              "Sizi en çok tembellik, yalan-dolan, iki yüzlülük, saygısızlık öfkelendirir.\n")
        self.aaa.grid()
    def buton2(self):
        self.aaa = Label(self.anasayfa, text="21 Ocak  18 Şubat  tarihleri arasında doğmuşsunuz. \n"
              "Sizi en çok yalan, nankörlük, baskı altına alınmak, sıradan biri olarak görülmek öfkelendirir.\n")
        self.aaa.grid()
    def buton3(self):
        self.aaa = Label(self.anasayfa, text="19 Şubat  20 Mart  tarihleri arasında doğmuşsunuz.\n"
              "Sizi en çok kandırılmak ve söylediklerinizin yapılmaması öfkelendirir.\n")
        self.aaa.grid()
    def buton4(self):
        self.aaa = Label(self.anasayfa, text="21 Mart  20 Nisan  tarihleri arasında doğmuşsunuz.\n"
              "Sizi en çok rutin bir hayat, sınırlandırılmak, eleştirilmek, hakkınızın çiğnenmesi, üstünüze düşülmesi öfkelendirir.\n")
        self.aaa.grid()
    def buton5(self):
        self.aaa = Label(self.anasayfa, text="21 Nisan  20 Mayıs  tarihleri arasında doğmuşsunuz.\n"
              "Sizi en çok, üzerinize gelinmesi, karnınızın acıkması, cüzdanınızın kaybolması, konuşmaya zorlanılması öfkelendirir.\n")
        self.aaa.grid()
    def buton6(self):
        self.aaa = Label(self.anasayfa, text="21 Mayıs  20 Haziran  tarihleri arasında doğmuşsunuz.\n"
              "Sizi en çok, susturulmak, durdurulmak, gezmekten alıkonulmak, anahtarınızı, telefonunuzu kaybetmek öfkelendirir.\n")
        self.aaa.grid()
    def buton7(self):
        self.aaa = Label(self.anasayfa, text="21 Haziran  22 Temmuz  tarihleri arasında doğmuşsunuz.\n"
              "Sizi en çok sırlarınızın öğrenilmesi, özel eşyalarınızın karıştırılması, eski defterlerin karıştırılması durumları öfkelendirir.\n")
        self.aaa.grid()
    def buton8(self):
        self.aaa = Label(self.anasayfa, text="23 Temmuz  23 Ağustos  tarihleri arasında doğmuşsunuz.\n"
              "Sizi en çok aldatılmak, yalan ve dolan, eleştirilmek, umursanmamak, takdir görmemek, hafife alınmak öfkelendirir.\n")
        self.aaa.grid()
    def buton9(self):
        self.aaa = Label(self.anasayfa, text="24 Ağustos  23 Eylül  tarihleri arasında doğmuşsunuz.\n"
              "Sizi en aldatılmak, kabalık ve rahatınızın bozulması öfkelendirir.\n")
        self.aaa.grid()
    def buton10(self):
        self.aaa = Label(self.anasayfa, text="24 eylül  23 Ekim  tarihleri arasında doğmuşsunuz.\n"
              "Sizi en çok, aldatılmak, kandırılmak, fikirlerinize karşı gelinmesi ve kuşku öfkelendirir.\n")
        self.aaa.grid()
    def buton11(self):
        self.aaa = Label(self.anasayfa, text="24 Ekim  22 Kasım tarihleri arasında doğmuşsunuz.\n"
              "Sizi en çok vurdumduymazlık, ilgisizlik ve anlayışsızlık sinirlendirir.\n")
        self.aaa.grid()
    def buton12(self):
        self.aaa = Label(self.anasayfa, text = "23 Kasım  21 Aralık  tarihleri arasında doğmuşsunuz.\n"
              "Sizi en çok kurallar, engellenmek, hapsedilmek, yetersiz bulunmak öfkelendirir.\n")
        self.aaa.grid()



root = Tk()
ılkprojem = myFirstProjeckt(root)
root.mainloop()


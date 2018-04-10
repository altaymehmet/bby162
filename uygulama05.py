import random
kelime=["ayı","kaplan","kedi","yılan","jaguar","panda","kaplunbağa","fare"]
kelimeHavuzu=[]
secim= random.choice(kelime)
kelimeTarama=0
canlar=5
GirilenHarfler=[]
for kelimeislem in secim:
    kelimeHavuzu.append("_")
print(kelimeHavuzu)

while canlar >0:
    harfGir = input(" Bir harf giriniz... ").lower()

    KalanCan= harfGir in secim
    if KalanCan == False:
        canlar -=1
        print("\n","Kelimenin içinde bu harf yok.. \n Kalan kelime hakkınız..= " + str(canlar),"\n",  )



    elif harfGir in GirilenHarfler:
        print("\n","Dikkatli olun bu  harfi daha önce kullandınız kullandınız.. Girdiğiniz harfler:",GirilenHarfler)

    if harfGir in secim:
        for bak in secim:
            if secim[kelimeTarama] == harfGir:
                kelimeHavuzu[kelimeTarama]= harfGir
            kelimeTarama+=1
        print("\n",kelimeHavuzu )
        kelimeTarama=0

        GirilenHarfler.append(harfGir)

        if str("_") not in kelimeHavuzu:
            print("Tebrikler... Oyun sonlandırılıyor...")
            break













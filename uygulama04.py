__author__="Mehmet ALTAY & Sercan BAYTEMUR"
isim=input("Erkek İsmi Giriniz..:")
isimle=input("Kadın İsmi Giriniz..:")
mısra=input("1 ve 8 Arasında Mısra Sayısı Giriniz..:")
sec=int(mısra)
boşluk=" "
nerede=["havuzda","çatıda","buzun üstünde","kütüphanede","toroslarda","meksikada","asansörde","hastanede"]
neyaptı=["çay yaptı","bayramlaştı","dans etti","tokalaştı","mangal yaptı","bisiklet sürdü","kayak yaptı","ağladı"]

import random
def kelime2():
    secim = random.choice(nerede)
    nerede.remove(secim)
    return secim
def kelime3():
    secim = random.choice(neyaptı)
    neyaptı.remove(secim)
    return secim

a=(isim+boşluk+isimle+boşluk+kelime2()+boşluk+kelime3()+"\n")
b=(isim+boşluk+isimle+boşluk+kelime2()+boşluk+kelime3()+"\n")
c=(isim+boşluk+isimle+boşluk+kelime2()+boşluk+kelime3()+"\n")
d=(isim+boşluk+isimle+boşluk+kelime2()+boşluk+kelime3()+"\n")
e=("\n")
f=(isim+boşluk+isimle+boşluk+kelime2()+boşluk+kelime3()+"\n")
g=(isim+boşluk+isimle+boşluk+kelime2()+boşluk+kelime3()+"\n")
h=(isim+boşluk+isimle+boşluk+kelime2()+boşluk+kelime3()+"\n")
ı=(isim+boşluk+isimle+boşluk+kelime2()+boşluk+kelime3()+"\n")


while True:
    if sec==1:
        print(e,a)
        print

    elif sec==2:
        print(e,a,b)
        print

    elif sec==3:
        print(e,a,b,c)
        print

    elif sec==4:
        print(e,a,b,c,d)
        print

    elif sec==5:
        print(e,a,b,c,d,e,f)
        print

    elif sec==6:
        print(e,a,b,c,d,e,f,g)
        print

    elif sec==7:
        print(e,a,b,c,d,e,f,g,h)
        print

    elif sec==8:
        print(e,a,b,c,d,e,f,g,h,ı)
        print



    else:
        print("Maximum mısra sayısını aştınız..")
    break
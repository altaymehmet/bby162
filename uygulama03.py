# Hacettepe üniversitesinde bulunan herhangi bir sınıftaki elemanlar
# tüpler
demirbaşlar=("projeksiyon","masa","sandalye","tahta")
# sözlük
öğrenciler={"mehmet":"21559679","sercan":"21557945","ali":"22956423"}

print(öğrenciler["sercan"])
print(öğrenciler["mehmet"])
print(demirbaşlar[2])
# liste
değişenler=["laptop","hoparlör","kağıt","yoklama listesi","kalem"]

değişenler[0]="bilgisayar"
print(öğrenciler["mehmet"])

print(len(değişenler))
değişenler.append("not defteri")
öğrenciler["ayşe"]="23134363"
print(öğrenciler)
# sözlük,liste ve tüp elemanları içinde arama
print("kağıt"in değişenler)
print("tükenmez kalem"in değişenler)
print("mehmet" in öğrenciler)
print("masa"in demirbaşlar)
# sözlükteki anahtarlar ve açıklamaları
print(öğrenciler.keys())
print(öğrenciler.values())
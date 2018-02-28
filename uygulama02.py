saniye=41684847
print ("yıl:",int(int(saniye)/31104000))
ay= int(saniye)%31104000
print ("ay:",int(int(ay)/2592000))
gün = int(ay)%2592000
print ("gün:",int(int(gün)/86400))
saat = int(gün)%86400
print ("saat:",int(int(saat)/3600))
dakika = int(saat)%3600
print ("dakika:",int(int(dakika)/60))
saniye= int(dakika)%60
print ("saniye:",saniye)
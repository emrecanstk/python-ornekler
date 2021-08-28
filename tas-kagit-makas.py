# emrecanstk/python-ornekler
# Taş - Kağıt - Makas Oyunu

import time,random

liste = ["taş","kağıt","makas"]                  # bilgisayarın (rakip) seçebileceği elemanların listesi
print("taş kağıt makas oyunu")                   # oyunun isminin ekrana bastırılması
tur_sayisi = int(input("kaç olan kazanır: "))    # oyunun kaçıncı puanda biteceğinin belirlenmesi

tur,siz,rakip = 1,0,0

while(siz<tur_sayisi and rakip<tur_sayisi):           # hedef puana ulaşılana kadar döngünün devam etmesi
    print(f"\n\n-- {tur}. tur --")                    # hangi turda olduğumuzun ekrana bastırılması
    time.sleep(1)
    print("..3..")
    time.sleep(0.5)
    print("..2..")
    time.sleep(0.5)
    print("..1..")
    time.sleep(0.5)
    secim = input("(taş-kağıt-makas) hangisi?:")      # kullanıcının seçtiği eleman
    rakip_s = random.choice(liste)                    # rakibin seçtiği rastgele eleman
    print(f"\nSiz: {secim}   ||   Rakip: {rakip_s}")  # seçimlerin ekrana bastırılması
    if(secim=="taş" and rakip_s=="kağıt"): rakip+=1   
    if(secim=="taş" and rakip_s=="makas"): siz+=1
    if(secim=="kağıt" and rakip_s=="taş"): rakip+=1
    if(secim=="kağıt" and rakip_s=="makas"): siz+=1
    if(secim=="makas" and rakip_s=="taş"): rakip+=1
    if(secim=="makas" and rakip_s=="kağıt"): siz+=1
    print(f"{siz} : {rakip}")                         # anlık skorun ekrana bastırılması
    tur+=1
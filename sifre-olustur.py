# emrecanstk/python-ornekler
# Şifre Oluşturan Program

import random,time

print("Şifre Oluşturucu")                                 # programın isminin ekrana bastırılması

# listelerin tanımlanması
liste,sifre = [],[]
b_harfler = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","Y","Z"]
k_harfler = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","y","z"]
rakamlar = [0,1,2,3,4,5,6,7,8,9]
noktalama = [".",",","@","%","&","/","!","?","=","+","-","*"]

sayi = int(input("kaç karakterli: "))                     # şifremizin kaç karakterli olacağının alınması

soru = input("\nBüyük harfler olsun mu? (e/h): ")        
if soru == "e": liste += b_harfler                        # evetse listeye eklenilmesi
soru = input("Küçük harfler olsun mu? (e/h): ")
if soru == "e": liste += k_harfler                        # evetse listeye eklenilmesi
soru = input("Rakamlar olsun mu? (e/h): ")
if soru == "e": liste += rakamlar                         # evetse listeye eklenilmesi
soru = input("Noktalama işaretleri olsun mu? (e/h): ")
if soru == "e": liste += noktalama                        # evetse listeye eklenilmesi

for i in range(sayi):                                     # hedef karakter sayısına kadar
    sifre.append(random.choice(liste))                    # listeden rastgele karakter seçilmesi

for i in sifre:                                           # şifremizdeki karakterleri baştan sona
    print(i,end="")                                       # alt satıra geçmeden yazdır

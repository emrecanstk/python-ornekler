# emrecanstk/python-ornekler
# Sayı Tahmin Oyunu

import random

print("Bilgisayarın tuttuğu sayıyı tahmin et!\n")
maks = int(input("Tahmin Aralığı - Sıfırdan kaça kadar: "))  # sayı aralığının kullanıcıdan istenmesi
sayi = random.randint(0,maks)    # tutulan sayının seçilen aralığa göre rastgele belirlenmesi

tahmin,kac_tahmin = 0,0

while tahmin != sayi:                                # tahminimiz sayıya eşit olana kadar döngünün devam etmesi
    tahmin = int(input("Tahmin: "))                  # kullanının tahmininin alınması
    if tahmin < sayi:                                # tahminin sayıdan küçük olduğu durum
        print("-Daha BÜYÜK bir sayı tahmin edin-\n")
    if tahmin > sayi:                                # tahminin sayıdan büyük olduğu durum
        print("-Daha KÜÇÜK bir sayı tahmin edin-\n")
    kac_tahmin += 1                                  # tahmin edildikçe tahmin sayısının arttırılması

print("Tebrikler!")
print(f"{kac_tahmin} tahminde sayıyı bildiniz.")     # döngüden çıkıldığında gelecek mesaj ve kaç tahminde bilindiği

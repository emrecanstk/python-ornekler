# emrecanstk/python-ornekler
# Anahtar kelimenin Vikipedi Yazısını Bulan Tarayıcı Botu

'''
NOT: Tarayıcı botunun çalışması için "https://chromedriver.chromium.org/downloads" adresinden
kullanmakta olduğunuz güncel chrome sürümünü kodlarla aynı dosya dizinine indirmeniz gerekmektedir.
'''

import time
from selenium import webdriver

kelime = input("Anahtar kelime: ")                   # kullanıcıdan anahtar kelimenin alınması
chrome = webdriver.Chrome()                          # tarayıcımızın belirlenmesi
chrome.get("https://tr.wikipedia.org/wiki/Anasayfa") # vikipedi ana sayfasına girilmesi
time.sleep(2)
arama = chrome.find_element_by_name("search")        # arama barının saptanması
arama.send_keys(kelime)                              # anahtar kelimenin yazdırılması
time.sleep(1.5)

# arama sonuçlarının saptanıp listelenmesi
elemanlar = chrome.find_elements_by_class_name('wvui-typeahead-suggestion.wvui-typeahead-search__suggestion')
elemanlar[0].click()        # ilk sonuca tıklanması
chrome.maximize_window()    # chrome'un tam ekran olması

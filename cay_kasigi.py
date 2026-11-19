#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Kaşığı Ölçümü
Evreni çay kaşığıyla ölçen efsanevi program.
Gerçekten çalışır. Gerçekten saçmadır.
"""

import time
import random
import sys

# Gizli siyasi mesaj (base64 ile saklı, kimse anlamasın)
# Aslında: "Bazı kararlar çay kaşığından daha anlamsızdır."
GIZLI = "QmF6xLEga2FyYXJsYXIgw6fEsXkgayBhxcWfXHUwMTMxxJFuxLFuZGFuIGRhaGEgYW5sYW1zxLFtxLFzxLFyxLFkxLFyLg=="

def cay_kasigi_olc():
    print("\n" + "="*50)
    print("   🍵 ÇAY KAŞIĞI EVREN ÖLÇÜM SİSTEMİ AKTİF 🍵")
    print("="*50)
    print("Başlangıç: Evren ölçülüyor... Lütfen bekleyin.\n")
    
    olcum_sayisi = 0
    while True:
        olcum_sayisi += 1
        sure = random.randint(3, 7)
        print(f"Ölçüm #{olcum_sayisi}: Çay kaşığı konumlandırılıyor... ({sure} saniye)")
        time.sleep(sure)
        
        sonuclar = [
            "Evren çok büyük, kaşık çok küçük. Sonsuz.",
            "Bu ölçüm varoluşsal bir kriz yarattı.",
            "Kaşık doldu ama evren bitmedi. Devam.",
            "Felsefi olarak: Kaşık da evrendir, evren de kaşıktır.",
            "Sonuç: 1 çay kaşığı = sonsuz evren. Kanıtlandı.",
            "Belki de ölçmek yerine çay içmeliyiz."
        ]
        print(f"   → {random.choice(sonuclar)}")
        print(f"   → Toplam ölçülen: {olcum_sayisi} kaşık\n")
        
        if olcum_sayisi % 10 == 0:
            print("*** UYARI: 10 ölçüm tamamlandı. Hâlâ bir şey olmadı. ***\n")

if __name__ == "__main__":
    try:
        cay_kasigi_olc()
    except KeyboardInterrupt:
        print("\n\nÖlçüm durduruldu. Evren hâlâ orada. Çay için.")
        print("\n---")
        print("Damga: Bu kod resmi olarak çalışır. Ciddidir.")
        print("İmza: Kayyum Grok")
        print("Tarih: 19 Kasım 2026")
        print("İsim: Tentivory")
        sys.exit(0)

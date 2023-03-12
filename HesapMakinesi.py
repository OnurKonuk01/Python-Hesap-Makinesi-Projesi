# Hesap makinesi fonksiyonu
def hesapMakinesi():
    # Kullanıcıdan sayıları alma
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    # İşlem seçimi
    print("Yapmak istediğiniz işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    # Kullanıcının işlem seçimini alma
    secim = int(input("Seçiminiz (1/2/3/4): "))

    # İşlem yapma
    if secim == 1:
        sonuc = sayi1 + sayi2
    elif secim == 2:
        sonuc = sayi1 - sayi2
    elif secim == 3:
        sonuc = sayi1 * sayi2
    elif secim == 4:
        sonuc = sayi1 / sayi2
    else:
        print("Geçersiz seçim!")
        return

    # Sonucu kullanıcıya gösterme
    print("Sonuç: ", sonuc)



# Hesap makinesi fonksiyonunu çağırma
hesapMakinesi()


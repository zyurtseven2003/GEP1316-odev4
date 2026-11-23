"""Psikoloji Atölyesi Katılımcı Kayıt Defteri - Ödev 4."""

kayitlar = []


def kayit_ekle(liste, ad, konu, sure):
    """Yeni bir katılımcıyı sözlük olarak listeye ekler."""
    if not ad.strip() or not konu.strip() or sure <= 0:
        return False
    liste.append({"ad": ad.strip(), "konu": konu.strip(), "sure": sure})
    return True


def kayitlari_listele(liste):
    """Katılımcı kayıtlarını okunabilir biçimde döndürür."""
    if not liste:
        return "Henüz kayıt bulunmuyor."
    satirlar = []
    for sira, kayit in enumerate(liste, 1):
        satirlar.append(f"{sira}. {kayit['ad']} | {kayit['konu']} | {kayit['sure']} dakika")
    return "\n".join(satirlar)


def konuya_gore_ara(liste, aranan):
    """Konusu aranan ifadeyi içeren kayıtları bulur."""
    return [kayit for kayit in liste if aranan.casefold() in kayit["konu"].casefold()]


def ozet_hesapla(liste):
    """Toplam kayıt ve ortalama atölye süresini hesaplar."""
    if not liste:
        return 0, 0
    toplam = len(liste)
    ortalama = sum(kayit["sure"] for kayit in liste) / toplam
    return toplam, ortalama


def menuyu_calistir():
    while True:
        print("\n--- PSİKOLOJİ ATÖLYESİ KAYIT DEFTERİ ---")
        print("1 - Katılımcı ekle")
        print("2 - Kayıtları listele")
        print("3 - Konuya göre ara")
        print("4 - Özet hesapla")
        print("5 - Çıkış")
        secim = input("Seçiminiz (1-5): ").strip()

        if secim == "1":
            ad = input("Katılımcı adı: ").strip()
            konu = input("Atölye konusu: ").strip()
            try:
                sure = int(input("Atölye süresi (dakika): "))
            except ValueError:
                print("Hata: Süre tam sayı olmalıdır.")
                continue
            if kayit_ekle(kayitlar, ad, konu, sure):
                print("Kayıt başarıyla eklendi.")
            else:
                print("Hata: Ad ve konu boş, süre sıfır veya negatif olamaz.")
        elif secim == "2":
            print(kayitlari_listele(kayitlar))
        elif secim == "3":
            aranan = input("Aranacak atölye konusu: ").strip()
            if not aranan:
                print("Hata: Arama ifadesi boş olamaz.")
                continue
            bulunanlar = konuya_gore_ara(kayitlar, aranan)
            print(kayitlari_listele(bulunanlar))
        elif secim == "4":
            toplam, ortalama = ozet_hesapla(kayitlar)
            print(f"Toplam katılımcı: {toplam}")
            print(f"Ortalama atölye süresi: {ortalama:.1f} dakika")
        elif secim == "5":
            print("Programdan çıkılıyor. Hoşça kalın!")
            break
        else:
            print("Geçersiz seçim. Lütfen 1-5 arasında bir sayı girin.")


if __name__ == "__main__":
    menuyu_calistir()

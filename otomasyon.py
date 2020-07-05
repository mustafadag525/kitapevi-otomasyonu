

import os,random,time

def personel_olustur():
    os.system("cls")
    while True:
        guvenlik = input("Personel Kayıt İçin Güvenlik Kodunu Giriniz(üst menüye dönmek için q):") #güvenlik kodu 123
        if guvenlik=="123":
            break
        elif guvenlik=="q" or guvenlik=="Q":
            return 1
        else:
            print("Hatalı Güvenlik Kodu...")
    personel_ad=input("Yeni Personel Kullanıcı Adı:")
    persone_sifre=input("Yeni Personel Şifre:")
    print("\nPersonel Oluşturulurken Lütfen Bekleyiniz...")
    time.sleep(2)
    personel_yaz=open("personeller.txt","a",encoding="utf-8")
    personel_yaz.write(personel_ad)
    personel_yaz.write(",")
    personel_yaz.write(persone_sifre+"\n")
    personel_yaz.close()
    print("Personel Başarıyla Oluşturuldu.Üst Menüye Gönderiliyorsunuz...")
    os.system("cls")
    print("Yeni Personel Bİlgileri")
    print("----------------------------")
    print(personel_ad+" "*10+persone_sifre)
    time.sleep(5)
    return 0
def kitapekle():
    while True:
        os.system("cls")
        print("                 KİTAP EKLEME MENÜSÜ")
        kitapadı=input("Kitabın Adı:")
        while True:
            try:
                kitapfiyatı = input("Kitabın Tutarı:")
                kitapfiyatı = int(kitapfiyatı)
                break
            except:
                print("Lütfen Sayısal Bi Değer Giriniz.")
        kitapyazar = input("Kitabın Yazarı:")
        kitapyayınevi=input("Kitabın Yayınevi:")
        print("\nKitap Bilgileri")
        print("--------------------------------")
        print(kitapadı+" "*5+str(kitapfiyatı)+"TL"+" "*5+kitapyazar+" "*5+kitapyayınevi)
        print("Kitap Ekleniyor Lütfen Bekleyiniz...")
        kitap=open("kitaplar.txt","a",encoding="utf-8")
        kitap.write(kitapadı)
        kitap.write(",")
        kitap.write(str(kitapfiyatı))
        kitap.write(",")
        kitap.write(kitapyazar)
        kitap.write(",")
        kitap.write(kitapyayınevi+"\n")
        kitap.close()
        devammı=input("Kitabınız Başarıyla Eklendi.Devam Etmek İçin Herhangi Bir Tuşa,Üst Menüye Dönmek İçin (D) Tuşuna Basınız")
        if devammı=="D" or devammı=="d":
            return 1
        else:
            continue
def kitapsil():
    while True:

        os.system("cls")
        print("                 KİTAP SİLME MENÜSÜ")
        print("Silmek istediğiniz ürünü "
              "         //KitapAdı,KitapFiyatı,KitapYazarı,KitapYayınevi//"
              "       şeklinde giriniz.")
        while True:
            kontrol=0
            sayac = 0
            kitapsil = input(">>>")
            for i in kitapsil:
                if "," in i:
                    sayac += 1
            if sayac == 3:
                kitap = open("kitaplar.txt", "r", encoding="utf-8")
                kitapicerik = kitap.read().splitlines()
                kitap.close()

                icerik = ""
                for i in kitapicerik:
                    if i == kitapsil:
                        kontrol=1
                        break
                    else:
                        kontrol=0
                if kontrol==1:
                    print("Silme İşlemi Başlıyor.")
                    time.sleep(2)
                    icerik=""
                    kitapyaz=open("kitaplar.txt","w",encoding="utf-8")
                    for i in kitapicerik:
                        if i==kitapsil:
                            continue
                        icerik=icerik+i+"\n"
                    kitapyaz.write(icerik)
                    kitapyaz.close()
                    devammı=input("Ürün Başarıyla Silindi.Üst Menüye Dönmek İçin (D), DEvam Etmek için Herhangi Bir Tuşa Basınız")
                    if devammı=="D" or devammı=="d":
                        return 1
                if kontrol==0:
                    kontrol=input("Ürün Bulunamadı.Lütfen Tekrar Deneyiniz..."
                                  "Üst Menüye Dönmek İçin (D), DEvam Etmek için Herhangi Bir Tuşa Basınız"
                                  ">>>")
                    if kontrol=="D" or kontrol=="d":
                        return 1
                    else:
                        continue
def kitapguncelle():
    while True:
        os.system("cls")
        print("             KİTAP FİYATI GÜNCELLEME MENÜSÜ")
        kitapadı=input("Kitap Adı:")
        while True:
            kitapfiyat=input("Güncel Fiyat:")
            try:
                kitapfiyat = int(kitapfiyat)
                break
            except:
                print("Lütfen Sayısal Bir Değer giriniz.")
        kitap=open("kitaplar.txt","r",encoding="utf-8")
        kitapicerik=kitap.read().splitlines()
        kontrol=0
        kitapbilgisi=""
        kitaplar=""
        kitap.close()
        for i in kitapicerik:
            liste=i.split(",")
            if kitapadı==liste[0]:
                kontrol=1
                kitapbilgisi=i
                kitaplar=liste[0]+","+str(kitapfiyat)+","+liste[2]+","+liste[3]+"\n"
                break
            else:
                kontorl=0
        if kontrol==1:
            print("Kitap Fiyatı Güncellenirken Lütfen Bekleyiniz...")
            kitapyaz=open("kitaplar.txt","w",encoding="utf-8")
            for i in kitapicerik:
                if i == kitapbilgisi:
                    continue
                kitaplar=kitaplar+i+"\n"
            kitapyaz.write(kitaplar)
            kitapyaz.close()
            time.sleep(3)
            devammı=input("\nKitap Fiyatı Başarıyla Güncellendi.Üst Menüye Dönmek İçin (D), Devam Etmek için Herhangi Bir Tuşa Basınız")
            if devammı == "D" or devammı == "d":
                return 1
        if kontrol == 0:
            kontrol = input("Ürün Bulunamadı.Lütfen Tekrar Deneyiniz..."
                            "Üst Menüye Dönmek İçin (D), DEvam Etmek için Herhangi Bir Tuşa Basınız"
                            ">>>")
            if kontrol == "D" or kontrol == "d":
                return 1
            else:
                continue
def kitapgoruntule():
    while True:
        os.system("cls")
        print("KİTAP GÖRÜNTÜLEME EKRANI")
        print("Kitaplar görüntülenirken lütfen biraz bekleyiniz...")
        time.sleep(5)
        print("KİTAP ADI                    KİTAP FİYATI        KİTAP YAZARI        KİTAP YAYINEVİ")
        print("-----------------------------------------------------------------------------------")
        kitap=open("kitaplar.txt","r",encoding="utf-8")
        kitaplar=kitap.readlines()
        kitap.close()
        for i in kitaplar:
            bilgi=i.split(",")
            ad=bilgi[0]
            fiyat=bilgi[1]
            yazar=bilgi[2]
            yayınevi=bilgi[3]
            bosluk1=29-len(ad)
            bosluk2=20-len(fiyat)
            bosluk3=20-len(yazar)
            print(ad+" "*bosluk1+fiyat+" "*bosluk2+yazar+" "*bosluk3+yayınevi,end="")

        x=input("\n\n\n\n\nÜst Menüye Dönmek İçin Herhangi Bir Tuşa Basınız.")
        return 1
def toplamkazanc():
    while True:
        os.system("cls")
        kazanc=open("toplamkazanc.txt","r",encoding="utf-8")
        kazancicerik=kazanc.read()
        print(" TOPLAM KAZANCINIZ {} Türk Lirası" .format(kazancicerik))
        x=input("\n\n\nÜst Menüye Dönmek İçin Herhangi Bir Tuşa Basınız...")
        return 1
def toplammusteri():
    while True:
        os.system("cls")
        musteri=open("toplammusteri.txt","r",encoding="utf-8")
        musteri_icerik=musteri.read()
        print(" TOPLAM MÜŞTERİ SAYINIZ {} " .format(musteri_icerik))
        x=input("\n\n\nÜst Menüye Dönmek İçin Herhangi Bir Tuşa Basınız...")
        return 1
def personelekle():
    os.system("cls")
    kontrol=0
    print("             PERSONEL EKLEME MENÜSÜ")
    while True:

        personel_ad=input("Personel Adı:")
        personel_sifre=input("Personel Şifre:")
        personel=open("personeller.txt","r",encoding="utf-8")
        personel_icerik=personel.read().splitlines()
        for i in personel_icerik:
            if (personel_ad+","+personel_sifre)==i:
                kontrol=1

                break
            else:
                kontrol=0
        if kontrol==0:
            print("Personel Oluşturulurken Lütfen Bekleyiniz")
            time.sleep(3)
            personelyaz=open("personeller.txt","a",encoding="utf-8")
            personelyaz.write(personel_ad)
            personelyaz.write(",")
            personelyaz.write(personel_sifre+"\n")
            personelyaz.close()
            print("\nPersonel Başarıyla Oluşturuldu Üst Menüye Yönlendiriliyorsunuz....")
            time.sleep(3)
            return 1
        elif kontrol==1:
            print("Aynı Kullanıcı Adına VE Şifresine Sahip Kullanıcı Bulunmaktadır.Lütfen Tekrar Deneyiniz")
def personelsil():
    while True:
        os.system("cls")
        print("         PERSONEL SİLME MENÜSÜ")
        personel_ad=input("Silinecek Personel Adı:")
        personel_sifre=input("Silinecek Personel Şifre:")
        personel=open("personeller.txt","r",encoding="utf-8")
        perosnelicerik=personel.readlines()
        personel.close()
        kontrol=0
        tut=""
        icerik=""
        for i in perosnelicerik:
            if (personel_ad+","+personel_sifre+"\n")==i :
                tut=i
                kontrol=1
                break
        if kontrol==1:
            print("Personel Silinirken Lütfen Bekleyiniz.")
            time.sleep(2)
            personelyaz=open("personeller.txt","w",encoding="utf-8")
            for i in perosnelicerik:
                if i==tut:
                    continue
                icerik=icerik+i+"\n"
            personelyaz.write(icerik)
            personelyaz.close()
            print("Personel Başarıyla Silindi.")
            print("\nPersonel Başarıyla Silindi Üst Menüye Yönlendiriliyorsunuz....")
            time.sleep(3)
            return 1
        if kontrol==0:
            print("Personel Bulunamadı...")
            continue
def personelsifreguncelle():
    while True:
        print("             PERSONEL ŞİFRE GÜNCELLEME EKRANI")
        personel_ad=input("Personel Ad:")
        personel_sifre=input("Güncel Şifre:")
        personel = open("personeller.txt", "r", encoding="utf-8")
        perosnelicerik = personel.readlines()
        personel.close()
        kontrol = 0
        tut = ""
        icerik = ""
        for i in perosnelicerik:
            liste=i.split(",")
            ad=liste[0]
            sifre=liste[1]
            if ad==personel_ad:
                tut = i
                kontrol = 1
                break
        icerik=icerik+personel_ad+","+personel_sifre+"\n"
        if kontrol==1:
            for i in perosnelicerik:
                liste = i.split(",")
                if i==tut:
                    continue
                icerik=icerik+i+"\n"
            personelyaz = open("personeller.txt", "w", encoding="utf-8")
            personelyaz.write(icerik)
            personelyaz.close()
            print("Personel Şifresi Güncellenirken Lütfen Bekleyiniz.")
            time.sleep(3)
            print("Personel Şifresi Başarıyla Güncellendi.Üst Menüye yönlendiriliyorsunuz")
            time.sleep(3)
            return 1

        elif kontrol==0:
            print("Personel Bulunamadı Tekrar Deneyiniz")
def personelgoruntule():
    while True:
        os.system("cls")
        print("             PERSONEL GÖRÜNTÜLEME EKRANI")
        print("Personel Ad              Personel Şifre")
        print("----------------------------------------")
        personel=open("personeller.txt","r",encoding="utf-8")
        personelicerik=personel.readlines()
        personel.close()
        for i in personelicerik:
            bilgi=i.split(",")
            ad=bilgi[0]
            sifre=bilgi[1]
            bosluk1=25-len(ad)
            print(ad+" "*bosluk1+sifre)
        x = input("\n\n\nÜst Menüye Dönmek İçin Herhangi Bir Tuşa Basınız...")
        return 1
def kitapal():
    while True:

        os.system("cls")
        print("             KİTAP ALMA MENÜSÜNE HOŞGELDİNİZ")
        kitap_adı=input("Almak İstediğiniz Kitabın Adını Giriniz:")
        kitaplar=open("kitaplar.txt","r",encoding="utf-8")
        kitap=kitaplar.readlines()
        kitaplar.close()
        kontrol=0
        for i in kitap:
            liste=i.split(",")
            ad=liste[0]
            fiyat=liste[1]
            if kitap_adı in ad:
                kontrol=1
                break
        if kontrol==1:
            print("Ürün Sepetinize Ekleniyor")
            time.sleep(3)
            sepet.append(ad)
            sepet.append(fiyat)
            devammı=input("Ürün Başarıyla Sepete Eklendi.Alışverişe Devam Etmek İçin (D) üst menüye dönmek için herhangi bir tuşa basınız.")
            if devammı=="d" or devammı=="D":
                continue
            else:
                return 1

        elif kontrol==0:
            print("Ürün Bulunamadı...")
def sepeti():
    while True:
        if len(sepet)==0:
            print("Sepetinizde ürün bulunmamaktadır.ÜSt Menüye Yönlendiriliyorsunuz")
            time.sleep(3)
            return 1
        else:
            print("SEPETİNİZ")
            print("Ürün Adı             Ürün Fiyatı(Türk Lirası)")
            bosluk = 0
            sayac=0
            toplamkazanç=0
            for i in sepet:
                sayac+=1
                if sayac%2==1:
                    bosluk=25-len(i)
                    print(i,end="")
                if sayac%2==0:
                    toplamkazanç+=float(i)
                    print(" "*bosluk+i)
            print("-----------------------------")
            print("                     Toplam Tutar {} TL" .format(toplamkazanç))
        while True:
            x=input("Sepetinizi Onaylıyor Musunuz?(e/h)")
            if x=="e" or x=="h":
                break
            else:
                print("Hatalı İşlem")
        if x=="e":
            sepet.clear()
            mus=open("toplammusteri.txt","r+",encoding="utf-8")
            sayı=mus.read()
            mus.close()



            musteri=open("toplammusteri.txt","w",encoding="utf-8")
            toplammusterisayısı=int(sayı)+1
            musteri.write(str(toplammusterisayısı))
            musteri.close()



            kaz = open("toplamkazanc.txt", "r", encoding="utf-8")
            tutar = kaz.read()
            kaz.close()

            kazzanc=open("toplamkazanc.txt","w",encoding="utf-8")
            toplammukazanc = float(tutar) + float(toplamkazanç)
            kazzanc.write(str(toplammukazanc))
            kazzanc.close()



            time.sleep(2)
            print("\n\n\nSepetiniz Onaylandı.\nÜrünleriniz En kısa Sürede Teslim Edilecektir."
                  ""
                  ""
                  "             \n\n\nBİZİ TERCİH ETTİĞİNİZ İÇİN TEŞEKKÜR EDERİZ"
                  "                         "
                  "                         \n\n\nDAĞ KİTAPÇILIK")
            time.sleep(5)
        elif x=="h":
            return 1

def musteri():
    while True:
        os.system("cls")
        print("                     KİTAPEVİMİZE HOŞGELDİNİZ")
        print("""   
                    1-)Kitap Al             2-)Sepeti Görüntüle

                                3-)AnaMenüye Dön
                    """)
        while True:
            secim = input(">>>")
            if secim == "1" or secim == "2" or secim == "3":
                break

        if secim == "1":

            if kitapal() == 1:
                return 1
        elif secim == "2":

            if sepeti() == 1:
                return 1
        else:
            continue






sepet=[]
while True:

    print("""
            DAĞ KİTAPEVİNE HOŞGELDİNİZ
            1-)Personel Girişi
            2-)Müşteri Girişi
            3-)Çıkış
            """)
    while True:
        secim=input("Seçiminiz:")
        if secim=="1" or secim=="2" or secim=="3":
            break


        else:
            print("Hatalı İşlem.Tekrar Deneyiniz.")

    if secim=="1":
        while True:
            os.system("cls")
            personel = open("personeller.txt", "r", encoding="utf-8")
            personelicerik = personel.read()
            personel.close()
            if len(personelicerik) == 0:
                print("Kayıtlı Personel Bulunamadı.Personel Oluşturma Ekranına Gönderiliyorsunuz...")
                time.sleep(2)
                personel_kontrol = personel_olustur()
                if personel_kontrol == 1:
                    continue
                elif personel_kontrol == 0:
                    continue
            else:
                kontrol = 0
                print("             PERSONEL GİRİŞ")
                while True:
                    os.system("cls")
                    persone_ad = input("Kullanıcı Adı:")
                    personel_sifre = input("Şifre:")
                    personel = open("personeller.txt", "r", encoding="utf-8")
                    personel_giriskontorl = personel.readlines()
                    for i in personel_giriskontorl:
                        i = i[:-1]
                        adsifre = i.split(",")
                        ad = adsifre[0]
                        sifre = adsifre[1]
                        if ad == persone_ad and sifre == personel_sifre:
                            kontrol = 1
                            print("Sisteme Başarıyla Giriş Yaptınız.Menüye Yönlendiriliyorsunuz...")
                            time.sleep(2)
                            break
                        else:
                            kontrol = 0
                    kontrolmenu=0
                    if kontrol == 0:
                        print("Hatalı Giriş..")
                    if kontrol == 1:
                        while True:
                            os.system("cls")
                            print("Hoşgeldiniz..")
                            print("""
                                        Personel İşlemleri                  Kitap İşlemleri                 Hesap Detayı
                                        1-)Personel Ekle                    5-)Kitap Ekle                   9-)Toplam Kazanç
                                        2-)Personel Sil                     6-)Kitap Sil                    10-)Toplam Müşteri
                                        3-)Personel Şifre Güncelle          7-)Kitap Fiyatı Güncelle
                                        4-)Personel Görüntüle               8-)Kitap Görüntüle         
                                                                    11-)AnaMenüye Dön
                            """)
                            while True:
                                secim = input("Seçiminiz:")
                                if secim == "1" or secim == "2" or secim == "3" or secim == "4" or secim == "5" or secim == "6" or secim == "7" or secim == "8" or secim == "9" or secim == "10" or secim == "11":
                                    break
                                else:
                                    print("Hatalı İşlem...")
                            if secim == "1":
                                if personelekle() == 1:
                                    continue

                            if secim == "2":
                                if personelsil() == 1:
                                    continue

                            if secim == "3":
                                if personelsifreguncelle() == 1:
                                    continue

                            if secim == "4":

                                if personelgoruntule() == 1:
                                    continue

                            if secim == "5":

                                if kitapekle() == 1:
                                    continue

                            if secim == "6":

                                if kitapsil() == 1:
                                    continue

                            if secim == "7":

                                if kitapguncelle() == 1:
                                    continue

                            if secim == "8":

                                if kitapgoruntule() == 1:
                                    continue

                            if secim == "9":
                                if toplamkazanc() == 1:
                                    continue

                            if secim == "10":

                                if toplammusteri() == 1:
                                    continue

                            if secim == "11":
                                kontrolmenu=1
                                break
                        try:
                            if kontrolmenu == 1:
                                break
                        except:
                            pass
                try:
                    if kontrolmenu==1:
                        break
                except:
                    pass
    if secim=="2":
        if musteri()==1:
            continue

    if secim=="3":
        exit()
import datetime
def logla(mesaj):
    güncel_tarih = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    with open("hata_dosyam.txt","a+",encoding="utf-8") as file:
        file.write(f"Tarih : {str(güncel_tarih)} , Mesaj : {mesaj} \n")
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde
from faker import Faker
plt.style.use("seaborn-v0_8-darkgrid")
class System:
    def veri_seti_oluştur(self):
        fake = Faker()
        kategoriler = ["Elektronik", "Ev", "Gıda", "Spor", "Eğlence","Kitap","Kişisel Bakım","Kıyafet"]
        sayı = int(input("Ürün Sayısını Giriniz : "))
        kategori = np.random.choice(kategoriler, sayı)
        ürün_isimleri=[]
        fake = Faker()
        for _ in range(sayı):
            ürün_isimleri.append(fake.catch_phrase())
        satış_adedi = np.random.randint(100, 301, sayı)
        birim_fiyat = np.random.randint(100, 2001, sayı)
        self.df = pd.DataFrame({"Ürün İsmi": ürün_isimleri, "Ürünün Kategorisi": kategori, "Birim Fiyat": birim_fiyat,"Satış Adedi": satış_adedi},index=range(1,sayı+1))
        self.df["Gelir"]=self.df["Birim Fiyat"] * self.df["Satış Adedi"]
        def maliyet_hesapla(fiyat):
            if fiyat>1500:
                return fiyat*0.8
            elif 1000<fiyat<=1500:
                return fiyat*0.6
            elif 100<=fiyat<=1000:
                return fiyat*0.4
        self.df["Birim Maliyet"]=self.df["Birim Fiyat"].apply(maliyet_hesapla)
        self.df["Gider"]=self.df["Birim Maliyet"] * self.df["Satış Adedi"]
        self.df["Kar"]=self.df["Gelir"] - self.df["Gider"]
        self.df["Kar Marjı"]=(self.df["Kar"]/self.df["Gelir"])*100
        print(self.df)
    def analiz_yap(self):
        en_yüksek_kar_marjı=self.df.nlargest(1,"Kar Marjı")[["Ürün İsmi","Kar Marjı"]]
        en_düşük_kar_marjı=self.df.nsmallest(1,"Kar Marjı")[["Ürün İsmi","Kar Marjı"]]
        print(f"En yüksek kar marjına sahip ürün : {en_yüksek_kar_marjı['Ürün İsmi'].values} , kar marj oranı : {en_yüksek_kar_marjı['Kar Marjı'].values}")
        print(f"En düşük kar marjına sahip ürün : {en_düşük_kar_marjı['Ürün İsmi'].values} , kar marjı oranı {en_düşük_kar_marjı['Kar Marjı'].values}")
        toplam_gelir=self.df["Gelir"].sum()
        print(f" Toplam Gelir : {toplam_gelir} ₺")
        toplam_gider=self.df["Gider"].sum()
        print(f"Toplam Gider : {toplam_gider}")
    def grafik_çiz(self):
        print("Grafik Çizme Fonksiyonuna Hoşgeldiniz".center(50,"-"))
        print("Yapabilecekleriniz:\n1=Kategori Bazlı Ortalama\n2=İleri Düzey Analiz\n3=Birim Fiyat - Kar İlişkisi\n4=En İyi 5 Ürünün Pasta Grafiği")
        try:
            decision=int(input("Yapmak istediğiniz işlemin numarasını giriniz : "))
            if decision==1:
                kategori_bazlı_ortalama = self.df.groupby("Ürünün Kategorisi")["Gelir"].mean()
                plt.bar(x=kategori_bazlı_ortalama.index, height=kategori_bazlı_ortalama.values, color="Red")
                plt.xlabel("Kategoriler", fontsize=15, color="Black")
                plt.ylabel("Kategori Ortalaması", fontsize=15, color="Black")
                plt.title("KATEGORİ BAZLI ORTALAMA", color="Black", fontsize=20)
                plt.grid(True)
                plt.show()
            elif decision==2:
                plt.hist(self.df["Kar"], bins=8, density=True, color="Yellow", linewidth=3)
                kde = gaussian_kde(self.df["Kar"])
                x = np.linspace(self.df["Kar"].min(), self.df["Kar"].max(), 800)
                plt.plot(x, kde(x), color="Red", linestyle="--", linewidth=3, label="Yoğunluk Eğrisi")
                plt.title("İLERİ DÜZEY ANALİZ", color="Black", fontsize=20)
                plt.legend()
                plt.grid(True)
                plt.show()
            elif decision==3:
                plt.scatter(self.df["Birim Fiyat"],self.df["Kar"],color="Blue",marker="s")
                plt.xlabel("BİRİM FİYAT",color="Black",fontsize=15)
                plt.ylabel("KAR",color="Black",fontsize=15)
                plt.title("BİRİM FİYAT - KAR İLİŞKİSİ",color="Black",fontsize=20)
                plt.show()
            elif decision==4:
                kar_marjına_göre_en_iyi_beş_ürün=self.df.nlargest(5,"Kar Marjı")[["Ürün İsmi","Kar Marjı"]]
                plt.pie(kar_marjına_göre_en_iyi_beş_ürün['Kar Marjı'],labels=kar_marjına_göre_en_iyi_beş_ürün['Ürün İsmi'],colors=["Red", "Blue", "Pink", "Yellow", "Purple"],autopct="%1.1f%%",shadow=True)
                plt.title("EN İYİ 5 ÜRÜNÜN KAR MARJINA GÖRE PASTA GRAFİĞİ",fontsize=20,color="Black")
                plt.show()
            else:
                print("Lütfen Belirtilen Değerleri Giriniz!")
                logla(f"Kullanıcı Belirtilen Değerleri Tuşlamadı,Tarih:{str(datetime.datetime.now())}")
        except ValueError as v:
            print(f"Hata Kodu : {v} , Lütfen belirtilen değerleri giriniz!")
            logla(f"Kullanıcı Belirtilen Değerleri Tuşlamadı,Tarih:{str(datetime.datetime.now())}")
    def csv_çevirme(self):
        self.df.to_csv("ürün_bilgisi.csv",index=False,encoding="utf-8-sig")
        print("Kaydetme İşlemi Başarılı!")
    def fonksiyon(self):
        def tavsiye_ver(row):
            kar_marjı=row["Kar Marjı"]
            satış_adedi=row["Satış Adedi"]
            if kar_marjı<30 and satış_adedi<200:
                return "Satıştan Kaldırılsın"
            elif kar_marjı==60 and satış_adedi>200:
                return "Ürün Rafta Kalabilir"
            else:
                return "Ürün incelenmeye devam edilsin!"
        self.df["Tavsiye"]=self.df.apply(tavsiye_ver,axis=1)
        print(self.df)
def main():
    print("Dinamik Ürün Satış ve Kâr Simülasyonuna Hoşgeldiniz 😎".center(100,"*"))
    print("Yapabilecekleriniz:\n1=Analiz Yapabilme\n2=Grafik Çizme\n3=Ürünlerin Durumu Hakkında Tavsiye Alma\n4=Veriyi csv Formatına Çevirme\n5=Sistemden Çıkış🥺".center(60,"."))
    system = System()
    while True:
        try:
            karar = int(input("Yapmak İstediğiniz İşlemin Numarasını Giriniz : "))
            if karar==1:
                system.veri_seti_oluştur()
                system.analiz_yap()
            elif karar==2:
                system.veri_seti_oluştur()
                system.grafik_çiz()
            elif karar==3:
                system.veri_seti_oluştur()
                system.komik_fonksiyon()
            elif karar==4:
                system.veri_seti_oluştur()
                system.csv_çevirme()
            elif karar==5:
                print("Sistemden Başarıyla Çıkıldı")
                quit()
            else:
                print("Lütfen Belirtilen Değerleri Girinzi ⚠️")
                logla(f"Kullanıcı Belirtilen Değerleri Tuşlamadı,Tarih:{str(datetime.datetime.now())}")
        except ValueError as v:
            print(f"HATA KODU : {v} , Lütfen Belirtilen Değerleri Giriniz ⚠️")
            logla(f"Kullanıcı Belirtilen Değerleri Tuşlamadı,Tarih:{str(datetime.datetime.now())}")
if __name__=="__main__":
    main()

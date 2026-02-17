📦 Dinamik Ürün Satış ve Kâr Simülasyonu
Bu Python projesi, rastgele oluşturulan ürün verileri üzerinden satış, maliyet, kâr ve kâr marjı analizi yapmanızı sağlar. Kullanıcıdan alınan ürün sayısına göre sahte veri üretilir ve bu veriler üzerinden çeşitli analizler, grafikler ve raporlamalar yapılır.

🚀 Özellikler
Rastgele ürün isimleri (Faker kütüphanesi ile)

Kategori bazlı ürün atama

Birim fiyat ve satış adedine göre maliyet, gelir, gider, kâr ve kâr marjı hesaplama

Kullanıcı dostu menü sistemi

Grafiksel analizler (çubuk grafik, histogram, scatter, pie chart)

İleri düzey analiz (yoğunluk eğrisi ile histogram)

Tavsiye sistemi: Ürünlerin kâr marjı ve satış adedine göre ürün durumu önerisi

CSV formatında veri dışa aktarma

Hata loglama sistemi

🛠️ Kullanılan Kütüphaneler
datetime

matplotlib

pandas

numpy

scipy

faker

📂 Dosya Yapısı
product_sales_analysis.py – Ana program dosyası

hata_dosyam.txt – Hataların loglandığı dosya

ürün_bilgisi.csv – Dışa aktarılan veri dosyası

📌 Kullanım
Program çalıştırıldığında aşağıdaki menü karşınıza gelir:

text
Yapabilecekleriniz:
1=Analiz Yapabilme
2=Grafik Çizme
3=Ürünlerin Durumu Hakkında Tavsiye Alma
4=Veriyi csv Formatına Çevirme
5=Sistemden Çıkış
Her işlem öncesi kaç ürünle çalışmak istediğiniz sorulur. Ardından seçtiğiniz işleme göre analizler yapılır ve sonuçlar ekrana yansıtılır.

📊 Grafik Türleri
Kategori bazlı ortalama gelir (Bar chart)

İleri düzey analiz (Histogram + yoğunluk eğrisi)

Birim fiyat – kâr ilişkisi (Scatter plot)

En iyi 5 ürünün kâr marjına göre pasta grafiği

📝 Tavsiye Sistemi
Kâr marjı ve satış adedi kriterlerine göre ürünler için aşağıdaki tavsiyeler üretilir:

Satıştan Kaldırılsın

Ürün Rafta Kalabilir

Ürün incelenmeye devam edilsin

🧪 Örnek Çıktı
text
En yüksek kar marjına sahip ürün : ['Awesome Wooden Clock'] , kar marj oranı : [92.5]
Toplam Gelir : 2456000 ₺
Toplam Gider : 1345000
⚠️ Hata Yönetimi
Yanlış veri girişlerinde hata mesajı gösterilir ve bu hatalar hata_dosyam.txt dosyasına kaydedilir.

# YOLOv8 ile gerçek zamanlı sebze ve meyve tespiti

Bu depo, çeşitli meyve ve sebzelerin tespiti için YOLOv8 modelini ve OpenCV'yi kullanan bir Python betiği içermektedir. Domateslerin olgunluk seviyesinin belirlenmesi de dahildir. Tespit, gerçek zamanlı olarak bir web kamerası kullanılarak yapılır.

## 📄 YOLO_vegatable_detection.py

`YOLO_vegatable_detection.py` dosyası, bu deponun ana betiğidir. Nesne tespiti için YOLOv8 modelini ve görüntü işleme için OpenCV'yi kullanır.


`best.pt` dosyası YOLOv8 modelinin önceden eğitilmiş ağırlıklarını içerir.

## 📸 Ekran Görüntüleri

![yolo](https://github.com/AbdulhalikAkdeniz/Fruit-Vegatable-Detection-YOLOv8-With-OpenCV/assets/139945380/4058166f-5561-4bf7-8bd9-8c4bd2d5712d)


## ✨ Özellikler

- YOLOv8 kullanarak gerçek zamanlı meyve ve sebze tespiti.
- Tespit edilen nesnelerin, sınırlayıcı kutular ve etiketlerle görselleştirilmesi.
- Renk önyargısına dayalı olarak domateslerin olgunluk seviyesinin belirlenmesi.

    Renk önyargısı, domateslerin kırmızı ve yeşil renk kanallarının ortalamaları arasındaki farkı değerlendirir. Bu farka göre domateslerin olgunluk düzeyini tahmin eder ve kullanıcıya sunar.
- **Sınıf isimleri** : Fasulye, Kivi, PATLICAN, BAL KABAGI, BEYAZ KUDRET NARI, Beyaz Lahana, Biber, Brinjal, Brokoli, Domates, Karnabahar, KUDRET NARI, Papaya, SALATALIK, UZUM

## 📦 Gerekli Paketler

- ultralytics
- opencv-python
- matplotlib
- numpy

## 🔧 Kurulum

1. Bu depoyu klonlayın:

~~~sh
git clone https://github.com/AbdulhalikAkdeniz/Fruit-Vegatable-Detection-YOLOv8-With-OpenCV.git
~~~

2. Gerekli bağımlılıkları yükleyin:

~~~sh
pip install ultralytics opencv-python matplotlib numpy
~~~

## 🚀 Kullanım


1. `YOLO_vegatable_detection.py` dosyasını çalıştırın.
    
    Terminal veya komut isteminde proje klasörüne gidin
    ~~~sh
    cd .../Fruit-Vegatable-Detection-YOLOv8-With-OpenCV 
    ~~~
    
    ardından
    
    ~~~sh
    python YOLO_vegatable_detection.py
    ~~~

2. Web kameranızın bağlı olduğundan emin olun. Betik çalıştığında, meyve ve sebzeleri tespit etmeye başlayacak ve domateslerin olgunluk seviyesini belirleyecektir.
3. Betiği durdurmak için 'q' tuşuna basın.

## 📜 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır - ayrıntılar için [LICENSE](LICENSE) dosyasına bakın.

## 📧 İletişim
Sorularınız veya geri bildirimleriniz için lütfen abdulhalikakdeniz08@gmail.com adresine e-posta gönderin.

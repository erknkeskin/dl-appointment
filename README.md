# Flask Randevu Takip Uygulaması

Python, Flask, Postgres, Html, Javascript, Scss/Css gibi teknolojilerden yararlanılarak oluşturulmuş basit bir randevu takip sistemi altyapısıdır. DeepLab.Bootcamp Fullstack Uygulama Geliştirme yayını sırasında geliştirdiğimiz uygulamadır.

## Özellikler

- Randevu Ekleme / Silme / Güncelleme
- Randevu Durumunu Değiştirme

## Installation

Yerel postgress sunucunuzda bir veritabanı oluşturun ve db.sql dosyasını import edin. Kendi postgres yerel sunucunuzun kullanıcı ve şifre bilgisini config.py dosyasına girin. Giriş için varsayılan kullanıcı bilgileri aşağıdaki gibidir;

E-Mail => admin@example.com
Password => test

Bilgisayarınızda node ve npm kurulu olsun ve package.json dosyası ile aynı dizindeyken aşağıdaki komutu çalıştırın.

```sh
npm install
```

Bilgisayarınızda virtualenv kurulu olsun. Proje klasörünüzde bir sanal ortam oluşturun. Sonra bu sanal ortamı ( adının venv olduğunu varsayalım ) aşağıdaki komut ile aktive edin.

```sh
source venv/bin/activate
```
Bağımlılıklarımızı yükleyelim

```sh
pip install -r requirements.txt
```
Ardından geliştirici sunucumuzu çalıştıralım
```sh
flask run
```

Eğer 5000 port dolu değilse direkt olarak yerel sunucunuza aşağıdaki şekilde ulaşabilirsiniz.

```sh
http://127.0.0.1:5000/
```

Her türlü soru ve sorununuz için DeepLab discord kanalından bana ulaşabilirsiniz.


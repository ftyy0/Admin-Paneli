\#  Admin Yönetim Paneli



Bu çalışma, benim \*\*ilk Python projem\*\* olup, yazılım geliştirme sürecindeki temel prensipleri ve veritabanı entegrasyonunu öğrenme amacıyla geliştirilmiştir. Proje kapsamında \*\*Python (Tkinter)\*\* arayüzü ile \*\*MS SQL Server\*\* arasında modüler bir bağ kurulmuş; iş mantığı büyük oranda SQL tarafındaki \*\*Saklı Yordamlar (Stored Procedures)\*\* ve \*\*Tetikleyiciler (Triggers)\*\* ile yönetilmiştir.



\---



\##  Temel Özellikler



\*   \*\*Oyuncu Veritabanı Yönetimi:\*\* Nick veya ID ile gerçek zamanlı arama, yeni karakter oluşturma ve istatistik takibi.

\*   \*\*Gelişmiş Ceza Sistemi:\*\* Banlama ve ban kaldırma işlemleri, yönetimsel takip için zorunlu sebep günlüğü ile entegre edilmiştir.

\*   \*\*Envanter Kontrolü:\*\* Seçim sistemiyle oyunculara doğrudan eşya gönderimi.

\*   \*\*Kaynak Yönetimi:\*\* Oyuncu Altın (Gold) ve Seviye (Level) miktarlarını anlık güncelleme.

\*   \*\*Sistem Logları:\*\* Güvenlik denetimleri için panel üzerinden yapılan her işlemin tarihli ve açıklamalı tam geçmiş takibi.

\*   \*\*SQL Mimari:\*\* Tüm veritabanı işlemleri, performans ve güvenlik amacıyla optimize edilmiş SQL Saklı Yordamları üzerinden yürütülür.



\---



\##  Teknoloji Yığını



\*   \*\*Dil:\*\* Python 3.x

\*   \*\*Arayüz (GUI):\*\* Tkinter \& ttk

\*   \*\*Veritabanı:\*\* Microsoft SQL Server

\*   \*\*Bağlantı:\*\* `pyodbc` kütüphanesi

\*   \*\*Tasarım:\*\* Hızlı navigasyon için modüler ve renk kodlu yapı



\---



\##  Önkoşullar



Uygulamayı çalıştırmadan önce sisteminizde şunların kurulu olduğundan emin olun:

1\.  \*\*Python 3.x\*\*

2\.  \*\*Microsoft SQL Server\*\*

3\.  \*\*ODBC Driver 17 for SQL Server\*\*

4\.  Gerekli kütüphane kurulumu:

&#x20;   ```bash

&#x20;   pip install pyodbc

&#x20;   ```



 Kurulum ve Yapılandırma

Veritabanı Kurulumu:



SQL Server'da Final\_proje adında bir veritabanı oluşturun.  



Tabloları, prosedürleri ve limit kontrol tetikleyicisini (trigger) oluşturmak için VeriTabani.sql dosyasını çalıştırın.  



Bağlantı Yapılandırması:



VTveRENKLER.py dosyasını açın.



VT\_AYAR değişkenini kendi sunucu bilgilerinizle güncelleyin:



&#x09;VT\_AYAR = (

&#x20;   'Driver={ODBC Driver 17 for SQL Server};'

&#x20;   'Server=SUNUCU\_ADINIZ;'

&#x20;   'Database=Final\_proje;'

&#x20;   'Trusted\_Connection=yes;'

)





\*\*Çalıştırma:\*\*

&#x20;   \*   Sistemi başlatmak için `Starter.py` dosyasını çalıştırın.

&#x20;   \*   \*\*Varsayılan Bilgiler:\*\* Kullanıcı: `admin` | Şifre: `12345`.



\---



\##  Proje Yapısı



\*   `Starter.py`: Uygulamanın ana giriş noktası.

\*   `Login\_Paneli.py`: Kimlik doğrulama ve geliştirici modu erişimi.

\*   `Admin\_Arayuzu\_2.py`: Oyuncu yönetimi mantığını içeren ana dashboard.

\*   `Veri\_Tabani.py`: Veritabanı bağlantısı ve sorgu yürütme katmanı.

\*   `VTveRENKLER.py`: Arayüz renkleri ve SQL bağlantı ayarları.



\---



\*\*Not:\*\* Bu proje, veritabanı bağlantısı kurmadan arayüzü test edebilmeniz için giriş ekranında bir 'Geliştirici Modu (Hızlı Giriş)' özelliği içerir. Gerçek kullanım için veritabanı bağlantısının yapılandırıldığından emin olun.


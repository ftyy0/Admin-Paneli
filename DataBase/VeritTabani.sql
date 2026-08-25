CREATE DATABASE Final_Proje;
GO
USE Final_proje;
GO

-- 1. TABLOLARIN OLUÞTURULMASI
CREATE TABLE Oyuncular (
    PlayerID INT IDENTITY(1,1) PRIMARY KEY,
    NickName NVARCHAR(50) UNIQUE,
    Sýnýf NVARCHAR(20),
    "Level" INT,
    Gold INT,
    Banli_mi NVARCHAR(20)
);

CREATE TABLE Esyalar (
    ItemID INT IDENTITY(1,1) PRIMARY KEY,
    ItemName NVARCHAR(100),
    ItemTur NVARCHAR(100),
    Stat INT
);

CREATE TABLE Envanter (
    PlayerID INT NOT NULL,
    ItemID INT NOT NULL,
    Miktar INT NOT NULL,
    FOREIGN KEY (PlayerID) REFERENCES Oyuncular(PlayerID),
    FOREIGN KEY (ItemID) REFERENCES Esyalar(ItemID)
);

CREATE TABLE Loglar (
    LogID INT IDENTITY(1,1) PRIMARY KEY,
    PlayerID INT,
    IslemTuru NVARCHAR(50),
    Aciklama NVARCHAR(500),
    Tarih DATETIME DEFAULT GETDATE()
);

CREATE TABLE Adminler (
    AdminID INT IDENTITY(1,1) PRIMARY KEY, 
    KullaniciAdi NVARCHAR(50) UNIQUE NOT NULL, 
    Sifre NVARCHAR(50) NOT NULL,
    SonGirisTarihi DATETIME DEFAULT GETDATE() 
);
GO

-- 2. ÖRNEK VERÝLERÝN EKLENMESÝ
INSERT INTO Adminler (KullaniciAdi, Sifre) VALUES ('admin', '12345');

INSERT INTO Oyuncular (NickName, Sýnýf, "Level", Gold, Banli_mi) VALUES 
('SuraKral', 'Warrior', 75, 4500, 'Hayýr'),
('KalkanSavascisi', 'Tank', 90, 1200, 'Hayýr'), 
('XxNinjaBossxX', 'Warrior', 55, 8500, 'Evet');

INSERT INTO Esyalar (ItemName, ItemTur, Stat) VALUES 
('Þeytan Boynuzu Zýrh', 'Zýrh', 66),
('Muharebe Kýlýcý', 'Silah', 75),
('Kýrmýzý Ýksir (Büyük)', 'Ýksir', 1),
('Kritik Vuruþ Taþý', 'Taþ', 5);
GO

-- 3. STORED PROCEDURELER (SÝSTEMÝN BEYNÝ)

-- Admin Giriþi ve Tarih Güncelleme
CREATE PROCEDURE sp_admin_giris
    @KullaniciAdi NVARCHAR(50), @Sifre NVARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;
    UPDATE Adminler SET SonGirisTarihi = GETDATE()
    WHERE KullaniciAdi = @KullaniciAdi AND Sifre = @Sifre;
    SELECT * FROM Adminler WHERE KullaniciAdi = @KullaniciAdi AND Sifre = @Sifre;
END
GO

-- Oyuncu Arama (Nick veya ID ile)
CREATE PROCEDURE sp_oyuncu_ara
    @Aranan NVARCHAR(50)
AS
BEGIN
    SELECT PlayerID,NickName,Sýnýf,Gold,Level,Banli_mi 
    FROM Oyuncular 
    WHERE LOWER(NickName) LIKE '%'+LOWER(@Aranan)+'%' 
       OR CAST(PlayerID as VARCHAR) LIKE '%'+@Aranan+'%'
END
GO

-- Tüm Oyuncularý Listeleme
CREATE PROCEDURE sp_tum_oyunculari_getir
AS
BEGIN
    SELECT PlayerID,NickName,Sýnýf,Gold,Level,Banli_mi FROM Oyuncular
END
GO

-- Banlama ve Loglama Sistemi
CREATE PROCEDURE sp_ban_islemi
    @PlayerID INT, @Durum NVARCHAR(20), @Sebep NVARCHAR(250) = '-'
AS
BEGIN
    UPDATE Oyuncular SET Banli_mi=@Durum WHERE PlayerID=@PlayerID
    DECLARE @LogMesaj NVARCHAR(500)
    IF @Durum='Evet'
        SET @LogMesaj=CAST(@PlayerID AS NVARCHAR) +' ID''li oyuncu banlandý. Sebep: '+@Sebep     
    ELSE
        SET @LogMesaj=CAST(@PlayerID AS NVARCHAR) +' ID''li oyuncunun baný kaldýrýldý.'
    
    INSERT INTO Loglar (PlayerID,IslemTuru,Aciklama) VALUES (@PlayerID,'Ban Ýþlemi',@LogMesaj)
END
GO

-- Gold Verme/Silme ve Loglama
CREATE PROCEDURE sp_gold_ver
    @PlayerID INT, @Miktar INT
AS
BEGIN
    UPDATE Oyuncular SET Gold=Gold+@Miktar WHERE PlayerID=@PlayerID
    INSERT INTO Loglar (PlayerID,IslemTuru,Aciklama) 
    VALUES (@PlayerID,'Gold Ýþlemi', CAST(@PlayerID AS NVARCHAR) + ' ID''ye ' + CAST(@Miktar AS NVARCHAR) + ' Gold iþlemi yapýldý.')
END
GO

-- Level Verme/Silme ve Loglama
CREATE PROCEDURE sp_level_ver
    @PlayerID INT, @Miktar INT
AS
BEGIN
    UPDATE Oyuncular SET Level=Level+@Miktar WHERE PlayerID=@PlayerID
    INSERT INTO Loglar (PlayerID,IslemTuru,Aciklama) 
    VALUES (@PlayerID,'Level Ýþlemi', CAST(@PlayerID AS NVARCHAR) + ' ID''ye ' + CAST(@Miktar AS NVARCHAR) + ' Level iþlemi yapýldý.')
END
GO

-- Eþya Yönetimi Prosedürleri
CREATE PROCEDURE sp_esya_listesi AS BEGIN SELECT ItemID,ItemName FROM Esyalar END
GO

CREATE PROCEDURE sp_esya_ekle @PlayerID INT, @ItemID INT
AS
BEGIN
    INSERT INTO Envanter (PlayerID,ItemID,Miktar) VALUES (@PlayerID,@ItemID,1)
    INSERT INTO Loglar (PlayerID,IslemTuru,Aciklama) 
    VALUES (@PlayerID,'Eþya Gönderimi', CAST(@PlayerID AS NVARCHAR) + ' ID''ye ItemID:' + CAST(@ItemID AS NVARCHAR) + ' verildi.')
END
GO

CREATE PROCEDURE sp_envanter_detay @PlayerID INT
AS
BEGIN
    SELECT E.ItemName,SUM(Env.Miktar) as Toplam_Miktar FROM Envanter Env
    JOIN Esyalar E ON Env.ItemID=E.ItemID WHERE Env.PlayerID=@PlayerID
    GROUP BY E.ItemName ORDER BY Toplam_Miktar DESC
END
GO

-- Oyuncu Ekleme ve Loglama
CREATE PROCEDURE sp_log_gecmisi AS BEGIN SELECT LogID,Tarih,IslemTuru,PlayerID,Aciklama FROM Loglar ORDER BY Tarih DESC END
GO

CREATE PROCEDURE sp_oyuncu_ekle @NickName NVARCHAR(50), @Sinif NVARCHAR(50), @Level INT, @Gold INT
AS
BEGIN
    INSERT INTO Oyuncular (NickName,Sýnýf,Level,Gold,Banli_mi) VALUES (@NickName,@Sinif,@Level,@Gold,'Hayýr')
END
GO

-- Raporlar (Top 5)
CREATE PROCEDURE sp_raporlar
AS
BEGIN
    SELECT * FROM (SELECT TOP 5 'Top 5 (Gold)' AS Kategori,NickName,Sýnýf,Gold FROM Oyuncular ORDER BY Gold DESC) AS T1
    UNION ALL
    SELECT * FROM (SELECT TOP 5 'Top 5 (Level)' AS Kategori, NickName, Sýnýf,Level FROM Oyuncular ORDER BY Level DESC) AS T2
END
GO

-- 4. GÜVENLÝK VE LÝMÝT KONTROLÜ (TRIGGER)
CREATE TRIGGER trg_LimitKontrol
ON Oyuncular
AFTER UPDATE, INSERT
AS
BEGIN
    IF EXISTS (SELECT 1 FROM inserted WHERE Level > 99)
    BEGIN
        RAISERROR ('HATA: Level maksimum 99 olabilir.', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END
    IF EXISTS (SELECT 1 FROM inserted WHERE Gold > 999999)
    BEGIN
        RAISERROR ('HATA: Gold maksimum 999.999 olabilir.', 16, 1);
        ROLLBACK TRANSACTION;
        RETURN;
    END
END
GO
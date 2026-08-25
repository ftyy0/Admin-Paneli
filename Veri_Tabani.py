import pyodbc
from tkinter import messagebox
import VTveRENKLER

class VeriTabani:
    def __init__(self):
        self.conn_str=VTveRENKLER.VT_AYAR

    def baglanti(self):
        try:
            return pyodbc.connect(self.conn_str)
        except pyodbc.Error as e:
            print(f"SQL Bağlantı Hatası: {e}")
            messagebox.showerror("Bağlantı Hatası",f"Veritabanına erişilemiyor.\nHata: {e}")
            return None

    def sorgu_calistir(self,sorgu,parametreler=(),veri_donus=False):
        conn=self.baglanti()
        if conn is None:
            return None
        try:
            cursor=conn.cursor()
            cursor.execute(sorgu,parametreler)      
            if veri_donus:
                veriler=cursor.fetchall()
                conn.commit()
                return veriler
            else:
                conn.commit()
                return True               
        except pyodbc.Error as e:
            messagebox.showerror("Veritabanı İşlem Hatası",f"İşlem yapılamadı.\nHata Detayı: {e}")
            return None
        finally:
            conn.close()

    def giris_yap(self,kadi,sifre):
        sonuc=self.sorgu_calistir("EXEC sp_admin_giris ?,?",(kadi,sifre),veri_donus=True)
        if sonuc:          
            return True
        else:              
            return False

    def oyuncu_getir(self,aranan=None):
        if aranan:
            return self.sorgu_calistir("EXEC sp_oyuncu_ara ?",(aranan,),veri_donus=True)
        return self.sorgu_calistir("EXEC sp_tum_oyunculari_getir",veri_donus=True)

    def oyuncu_ekle(self,nick,sinif,level,gold):
        return self.sorgu_calistir("EXEC sp_oyuncu_ekle ?,?,?,?",(nick,sinif,level,gold))

    def ban_guncelle(self,player_id,durum,sebep="-"):
        return self.sorgu_calistir("EXEC sp_ban_islemi ?,?,?",(player_id,durum,sebep))

    def kaynak_ver(self,player_id,miktar,tur):
        if tur=="Gold":
            return self.sorgu_calistir("EXEC sp_gold_ver ?,?",(player_id,miktar))
        if tur=="Level":
            return self.sorgu_calistir("EXEC sp_level_ver ?,?",(player_id,miktar))

    def esya_listesi_al(self):
        veriler=self.sorgu_calistir("EXEC sp_esya_listesi",veri_donus=True)
        if veriler:
            veriler2=[]
            for i in veriler:
                cmb_yazi=f"{i[0]} | {i[1]}"
                veriler2.append(cmb_yazi)
            return veriler2
        else:
            return []

    def esya_ekle(self,player_id,item_id):
        return self.sorgu_calistir("EXEC sp_esya_ekle ?,?",(player_id,item_id))

    def envanter_goruntule(self,player_id):
        return self.sorgu_calistir("EXEC sp_envanter_detay ?",(player_id,),veri_donus=True)

    def loglari_getir(self):
        return self.sorgu_calistir("EXEC sp_log_gecmisi",veri_donus=True)
    
    def raporlari_getir(self):
        return self.sorgu_calistir("EXEC sp_raporlar",veri_donus=True)
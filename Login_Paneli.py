import tkinter as tk
from tkinter import messagebox
import VTveRENKLER
from Veri_Tabani import VeriTabani

class Giris_Paneli:
    def __init__(self):
        self.vt=VeriTabani()
        self.pencere=tk.Tk()
        self.pencere.title("Sisteme Giriş")
        self.pencere.geometry("800x500")
        self.pencere.configure(bg=VTveRENKLER.RENKLER["arkapanel"])
        self.arayuz_olustur()

    def arayuz_olustur(self):
        R=VTveRENKLER.RENKLER
        lbl_baslik=tk.Label(self.pencere,text="ADMİN PANELİ",font=("Impact",24),bg=R["arkapanel"],fg=R["sari"])
        lbl_baslik.pack(pady=40)

        frame_giris=tk.Frame(self.pencere,bg=R["arkapanel"])
        frame_giris.pack()
        
        btn_hizli_giris = tk.Button(self.pencere, text="HIZLI GİRİŞ (Veritabanı kontrolünü atlamak için)",bg=R["sari"],fg=R["siyah"], font=("Arial",10,"bold"),command=self.hizli_giris_yap)
        btn_hizli_giris.pack(pady=5)

        lbl_kul=tk.Label(frame_giris,text="Kullanıcı Adı:",font=("Arial",12,"bold"),bg=R["arkapanel"],fg=R["yazi"])
        lbl_kul.grid(row=0,column=0,padx=10,pady=10,sticky="e")

        self.entry_kul=tk.Entry(frame_giris,font=("Arial",12))
        self.entry_kul.grid(row=0,column=1,padx=10,pady=10)

        lbl_sifre=tk.Label(frame_giris,text="Şifre:",font=("Arial",12,"bold"),bg=R["arkapanel"],fg=R["yazi"])
        lbl_sifre.grid(row=1,column=0,padx=10,pady=10,sticky="e")

        self.entry_sifre=tk.Entry(frame_giris,font=("Arial",12),show="*")
        self.entry_sifre.grid(row=1,column=1,padx=10,pady=10)

        btn_giris=tk.Button(self.pencere,text="GİRİŞ YAP",bg=R["sari"],fg=R["siyah"],font=("Arial",11,"bold"),width=20,height=2,command=self.giris_yap)
        btn_giris.pack(pady=30)

        
    def hizli_giris_yap(self):
        messagebox.showinfo("Geliştirici Modu","Veritabanı kontrolü atlandı.")
        self.pencere.destroy()
        from Admin_Arayuzu import Admin_Paneli
        Admin_Paneli().baslat()

    def giris_yap(self):
        kadi=self.entry_kul.get()
        sifre=self.entry_sifre.get()

        if self.vt.giris_yap(kadi,sifre):
            messagebox.showinfo("Başarılı","Admin paneline giriş izni verildi.")
            self.pencere.destroy()
            from Admin_Arayuzu import Admin_Paneli
            Admin_Paneli().baslat()
        else:
            messagebox.showerror("Hata","Kullanıcı adı veya şifre yanlış.")

    def baslat(self):
        self.pencere.mainloop()
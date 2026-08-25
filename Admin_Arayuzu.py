import tkinter as tk
from tkinter import ttk,messagebox,simpledialog
import VTveRENKLER
from Veri_Tabani import VeriTabani

R=VTveRENKLER.RENKLER
class Admin_Paneli:
    def __init__(self):
        self.vt=VeriTabani()
        self.pencere=tk.Tk()
        self.pencere.title("Panel")
        self.pencere.geometry("1368x768")
        self.pencere.configure(bg=R["arkapanel"])
        self.player_id=None
        self.arayuz_kur()

    def arayuz_kur(self):       
        cerceve_ust=tk.Frame(self.pencere,bg=R["arkapanel"],height=60,width=1400,bd=3)
        cerceve_ust.place(x=0,y=0)

        lbl_baslik=tk.Label(cerceve_ust,text="Admin Paneli",font=("Impact",20),bg=R["arkapanel"],fg=R["sari"])
        lbl_baslik.place(x=10,y=10)

        btn_yeni_karakter=tk.Button(cerceve_ust,text="Yeni Karakter Ekle",bg=R["mavi"],fg=R["yazi"],font=("Arial",10,"bold"),command=self.karakter_ekle)
        btn_yeni_karakter.place(x=1040,y=15)

        btn_loglar=tk.Button(cerceve_ust,text="Loglar",bg=R["solpanel"],fg=R["yazi"],font=("Arial",10,"bold"),command=self.log_penceresi)
        btn_loglar.place(x=1190,y=15)

        btn_raporlar=tk.Button(cerceve_ust,text="Raporlar",bg=R["solpanel"],fg=R["yazi"],font=("Arial",10,"bold"),command=self.rapor_penceresi)
        btn_raporlar.place(x=1260,y=15)

        btn_cikis=tk.Button(cerceve_ust,text="Çıkış Yap",bg=R["kirmizi"],fg=R["yazi"],font=("Arial",10,"bold"),width=10,command=self.cikis_yap)
        btn_cikis.place(x=930,y=15)

        cerceve_sol=tk.Frame(self.pencere,height=670,width=600,bg=R["solpanel"])
        cerceve_sol.place(x=10,y=70)

        lbl_ara=tk.Label(cerceve_sol,text="Oyuncu Ara:",bg=R["solpanel"],fg=R["yazi"],font=("Arial",12))
        lbl_ara.place(x=10,y=10)

        self.entry_arama=tk.Entry(cerceve_sol,font=("Arial",11),width=72)
        self.entry_arama.place(x=10,y=45)

        btn_bul=tk.Button(cerceve_sol,text="Bul",bg=R["mavi"],fg=R["yazi"],width=10,command=self.oyuncu_ara)
        btn_bul.place(x=140,y=80)

        btn_tum_kayitlar=tk.Button(cerceve_sol,text="Tüm Kayıtları Getir",bg=R["solpanel"],fg=R["yazi"],width=28,command=self.tum_kayitlar)
        btn_tum_kayitlar.place(x=230,y=80)

        cerceve_liste=tk.Frame(cerceve_sol,bg=R["solpanel"],width=580,height=540)
        cerceve_liste.place(x=10,y=120)

        style=ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",bg=R["solpanel"],fg=R["yazi"])
        style.map('Treeview',background=[('selected',R["mavi"])])

        sutunlar=("ID","İsim","Sınıf","Gold","Level","Durum")
        self.liste=ttk.Treeview(cerceve_liste,columns=sutunlar,show="headings",style="Treeview")

        for sutun in sutunlar:
            self.liste.heading(sutun,text=sutun)
            self.liste.column(sutun,width=90,anchor='center')
        self.liste.column("İsim",width=100,anchor='center')

        kayanbar=ttk.Scrollbar(cerceve_liste,orient="vertical",command=self.liste.yview)
        
        self.liste.configure(yscrollcommand=kayanbar.set)
        self.liste.pack(side="left",fill="both",expand=True)
        kayanbar.pack(side="right",fill="y")
        self.liste.bind("<<TreeviewSelect>>",self.oyuncu_secimi)

        cerceve_sag=tk.Frame(self.pencere,bg=R["sagpanel"],height=670,width=730,bd=3)
        cerceve_sag.place(x=620,y=70)

        cerceve_hedef=tk.Frame(cerceve_sag,bg=R["sagpanel"],width=640,height=100)
        cerceve_hedef.place(x=10,y=10)

        lbl_secili_oyuncu=tk.Label(cerceve_hedef,text="Seçili Oyuncu:",bg=R["sagpanel"],fg="gray")
        lbl_secili_oyuncu.pack()

        self.lbl_hedef_isim=tk.Label(cerceve_hedef,text="Hedef Seçilmedi",font=("Arial",20,"bold"),bg=R["sagpanel"],fg="gray")
        self.lbl_hedef_isim.pack()

        self.lbl_hedef_detay=tk.Label(cerceve_hedef,text="Soldan bir oyuncu seç.",bg=R["sagpanel"],fg=R["yazi"])
        self.lbl_hedef_detay.pack()

        lfrm_ceza=tk.LabelFrame(cerceve_sag,text=" Ceza İşlemleri ",bg=R["sagpanel"],fg=R["kirmizi"],font=("Arial",11,"bold"))
        lfrm_ceza.place(x=20,y=130,width=620,height=80)

        btn_banla=tk.Button(lfrm_ceza,text="BANLA",bg=R["kirmizi"],fg=R["siyah"],width=15,command=self.banla)
        btn_banla.place(x=20,y=10)

        btn_ban_ac=tk.Button(lfrm_ceza,text="BAN AÇ",bg=R["yesil"],fg=R["siyah"],width=15,command=self.ban_ac)
        btn_ban_ac.place(x=200,y=10)

        lfrm_kaynak=tk.LabelFrame(cerceve_sag,text="Kaynak Gönder",bg=R["sagpanel"],fg=R["sari"],font=("Arial",11,"bold"))
        lfrm_kaynak.place(x=20,y=230,width=620,height=100)

        lbl_miktar=tk.Label(lfrm_kaynak,text="Miktar:",bg=R["sagpanel"],fg=R["yazi"])
        lbl_miktar.place(x=20,y=20)

        self.entry_miktar=tk.Entry(lfrm_kaynak,width=10)
        self.entry_miktar.place(x=80,y=20)

        btn_altin_ver=tk.Button(lfrm_kaynak,text="Altın Ver",bg=R["sari"],fg=R["siyah"],width=15,command=self.altin_ver)
        btn_altin_ver.place(x=200,y=15)

        btn_level_ver=tk.Button(lfrm_kaynak,text="Level Ver",bg=R["mor"],fg=R["siyah"],width=15,command=self.level_ver)
        btn_level_ver.place(x=350,y=15)

        lfrm_esya=tk.LabelFrame(cerceve_sag,text="Eşya ve Envanter",bg=R["sagpanel"],fg=R["mavi"],font=("Arial",11,"bold"))
        lfrm_esya.place(x=20,y=350,width=620,height=150)

        lbl_esya_id=tk.Label(lfrm_esya,text="Eşya ID:",bg=R["sagpanel"],fg=R["yazi"])
        lbl_esya_id.place(x=20,y=20)

        self.cmb_esya=ttk.Combobox(lfrm_esya,width=20, state="readonly")
        self.cmb_esya.place(x=80,y=20)
        self.cmb_esya['values']=self.vt.esya_listesi_al()

        btn_esya_gonder=tk.Button(lfrm_esya,text="Gönder",bg=R["turuncu"],fg=R["siyah"],width=13,command=self.esya_ekle)
        btn_esya_gonder.place(x=245,y=17)

        btn_envanter_gor=tk.Button(lfrm_esya,text="OYUNCUNCU ENVANTER GÖR",bg=R["mavi"],fg=R["siyah"],width=40,command=self.envanter_goruntule)
        btn_envanter_gor.place(x=150,y=70)

    def karakter_ekle(self):
        karakter_ekle=tk.Toplevel(self.pencere)
        karakter_ekle.title("Yeni Karakter Ekle")
        karakter_ekle.geometry("300x400")
        karakter_ekle.configure(bg=R["arkapanel"])

        lbl_nick=tk.Label(karakter_ekle,text="NickName:",bg=R["arkapanel"],fg=R["yazi"])
        lbl_nick.pack(pady=5)
        
        ent_nick=tk.Entry(karakter_ekle)
        ent_nick.pack()

        lbl_sinif=tk.Label(karakter_ekle,text="Sınıf:",bg=R["arkapanel"],fg=R["yazi"])
        lbl_sinif.pack(pady=5)

        cmb_sinif=ttk.Combobox(karakter_ekle,values=["Warrior","Tank","Healer","Wizard"])
        cmb_sinif.pack()
        cmb_sinif.current(0)

        lbl_lvl=tk.Label(karakter_ekle,text="Level:",bg=R["arkapanel"],fg=R["yazi"])
        lbl_lvl.pack(pady=5)

        ent_level=tk.Entry(karakter_ekle)
        ent_level.pack()
        ent_level.insert(0,"0")

        lbl_gold=tk.Label(karakter_ekle,text="Gold:",bg=R["arkapanel"],fg=R["yazi"])
        lbl_gold.pack(pady=5)

        ent_gold=tk.Entry(karakter_ekle)
        ent_gold.pack()
        ent_gold.insert(0,"0")

        def kaydet():
            nick=ent_nick.get()
            sinif=cmb_sinif.get()
            if not nick:
                messagebox.showwarning("Eksik Bilgi","Nickname boş olamaz.")
                return
            try: 
                lvl=int(ent_level.get())
                gold=int(ent_gold.get())           
                self.vt.oyuncu_ekle(nick,sinif,lvl,gold)              
                messagebox.showinfo("Başarılı","Karakter oluşturuldu.")
                karakter_ekle.destroy()
                self.tum_kayitlar()
            except ValueError:
                messagebox.showerror("Hata","Level ve Gold alanlarına sadece sayı girimeli.")

        btn_kaydet=tk.Button(karakter_ekle,text="KAYDET",bg=R["yesil"],fg=R["siyah"],command=kaydet)
        btn_kaydet.pack(pady=20)

    def liste_doldur(self,veriler):
        for satir in self.liste.get_children():
            self.liste.delete(satir)
        for veri in veriler:
            if veri[5]=='Evet':
                durum="BANLI"
            else:
                durum="BANSIZ"
            self.liste.insert("","end",values=(veri[0],veri[1],veri[2],veri[3],veri[4],durum))
            
    def oyuncu_ara(self):
        aranan=self.entry_arama.get()
        if not aranan.strip():
            messagebox.showwarning("Uyarı","Lütfen bir oyuncu adı veya ID girin.")
            return
        sonuclar=self.vt.oyuncu_getir(aranan)
        self.liste_doldur(sonuclar)

    def tum_kayitlar(self):
        self.entry_arama.delete(0,tk.END)
        veriler=self.vt.oyuncu_getir()
        self.liste_doldur(veriler)

    def oyuncu_secimi(self,event):
        secilen=self.liste.selection()
        if secilen:
            degerler=self.liste.item(secilen)['values']
            self.player_id=degerler[0]
            isim=degerler[1]
            durum=degerler[5]
            self.lbl_hedef_isim.config(text=isim,fg=R["sari"])
            self.lbl_hedef_detay.config(text=f"ID: {self.player_id} | Durum: {durum}")
        else:
            self.player_id=None
            self.lbl_hedef_isim.config(text="HEDEF SEÇİLMEDİ",fg="gray")
            self.lbl_hedef_detay.config(text="Soldan bir oyuncu seç.")

    def banla(self):
        if not self.player_id:
            messagebox.showwarning("Hata","Lütfen önce listeden bir oyuncu seç.")
            return
        sebep=simpledialog.askstring("Ban İşlemi",f"{self.player_id} ID'li oyuncuyu banlama nedeniniz:")
        if sebep and sebep.strip()!="":
            self.vt.ban_guncelle(self.player_id,'Evet',sebep)
            messagebox.showinfo("İşlem Yapıldı","Oyuncu banlandı ve sebep loglandı.")
            if self.entry_arama.get().strip()=="":
                self.tum_kayitlar()
            else:
                self.oyuncu_ara()
        else:
            if sebep is not None:
                messagebox.showwarning("İptal","Banlama işlemi için bir sebep girmelisiniz.")

    def ban_ac(self):
        if not self.player_id:
            messagebox.showwarning("Hata","Lütfen önce listeden bir oyuncu seç.")
            return
        cevap=messagebox.askyesno("Dikkat",f"{self.player_id} ID'li oyuncunun banı kaldırılsın mı ?")
        if cevap:
            self.vt.ban_guncelle(self.player_id,'Hayır',"Yönetici Kararı")
            messagebox.showinfo("İşlem Yapıldı","Oyuncu banı açıldı.")
            if self.entry_arama.get().strip()=="":
                self.tum_kayitlar()
            else:
                self.oyuncu_ara()

    def altin_ver(self):
        if not self.player_id:
            messagebox.showwarning("Hata","Lütfen önce listeden bir oyuncu seç.")
            return        
        try:
            miktar=int(self.entry_miktar.get())
            if miktar<0:
                messagebox.showwarning("Hata","Negatif değer giremezsiniz!")
                return
            
            sonuc=self.vt.kaynak_ver(self.player_id,miktar,"Gold")
            if sonuc:
                messagebox.showinfo("İşlem",f"{self.player_id} ID'li oyuncuya {miktar} Gold eklendi.")            
                if self.entry_arama.get().strip()=="":
                    self.tum_kayitlar()
                else:
                    self.oyuncu_ara()
        except ValueError:
            messagebox.showerror("Hata","Lütfen sayı girin.")

    def level_ver(self):
        if not self.player_id:
            messagebox.showwarning("Hata","Lütfen önce listeden bir oyuncu seç.")
            return
        try:
            miktar=int(self.entry_miktar.get())
            if miktar<0:
                messagebox.showwarning("Hata","Negatif değer giremezsiniz!")
                return
            sonuc=self.vt.kaynak_ver(self.player_id,miktar,"Level")
            if sonuc:
                messagebox.showinfo("İşlem",f"{self.player_id} ID'li oyuncuya {miktar} Level eklendi.")
                if self.entry_arama.get().strip()=="":
                    self.tum_kayitlar()
                else:
                    self.oyuncu_ara()
        except ValueError:
            messagebox.showerror("Hata","Lütfen sayı giriniz.")

    def esya_ekle(self):
        esya=self.cmb_esya.get()
        if not self.player_id:
            messagebox.showwarning("Hata","Lütfen önce listeden bir oyuncu seç.")
            return      
        if not esya:
            messagebox.showwarning("Hata","Lütfen eşya seçiniz.")
            return
        esya_id=esya.split('|')[0].strip()
        self.vt.esya_ekle(self.player_id,int(esya_id))
        messagebox.showinfo("İşlem Yapıldı","Eşya envantere eklendi.")

    def envanter_goruntule(self):
        if not self.player_id:
            messagebox.showwarning("Hata","Lütfen önce listeden bir oyuncu seçin.")
            return
        env_pencere=tk.Toplevel(self.pencere)
        env_pencere.title(f"Oyuncu Envanteri - ID: {self.player_id}")
        env_pencere.geometry("500x400")
        env_pencere.configure(bg=R["arkapanel"])

        sutunlar=("Eşya Adı","Miktar")
        tree=ttk.Treeview(env_pencere,columns=sutunlar,show="headings")
        tree.heading("Eşya Adı",text="Eşya Adı")
        tree.heading("Miktar",text="Miktar")
        tree.column("Eşya Adı",width=250,anchor='center')
        tree.column("Miktar",width=100,anchor='center')        
        tree.pack(fill="both",expand=True,padx=10,pady=10)

        kayitlar=self.vt.envanter_goruntule(self.player_id)
        if kayitlar:
            for kayit in kayitlar:
                tree.insert("","end",values=(kayit[0],kayit[1]))
        else:
            tree.insert("","end",values=("ENVANTER BOŞ","-"))

    def log_penceresi(self):
        log_ekrani=tk.Toplevel(self.pencere)
        log_ekrani.title("Sistem Log Kayıtları")
        log_ekrani.geometry("950x500")
        log_ekrani.configure(bg=R["arkapanel"])

        lbl_log=tk.Label(log_ekrani,text="İŞLEM GEÇMİŞİ",font=("Impact",18),bg=R["arkapanel"],fg=R["sari"])
        lbl_log.pack(pady=10)

        style=ttk.Style()
        style.configure("Treeview",rowheight=25)
        sutunlar=("Log ID","Tarih","İşlem Türü","Oyuncu ID","Açıklama")
        tree=ttk.Treeview(log_ekrani,columns=sutunlar,show="headings",height=15)
        tree.heading("Log ID",text="Log ID")
        tree.column("Log ID",width=60,anchor="center")
        tree.heading("Tarih",text="Tarih / Saat")
        tree.column("Tarih",width=140,anchor="center")
        tree.heading("İşlem Türü",text="İşlem Türü")
        tree.column("İşlem Türü",width=120,anchor="center")
        tree.heading("Oyuncu ID",text="Oyuncu ID")
        tree.column("Oyuncu ID",width=90,anchor="center")
        tree.heading("Açıklama",text="Açıklama")
        tree.column("Açıklama",width=500,anchor="w")
        kayan_cubuk=ttk.Scrollbar(log_ekrani,orient="vertical",command=tree.yview)
        tree.configure(yscrollcommand=kayan_cubuk.set)        
        tree.pack(side="left",fill="both",expand=True,padx=10,pady=10)
        kayan_cubuk.pack(side="right",fill="y",pady=10)

        kayitlar=self.vt.loglari_getir()
        if kayitlar:
            for kayit in kayitlar:
                tarih=kayit[1].strftime("%d.%m.%Y %H:%M")
                tree.insert("","end",values=(kayit[0],tarih,kayit[2],kayit[3],kayit[4]))
        else:
            tree.insert("","end",values=("-","KAYIT YOK","-","-","-"))
    
    def rapor_penceresi(self):
        rapor_ekrani=tk.Toplevel(self.pencere)
        rapor_ekrani.title("Raporlar")
        rapor_ekrani.geometry("600x500")
        rapor_ekrani.configure(bg=R["arkapanel"])

        lbl_baslik=tk.Label(rapor_ekrani,text="En İyi Oyuncular",font=("Impact",18),bg=R["arkapanel"],fg=R["sari"])
        lbl_baslik.pack(pady=15)

        style=ttk.Style()
        style.configure("Treeview",rowheight=25)      
        sutunlar=("Kategori","Oyuncu Adı","Sınıf","Değer (Gold/Lvl)")
        tree=ttk.Treeview(rapor_ekrani,columns=sutunlar,show="headings",height=15)        
        tree.heading("Kategori",text="Kategori")
        tree.column("Kategori",width=150,anchor="center")
        tree.heading("Oyuncu Adı",text="Oyuncu Adı")
        tree.column("Oyuncu Adı",width=150,anchor="center")
        tree.heading("Sınıf",text="Sınıf")
        tree.column("Sınıf",width=100,anchor="center")
        tree.heading("Değer (Gold/Lvl)",text="Değer")
        tree.column("Değer (Gold/Lvl)",width=120,anchor="center")
        tree.pack(fill="both",expand=True,padx=20,pady=10)
        
        veriler=self.vt.raporlari_getir()
        if veriler:
            for veri in veriler:
                tree.insert("","end",values=(veri[0],veri[1],veri[2],veri[3]))
        else:
            messagebox.showinfo("Bilgi","Henüz yeterli veri yok.")

    def cikis_yap(self):
        cevap=messagebox.askyesno("Çıkış","Uygulamayı kapatmak istiyor musun ?")
        if cevap:
            self.pencere.destroy()

    def baslat(self):
        self.pencere.mainloop()
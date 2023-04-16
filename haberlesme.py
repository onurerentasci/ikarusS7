class GirisBilgileri:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre

class SunucuSaati:
    def __init__(self, gun, saat, dakika, saniye, milisaniye):
        self.gun = gun
        self.saat = saat
        self.dakika = dakika
        self.saniye = saniye
        self.milisaniye = milisaniye

class TelemetriVerisi:
    def __init__(self, takim_numarasi, iha_enlem, iha_boylam, iha_irtifa, iha_hiz, iha_otonom, iha_kilitlenme, Hedef_merkez_X, Hedef_merkez_Y, Hedef_genislik, Hedef_yukseklik, GPSSaati):
        self.takim_numarasi = takim_numarasi
        self.iha_enlem = iha_enlem
        self.iha_boylam = iha_boylam
        self.iha_irtifa = iha_irtifa
        self.iha_hiz = iha_hiz
        self.iha_otonom = iha_otonom
        self.iha_kilitlenme = iha_kilitlenme
        self.Hedef_merkez_X = Hedef_merkez_X
        self.Hedef_merkez_Y = Hedef_merkez_Y
        self.Hedef_genislik = Hedef_genislik
        self.Hedef_yukseklik = Hedef_yukseklik
        self.GPSSaati = GPSSaati

class KilitlenmeBilgisi:
    def __init__(self, kilitlenmeBaslangicZamani, kilitlenmeBitisZamani, otonom_kilitlenme):
        self.kilitlenmeBaslangicZamani = kilitlenmeBaslangicZamani
        self.kilitlenmeBitisZamani = kilitlenmeBitisZamani
        self.otonom_kilitlenme = otonom_kilitlenme

# class GirisBilgileri:
#     def __init__(self, kullanici_adi, sifre):
#         self.kullanici_adi = kullanici_adi
#         self.sifre = sifre

# class SunucuSaati:
#     def __init__(self, gun, saat, dakika, saniye, milisaniye):
#         self.gun = gun
#         self.saat = saat
#         self.dakika = dakika
#         self.saniye = saniye
#         self.milisaniye = milisaniye

# class TelemetriVerisi:
#     def __init__(self, takim_numarasi, iha_enlem, iha_boylam, iha_irtifa, iha_hiz, iha_otonom, iha_kilitlenme, Hedef_merkez_X, Hedef_merkez_Y, Hedef_genislik, Hedef_yukseklik, GPSSaati):
#         self.takim_numarasi = takim_numarasi
#         self.iha_enlem = iha_enlem
#         self.iha_boylam = iha_boylam
#         self.iha_irtifa = iha_irtifa
#         self.iha_hiz = iha_hiz
#         self.iha_otonom = iha_otonom
#         self.iha_kilitlenme = iha_kilitlenme
#         self.Hedef_merkez_X = Hedef_merkez_X
#         self.Hedef_merkez_Y = Hedef_merkez_Y
#         self.Hedef_genislik = Hedef_genislik
#         self.Hedef_yukseklik = Hedef_yukseklik
#         self.GPSSaati = GPSSaati

# class KilitlenmeBilgisi:
#     def __init__(self, kilitlenmeBaslangicZamani, kilitlenmeBitisZamani, otonom_kilitlenme):
#         self.kilitlenmeBaslangicZamani = kilitlenmeBaslangicZamani
#         self.kilitlenmeBitisZamani = kilitlenmeBitisZamani
#         self.otonom_kilitlenme = otonom_kilitlenme


class TelemetriVerisi:
    def __init__(self):
        self.takim_numarasi = 0
        self.iha_enlem = 0.0
        self.iha_boylam = 0.0
        self.iha_irtifa = 0.0
        self.iha_dikilme = 0.0
        self.iha_yonelme = 0.0
        self.iha_yatis = 0.0
        self.iha_hiz = 0.0
        self.iha_batarya = 0
        self.iha_otonom = False
        self.iha_kilitlenme = False
        self.Hedef_merkez_X = 0
        self.Hedef_merkez_Y = 0
        self.Hedef_genislik = 0
        self.Hedef_yukseklik = 0
        self.GPSSaati = SunucuSaati()

class SunucuSaati:
    def __init__(self):
        self.saat = 0
        self.dakika = 0
        self.saniye = 0
        self.milisaniye = 0

class Kilitlenme_Bilgisi:
    def __init__(self):
        self.kilitlenmeBasslangicZamanı = SunucuSaati()
        self.kilitlenmeBitisZamanı = SunucuSaati()
        self.otonom_kilitlenme = False

class GirisBilgileri:
    def __init__(self, kadi, sifre):
        self.kadi = kadi
        self.sifre = sifre

import requests
from api_get_post import Api_Get, Api_Post
import time

# Post isteği yapılacak URL
url_giris = "https://savasaniha.baykartech.com/api/giris"
url_sunucusaati = "https://savasaniha.baykartech.com/api/sunucusaati"
url_telemetri = "https://savasaniha.baykartech.com/api/telemetri_gonder"

# Gönderilecek JSON verisi
data = {
    "giris":{
        "kadi" : "ikaruss7",
        "sifre" : "r7pr8zCywP"
        },
    "telemetri":{
        "takim_numarasi": 1,
        "iha_enlem": 41.508775,
        "iha_boylam": 36.118335,
        "iha_irtifa": 38,
        "iha_dikilme": 7,
        "iha_yonelme": 210,
        "iha_yatis": -30,
        "iha_hiz": 28,
        "iha_batarya": 50,
        "iha_otonom": 1,
        "iha_kilitlenme": 1,
        "hedef_merkez_X": 300,
        "hedef_merkez_Y": 230,
        "hedef_genislik": 30,
        "hedef_yukseklik": 43,
        "gps_saati": {
            "saat": 11,
            "dakika": 38,
            "saniye": 37,
            "milisaniye": 654
            }
        },
            
        "kilitlenme_bilgisi": {
            "kilitlenmeBaslangicZamani": {
                "saat":14,
                "dakika":43,
                "saniye":21, 
                "milisaniye":421
            },
            "kilitlenmeBitisZamani": {
                "saat": 14,
                "dakika":43,
                "saniye": 26,
                "milisaniye": 421
            },
            "otonom_kilitlenme": 0
        },
        "kamikaze_bilgisi": {
            "kamikazeBaslangicZamani": {
                "saat":14,
                "dakika": 51,
                "saniye": 21,
                "milisaniye": 512
            },
            "kamikazeBitisZamani": {
                "saat": 14,
                "dakika": 51,
                "saniye": 25,
                "milisaniye":99
            },
            "qr_metni": "teknofest2023"
                }
            }


session = requests.Session()
response_giris = session.post(url_giris,json=data["giris"])
print(response_giris)

response_saat = Api_Get(url_sunucusaati)
sunucusaati = response_saat.json()
print(sunucusaati["saat"])

# while True:
#     response_telemetri = session.post(url_telemetri,json=data["telemetri"])
#     print(response_telemetri)
#     print(response_telemetri.text)

#     # 1 saniyelik bekleme süresi ekle
#     time.sleep(1)
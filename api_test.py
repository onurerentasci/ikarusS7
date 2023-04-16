import requests
from api_get_post import Api_Get, Api_Post
import time

# Post isteği yapılacak URL
url_giris = "http://10.0.0.10:10001/api/giris"
url_sunucusaati = "https://10.0.0.10:10001/api/sunucusaati"
url_telemetri = "https://10.0.0.10:10001/api/telemetri_gonder"

# Gönderilecek JSON verisi
data = {
    "giris":{
        "kadi": "ikaruss7",
        "sifre": "r7pr8zCywP"
            },
    "telemetri":{
        "takim_numarasi": 7,
        "iha_enlem": "",
        "iha_boylam": "",
        "iha_irtifa": "",
        "iha_dikilme": "",
        "iha_yonelme": "",
        "iha_yatis": "",
        "iha_hiz": "",
        "iha_otonom": "",
        "iha_kilitlenme": "",
        "hedef_merkez_x": "",
        "hedef_merkez_y": "",
        "hedef_genislik": "",
        "hedef_yukseklik": "",
        "gps_saati":{
            "saat":"",
            "dakika":"",
            "saniye":"",
            "milisaniye":""
        },
            
        "kilitlenme_bilgisi": {
            "kilitlenmeBaslangicZamani": "",
            "kilitlenmeBitisZamani": "",
            "otonom_kilitlenme": ""
        },
        "kamikaze_bilgisi": {
            "kamikazeBaslangicZamani": "",
            "kamikazeBitisZamani": "",
            "qr_metni": ""
                }
            }
        }

Api_Post(url_giris, data["giris"], data["giris"]["kadi"], data["giris"]["sifre"])

while True:
    Api_Post(url_telemetri, data["telemetri"], data["giris"]["kadi"], data["giris"]["sifre"])
    time.sleep(2000)


# Api_Get(url_sunucusaati)


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
        "kadi": "ikaruss7",
        "sifre": "r7pr8zCywP"
            },
    "telemetri":{
        "takim_numarasi": 7,
        "iha_enlem": 21.23,
        "iha_boylam": 11.02,
        "iha_irtifa": 10,
        "iha_dikilme": 42,
        "iha_yonelme": 12,
        "iha_yatis": 4,
        "iha_hiz": 45,
        "iha_otonom": 0,
        "iha_kilitlenme": 1,
        "hedef_merkez_x": 57,
        "hedef_merkez_y": 15,
        "hedef_genislik": 33,
        "hedef_yukseklik": 21,
        "gps_saati":{
            "saat":13,
            "dakika":57,
            "saniye":12,
            "milisaniye":2143
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

import requests
from api_get_post import Api_Get, Api_Post
import time

# Post isteği yapılacak URL
url_giris = "https://savasaniha.baykartech.com/api/api/giris"
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
        "iha_enlem": "21",
        "iha_boylam": "11",
        "iha_irtifa": "1",
        "iha_dikilme": "42",
        "iha_yonelme": "12",
        "iha_yatis": "4",
        "iha_hiz": "45",
        "iha_otonom": "True",
        "iha_kilitlenme": "True",
        "hedef_merkez_x": "57",
        "hedef_merkez_y": "15",
        "hedef_genislik": "33",
        "hedef_yukseklik": "21",
        "gps_saati":{
            "saat":"13",
            "dakika":"57",
            "saniye":"12",
            "milisaniye":"2143"
        },
            
        "kilitlenme_bilgisi": {
            "kilitlenmeBaslangicZamani": "13:58:02:123",
            "kilitlenmeBitisZamani": "13:58:05:542",
            "otonom_kilitlenme": "True"
        },
        "kamikaze_bilgisi": {
            "kamikazeBaslangicZamani": "14:02:42:622",
            "kamikazeBitisZamani": "14:05:12:123",
            "qr_metni": "teknofest2023"
                }
            }
        }

Api_Post(url_telemetri, data["telemetri"], data["giris"]["kadi"], data["giris"]["sifre"])
time.sleep(2)

# Api_Get(url_sunucusaati)


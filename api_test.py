import requests
from api_get_post import Api_Get, Api_Post

# Post isteği yapılacak URL
url_giris = "https://savasaniha.baykartech.com/api/giris"
url_sunucusaati = "https://savasaniha.baykartech.com/api/sunucusaati"
url_telemetri = "https://savasaniha.baykartech.com/api/"

# Gönderilecek JSON verisi
data = {
    "giris":{
        "kadi": "ikaruss7",
        "sifre": "r7pr8zCywP"
            },
    "telemetri":{
        'takim_numarasi': 10,
        'iha_enlem': "current_lat",
        'iha_boylam': "current_lon",
        'iha_irtifa': "current_alt",
        'iha_dikilme': "pitch",   # pitch
        'iha_yonelme': "yaw",  # yaw
        'iha_yatis': "roll",  # roll
        'iha_hiz': "",
        'iha_otonom': False if  "" else True,
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

# Api_Post(url_giris, data["giris"], data["giris"]["kadi"], data["giris"]["sifre"])


# Api_Get(url_sunucusaati)


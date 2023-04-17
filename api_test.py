# import requests
# from api_get_post import Api_Get, Api_Post
# import time

# # Post isteği yapılacak URL
# url_giris = "https://savasaniha.baykartech.com/api/giris"
# url_sunucusaati = "https://savasaniha.baykartech.com/api/sunucusaati"
# url_telemetri = "https://savasaniha.baykartech.com/api/telemetri_gonder"

# # Gönderilecek JSON verisi
# data = {
#     "giris":{
#         "kadi": "ikaruss7",
#         "sifre": "r7pr8zCywP"
#             },
#     "telemetri":{
#         "takim_numarasi": 7,
#         "iha_enlem": 21.23,
#         "iha_boylam": 11.02,
#         "iha_irtifa": 10,
#         "iha_dikilme": 42,
#         "iha_yonelme": 12,
#         "iha_yatis": 4,
#         "iha_hiz": 45,
#         "iha_otonom": 0,
#         "iha_kilitlenme": 1,
#         "hedef_merkez_x": 57,
#         "hedef_merkez_y": 15,
#         "hedef_genislik": 33,
#         "hedef_yukseklik": 21,
#         "gps_saati":{
#             "saat":13,
#             "dakika":57,
#             "saniye":12,
#             "milisaniye":2143
#         }
#     },
            
#         "kilitlenme_bilgisi": {
#             "kilitlenmeBaslangicZamani": {
#                 "saat":14,
#                 "dakika":43,
#                 "saniye":21, 
#                 "milisaniye":421
#             },
#             "kilitlenmeBitisZamani": {
#                 "saat": 14,
#                 "dakika":43,
#                 "saniye": 26,
#                 "milisaniye": 421
#             },
#             "otonom_kilitlenme": 0
#         },
#         "kamikaze_bilgisi": {
#             "kamikazeBaslangicZamani": {
#                 "saat":14,
#                 "dakika": 51,
#                 "saniye": 21,
#                 "milisaniye": 512
#             },
#             "kamikazeBitisZamani": {
#                 "saat": 14,
#                 "dakika": 51,
#                 "saniye": 25,
#                 "milisaniye":99
#             },
#             "qr_metni": "teknofest2023"
#                 }
#             }

# session = requests.Session()
# response = session.post(url_giris,json=data["giris"])
# print(response)
# print(response.status_code)
# print(response.text)
# while True:
#     response2 = session.post(url_telemetri,json=data["telemetri"])
#     print(response2)
#     print(response2.text)
#     print(response2.status_code)

#     time.sleep(0.25)

import requests
import json
import time

telemetry_url = "https://savasaniha.baykartech.com/api/telemetri_gonder"
position_url = "https://savasaniha.baykartech.com/api/telemetri_gonder"
response = requests.Session()
response.post("https://savasaniha.baykartech.com/api/giris",json={"kadi" : "ikaruss7", "sifre" :  "r7pr8zCywP"})
def send_telemetry(telemetry_data):
    
    headers = {'Content-type': 'application/json'}
    response = requests.post(telemetry_url, data=json.dumps(telemetry_data), headers=headers)
    if response.status_code == 200:
        print("Telemetri verileri başarıyla gönderildi.")
    else:
        print("Telemetri verileri gönderirken hata oluştu.")
   
def get_positions():
    response = requests.get(position_url)
    if response.status_code == 200:
        data = json.loads(response.text)
        print("Konum bilgileri alındı.")
        return data
    else:
        print("Konum bilgileri alırken hata oluştu.")

# Telemetri verileri oluşturma
telemetry_data = {
    "takim_numarasi": 10,
    "IHA_enlem": 43.576546,
    "IHA_boylam": 22.385421,
    "IHA_irtifa": 100,
    "IHA_dikilme": 5,
    "IHA_yonelme": 256,
    "IHA_yatis": 0,
    "IHA_hiz": 223,
    "IHA_batarya": 20,
    "IHA_otonom": 0,
    "IHA_kilitlenme": 1,
    "Hedef_merkez_X": 315,
    "Hedef_merkez_Y": 220,
    "Hedef_genislik": 12,
    "Hedef_yukseklik": 46,
    "GPSSaati": {
        "saat": 19,
        "dakika": 1,
        "saniye": 23,
        "milisaniye": 507
    }
}

# Telemetri verilerini gönderme
send_telemetry(telemetry_data)

# Diğer takımların konum bilgilerini alma
positions = get_positions()

# # Konum bilgilerini işleme
# for position in positions:
#     timestamp = position["timestamp"]
#     lat = position["latitude"]
#     lon = position["longitude"]
#     time_diff = position["time_diff"]
#     print("Takımın konumu: ({}, {}), Saat farkı: {} ms".format(lat, lon, time_diff))

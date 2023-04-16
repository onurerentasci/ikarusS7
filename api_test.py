import requests
from api_get_post import Api_Get, Api_Post

# Post isteği yapılacak URL
url = "https://savasaniha.baykartech.com/api/giris"

# Gönderilecek JSON verisi
data = {
    "kadi": "ikaruss7",
    "sifre": "r7pr8zCywP"
}

# # Post isteği yap ve yanıtı al
# response = requests.post(url, json=data)

# # İşlem başarılıysa yanıt kodunu yazdır
# if response.ok:
#     print(requests.post(url, json=data))
# else:
#     print('Post request failed')


# response = requests.get(url)

# if response.ok:
#     print(requests.get(url))
# else:
#     print("request failed")


Api_Post(url, data, "ikaruss7", "r7pr8zCywP")
# response = Api_Get(url)
# data = response.json()
# print(type(data["gun"]))
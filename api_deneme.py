import requests
URL = "https://random-data-api.com/api/bank/random_bank?size=3"
response = requests.get(url=URL)
status_code = response.status_code
if status_code == "<Request [200]>":
    print("success")
else:
    print("fail")

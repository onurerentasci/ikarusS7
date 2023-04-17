import cv2
import pyzbar.pyzbar as pyzbar
import json
import requests

url = "http://savasaniha.baykartech.com/api/giris"
url_kamikaze="https://savasaniha.baykartech.com/api/kamikaze_bilgisi"
data = {
    "giris":{
        "kadi": "ikaruss7",
        "sifre": "r7pr8zCywP"
            }
}
session = requests.Session()
response = session.post(url, json=data["giris"])
print(response.status_code)
# if response.status_code != 200:
#     #raise ValueError('Oturum açma başarısız oldu')
#     print(response.status_code)
def post_json_data(json_data):
    response = session.post(url, json=json_data)
    if response.status_code == 200:
        print('JSON verisi sunucuya gönderildi')
    else:
        print('JSON verisi sunucuya gönderilemedi')

cap = cv2.VideoCapture(0)
cap.set(3, 640) 
cap.set(4, 480) 
while True:
    ret, frame = cap.read()
    if not ret:
        continue
    
    decoded_objs = pyzbar.decode(frame)
    for obj in decoded_objs:
        qr_data = {"QR Kodu İçeriği": obj.data.decode()}
        json_data = json.dumps(qr_data)
        print("JSON Verisi:", json_data)

        with open("data.json", "w") as f:
            json.dump(qr_data, f)
            print("JSON Verisi dosyaya yazdırıldı.")
        
        # JSON verisini sunucuya gönder
        post_json_data(qr_data)
    
    cv2.imshow("QR Kodu Okuyucu", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

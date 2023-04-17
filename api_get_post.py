import json
import requests

def Api_Get(adres):
    try:
        session = requests.Session()
        response = session.get(adres)
        if response.status_code == requests.codes.ok:
            return response
        
        else:
            return response
    except Exception as ex:
        print(ex)
        return None


def Api_Post(adres, model):
    try:
        json_data = json.dumps(model)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        session = requests.Session()
        response = session.post(adres, data=json_data, headers=headers)
        
        if response.status_code == requests.codes.ok:
            print(response)
            return response.text
        else:
            print(response)
            return response            

    except Exception as ex:
        print(ex)
        return None

client = requests.Session()
 
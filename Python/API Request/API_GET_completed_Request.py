import requests
import time


User_ID = "mohan12.prakash89@gmail.com"
Video_ID = "V2241599357364169_mohan12.prakash89@gmail.com_URL_979"


url = f'https://mediafirewall-ai.millionvisions.ai/mfw/model/config/{User_ID}/{Video_ID}'

params = {
  'apikey': 'Xi1G9pVWAacYW6hthVCiXBnfSTOHL4Rh',
}

response_json = requests.get(url, params=params).json()

while True:
    if response_json.get("processStatus", {}).get("complete", False):
        print(response_json)
        break
    time.sleep(1)  # Wait for 1 second before checking again

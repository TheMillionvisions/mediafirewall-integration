import requests

userID = "mohan12.prakash89@gmail.com"
webhooks = [
        "https://webhook-test.com/bcf2fcc633795f6a00371475c3e301ef"
        ]

url = "https://mediafirewall-ai.millionvisions.ai/notification/webhook"

body = {
    "userId" : userID,
    "webhooks" : webhooks
}

headers = {'Content-Type': 'application/json'}

params = {
  'apikey': 'Xi1G9pVWAacYW6hthVCiXBnfSTOHL4Rh'
}

response = requests.post(url,params=params,json=body ,headers=headers)

if response.status_code == 201:
    print("POST request sent successfully.")       
else:
    print("Failed to send POST request. Status code:", response.status_code)
    print("Response content:", response.content)


import requests

userID = "" #provide your userId here 
webhooks = [
        "https://example.com/webhook","https://example1.com/webhook"
        ]

url = "https://mediafirewall-ai.millionvisions.ai/notification/webhook"

body = {
    "userId" : userID,
    "webhooks" : webhooks
}

headers = {'Content-Type': 'application/json'}

params = {
  'apikey': '' #provide your apikey here
}

response = requests.post(url,params=params,json=body ,headers=headers)

if response.status_code == 201:
    print("POST request sent successfully.")       
else:
    print("Failed to send POST request. Status code:", response.status_code)
    print("Response content:", response.content)


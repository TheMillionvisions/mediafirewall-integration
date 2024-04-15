# from flask import Flask, request
# import requests

# app = Flask(__name__)
# subscription_activated = False

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     global subscription_activated
#     data = request.json

#     if 'subscription_url' in data and not subscription_activated:
#         subscription_url = data['subscription_url']
#         response = requests.get(subscription_url)
#         if response.status_code == 200:
#             subscription_activated = True
#             return 'Subscription activated successfully', 200
#         else:
#             return 'Failed to activate subscription', 400

#     else:
#         print(data)
#         return 'Request received successfully', 200

# if __name__ == '__main__':
#     app.run(host= "10.10.6.246" ,port=5000 ,debug=True)



from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():

    data = request.data.decode("utf-8") 
    if data:
        if 'SubscribeURL' in data:
            subscribe_url = data.split('"SubscribeURL": "')[1].split('"')[0]
            response = requests.get(subscribe_url)
            if response.status_code == 200:
                return 'Subscription activated successfully', 200
            else:
                return 'Failed to activate subscription', 400

        else:
            print(data)
            return 'Request received successfully', 200
    else:
        return 'Empty request', 400

if __name__ == '__main__':
    app.run(host= "localhost" ,port=5000 ,debug=True)
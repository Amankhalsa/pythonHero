# Acess Data of the Crypto currency


# Get data of BitCoin
# Track Changes in Live Mode(time)


import requests
import time

while True:
    url = 'https://api.coincap.io/v2/assets'
    data = requests.get(url)
    # print(data)
    # 200 all is well
    # 404 error
    currency = data.json()
    # print(currency["data"])
    # for i in range(len(currency["data"])):
    #     result = currency["data"][i]["priceUsd"]
    #     print(result)
    bitcoin = currency["data"][0]['priceUsd']
    print(f'The current value of bitcoin is {bitcoin} USD')
    time.sleep(10)
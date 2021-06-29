import requests
# api
url = 'https://api.exchangerate-api.com/v4/latest/eur'

data = requests.get(url)

exchage_api = data.json()
rates = exchage_api['rates']
print("indian",rates["INR"])

indian=rates["INR"]
# for key,value in rates.items():
#  print(key,value)

usr_amt = int(input('Enter amount : '))
usr_cur = input('Cur Type : ').upper()

if usr_cur in rates.keys():
    # for key,value in rates.items():
    #     if rates[f'{usr_cur}'] == usr_cur:
    #         print("hi")
    #     else:
    #         print(rates[f"{usr_cur}"])
    #         break
    print("USD",rates[f'{usr_cur}'] )
    conv_cur = usr_amt * rates[f'{usr_cur}']

    print(f'For {usr_amt}  you will get {conv_cur} {usr_cur} ')

else:
    print(f'{usr_cur} Does not exist')

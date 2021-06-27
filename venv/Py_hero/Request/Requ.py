
#Request
#Http GET AND POST
# .GET
# .content
# API

import requests
url = 'https://api.exchangerate-api.com/v4/latest/eur'
test = requests.get(url)

info = test.json()

# print(info.values())
# print(info.values())
for key,value in info.items():
	print(key,"=", value)
# url = 'https://www.youtube.com/'
# test = requests.get(url)
# info = test.content
# print(info)

# url="https://www.youtube.com/"
# test=requests.get(url)
#
# info=test.content
# print(test)
# print(info)


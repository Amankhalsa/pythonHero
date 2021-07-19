# from win32com.client import Dispatch
# def speak(string):
# 	said=Dispatch("SAPI.Spvoice")
# 	said.speak(string)
# # a ="""Lorem Ipsum is simply dummy text of the printing
# #  and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever
# #   since the 1500s, when an unknown printer took a galley of type and scrambled it to make
# #    a type specimen book. It has survived not only five centuries, but also the leap into
# #     electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s
# #      with the release of Letraset sheets containing Lorem Ipsum passages, and more recently
# #       with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
# s=input("Give a sentance to speak:")
# # s=a

# speak(s)


# calendar using python 
# import calendar 
# year =2021
# print(calendar.calendar(year))

# # Decimal to binary 
# decNum =int(input("number :"))
# binNum = bin(decNum)
# print(binNum[2:])

# binary  to Decimal
# binNum =int(input("number :"))
# decNum = int(str(binNum),2)
# print(decNum)

# Genrate captcha img

# from captcha.image import imagecaptcha
# import random
# img = imageCaptcha()
# randomNum= random.randint(1000, 9999)
# saveImage=img.write(str(randomNum),"Captcha2.png")


# For valid email checing
# from verify_email import verify_email

# email =input("enter email:")
# print("validating...")
# if verify_email(email):
# 	print("yes this is valid email")
# else:
# 	print("no  this is not valid email")
# importing subprocess

# Wifi password chec 

# first we will import the subprocess module
# import subprocess

# # now we will store the profiles data in "data" variable by 
# # running the 1st cmd command using subprocess.check_output
# data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# # now we will store the profile by converting them to list
# profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# # using for loop in python we are checking and printing the wifi 
# # passwords if they are available using the 2nd cmd command
# for i in profiles:

#     # running the 2nd cmd command to check passwords
#     results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 
#                         'key=clear']).decode('utf-8').split('\n')
#     # storing passwords after converting them to list
#     results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#     # printing the profiles(wifi name) with their passwords using 
#     # try and except method 
#     try:
#         print ("{:<30}|  {:<}".format(i, results[0]))
#     except IndexError:
#         print ("{:<30}|  {:<}".format(i, ""))

#         netsh wlan show profile
# netsh wlan show profile PROFILE-NAME key=clear


# text_to_handweitting
import pywhatkit
pywhatkit.text_to_handwriting(" python is an programing lanuage",rgb=(0,0,255))




# import time
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse('<h1>This is a http response</h1>')

from django.shortcuts import render
def home(request):
    return render(request,"About.html")
def contact(request):
    return render(request,"contact.html")
def thanks(request):
    return render(request,"thx.html")
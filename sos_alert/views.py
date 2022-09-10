from django.shortcuts import render, HttpResponse
from . import send_sms

# Create your views here.
def alert(request):
    send_sms.send_alert(request.user.username, '+16124828726', '+919049917706')
    return HttpResponse("Hi")
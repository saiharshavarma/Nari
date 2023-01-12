from django.shortcuts import render, HttpResponse
from accounts.models import EmergencyContact, Profile
import requests
import json
from . import send_sms

# Create your views here.

api_key = 'b8463a85322f44f79bdfde1565d59719'
api_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + api_key


def alert(request):
    # Sending alert to nearby devices

    # Sending alert to all emergency contacts
    econtacts = EmergencyContact.objects.filter(user=request.user)
    name = str(request.user.first_name + ' ' + request.user.last_name)
    for econtact in econtacts:
        send_sms.send_alert(name, '+16124828726', econtact.mobile)
    inSOSRange(request)
    return HttpResponse("Hi")


def inSOSRange(request):
    profiles = list(Profile.objects.all())
    user = request.user
    name = str(user.first_name + ' ' + user.last_name)
    for profile in profiles:
        # Google API from profile location to user's location
        distance = 10
        if distance < 20:
            send_sms.send_alert(name, '+16124828726', profile.mobile)
    return None


def getGeoLocation(ip):
    response = requests.get(api_url + "&ip_address=" + ip)
    print(response.content)
    geolocation_data = json.loads(response.content)
    latitude = geolocation_data['latitude']
    longitude = geolocation_data['longitude']
    return latitude, longitude


def getAllUserLocation(request):
    profiles = list(Profile.objects.all())
    for profile in profiles:
        ip = profile.ip
        print(ip)
        profile.latitude, profile.longitude = getGeoLocation(ip)
        profile.save()
    return HttpResponse("Hi")


def tempHome(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    ip = "157.51.83.237"
    profile = Profile.objects.get(user=request.user)
    profile.ip = ip
    profile.save()
    return HttpResponse("tempHome")

from django.shortcuts import render, HttpResponse
from accounts.models import EmergencyContact
from . import send_sms

# Create your views here.
def alert(request):
    # Sending alert to nearby devices

    # Sending alert to all emergency contacts
    econtacts = EmergencyContact.objects.filter(user = request.user)
    name = str(request.user.first_name + ' ' + request.user.last_name)
    for econtact in econtacts:
        send_sms.send_alert(name, '+16124828726', '+919049917706')
    return HttpResponse("Hi")
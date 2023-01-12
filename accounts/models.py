from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = PhoneNumberField(blank=False)
    ip = models.TextField(null=True)
    latitude = models.TextField(null=True)
    longitude = models.TextField(null=True)

    def __str__(self):
        return str(f'{self.user.id}' + ' ' + f'{self.user.username}' + ' ' + f'{self.mobile}')


class EmergencyContact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    mobile = PhoneNumberField(blank=False)
    relation = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str("Emergency contact of " + f'{self.user.username}' + ': ' + f'{self.name}' + ' ' + f'{self.mobile}')

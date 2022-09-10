from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.IntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])

    def __str__(self):
        return str(f'{self.user.id}' + ' ' + f'{self.user.username}' + ' ' + f'{self.mobile}')

class EmergencyContact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)    
    mobile = models.IntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])

    def __str__(self):
        return str("Emergency contact of " + f'{self.user.username}' + ': ' + f'{self.name}' + ' ' + f'{self.mobile}')

    
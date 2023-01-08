from django.contrib import admin
from .models import EmergencyContact, Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'mobile')


class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'mobile', 'relation')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(EmergencyContact, EmergencyContactAdmin)


from django.urls import path
from . import views

urlpatterns = [
    path('alert/', views.alert, name='alert'),
    path('prof/', views.getAllUserLocation, name='prof'),
    path('', views.tempHome, name='tempHome'),
]

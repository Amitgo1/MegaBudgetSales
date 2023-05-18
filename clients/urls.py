from django.urls import path
from clients.views import clients

urlpatterns = [
    path('', clients),
    
]
from django.urls import path
from category.views import category

urlpatterns = [
    path('', category),
    
]
from django.urls import path
from main.views import index,register,login3,logout1

urlpatterns = [
    path('', index, name="index"),
    path('register/',register, name="register"),
    path('login3/',login3, name="login3"),
    path('logout1/', logout1 , name="logout1")
    
    # path('login/',login_page , name="login"),
    # path('logout/',logout_page , name="logout"),
    
]
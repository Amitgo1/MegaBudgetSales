from django import forms
from main.models import MyUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password

class MyForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ("username","email","phone","password")
        
    def clean_password(self):
        password = self.cleaned_data["password"]
        validate_password(password)
        password = make_password(password)
        return password
    
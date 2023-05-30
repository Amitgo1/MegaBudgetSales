from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13,unique=True)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.username
    
class MyEmail(models.Model):
    email = models.EmailField()


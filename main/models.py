from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
class MyEmail(models.Model):
    email = models.EmailField()


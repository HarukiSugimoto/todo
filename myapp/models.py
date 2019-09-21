from django.db import models

# Create your models here.
class Login(models.Model):
    mail_address = models.EmailField()
    password = models.CharField(max_length=10)

class Register(models.Model):
    user_name = models.CharField(max_length=10)
    mail_address = models.EmailField()
    password = models.CharField(max_length=10)
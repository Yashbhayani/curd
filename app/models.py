import email
from unicodedata import name
from django.db import models

# Create your models here.

class Master_User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)

class Customer(models.Model):
    user_fk = models.ForeignKey(Master_User,on_delete=models.CASCADE)
    name = models.TextField(max_length=10)
    city = models.TextField(max_length=20)

class seller(models.Model):
    user_fk = models.ForeignKey(Master_User,on_delete=models.CASCADE)
    name = models.TextField(max_length=10)
    shop_name =models.TextField(max_length=20)
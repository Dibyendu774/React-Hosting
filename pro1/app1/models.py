from django.db import models

# Create your models here.

class Users(models.Model):
    fullname = models.CharField(max_length=20)  # firstname
    lastname = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15, null=True, blank=True)
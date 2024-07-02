from django.db import models

# Create your models here.
class Enquiry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    contactno = models.CharField(max_length=10)
    emailaddress = models.CharField(max_length=100)
    subject = models.CharField(max_length=500)
    message = models.CharField(max_length=5000)
    posteddate = models.CharField(max_length=30)

class Customer(models.Model):
    name  = models.CharField(max_length=50)
    gender = models.CharField(max_length=6)
    address = models.CharField(max_length=500)
    contactno = models.CharField(max_length=10)
    emailaddress = models.EmailField(max_length=100,primary_key=True)
    regdate = models.CharField(max_length=30)

class Login(models.Model):
    userid = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=30)
    usertype = models.CharField(max_length=30)
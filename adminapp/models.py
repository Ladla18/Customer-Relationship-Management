from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=500)
    mfgdate = models.CharField(max_length=30)
    expdate = models.CharField(max_length=30)
    price = models.IntegerField()
    productpic = models.FileField(upload_to='')
    avail= models.CharField(max_length=5)
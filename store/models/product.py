from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=800)
    price = models.FloatField()
    description = models.TextField()
    imglink = models.CharField(max_length=800)

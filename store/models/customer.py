from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    middle_name = models.CharField(max_length=400)
    email = models.CharField(max_length=400)
    number = models.CharField(max_length=400)
    street = models.CharField(max_length=600)
    city = models.CharField(max_length=400)
    district = models.CharField(max_length=400)
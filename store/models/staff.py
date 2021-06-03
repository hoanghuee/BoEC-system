from django.db import models


class Staff(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    address = models.CharField(max_length=600)
    position = models.CharField(max_length=400)

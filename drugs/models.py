from django.contrib.auth.models import User
from django.db import models
from store.models import *


class Drugs(models.Model):
    pharmacy = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    expiry_date = models.DateTimeField()

from django.contrib.auth.models import User
from django.db import models


class Store(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

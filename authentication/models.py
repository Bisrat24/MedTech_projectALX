from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


CHOICES = [('pharmacy', 'Pharmacy'), ('user', 'User')]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(choices=CHOICES, max_length=10)

    def __str__(self):
        return self.user.username

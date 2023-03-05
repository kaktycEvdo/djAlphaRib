from django.db import models


class CatItem(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=6)
    characteristics = models.TextField(max_length=500)
    links = models.TextField(max_length=200)


class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    is_authorised = models.BooleanField(default=False)

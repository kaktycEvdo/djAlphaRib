from django.db import models
from django.contrib.auth.models import User


class CatItem(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=6)
    characteristics = models.TextField(max_length=500)
    characteristics_long = models.TextField(max_length=1000)
    links = models.TextField(max_length=200)
    image = models.FilePathField(path="alpha/templates/media")


class FavItems(models.Model):
    acpk = models.ForeignKey(User, on_delete=models.CASCADE)
    itpk = models.OneToOneField(CatItem, on_delete=models.SET_NULL, null=True)
    favd = models.BooleanField(default=False)

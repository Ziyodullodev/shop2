from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    ism = models.CharField(max_length=50)
    rasm = models.FileField(upload_to="client",   blank=True)
    email = models.EmailField()
    tel = models.CharField(max_length=30, blank=True)
    jins = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.ism

class Adress(models.Model):
    davlat = models.CharField(max_length=50)
    shahar = models.CharField(max_length=50, blank=True)
    kocha = models.CharField(max_length=50, blank=True)
    uy = models.CharField(max_length=30, blank=True)
    zipcode = models.PositiveIntegerField(blank=True, null=True)
    mijoz = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f" {self.kocha}, {self.uy}"


from django.db import models

# Create your models here.
# class tryst(models.Model):
#     username=models.CharField(max_length=50)
#     password=models.CharField(max_length=50)


class tryst(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    captur = models.CharField(max_length=20)

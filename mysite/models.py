from django.db import models
from django.db.models.aggregates import Max
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.

class Work(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='workimages/')
    summary =models.CharField(max_length=100)


    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=50, null=True)
    message = models.CharField(max_length=1000, null= True)

    def __str__(self):
        return self.name

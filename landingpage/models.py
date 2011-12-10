from django.db import models
from django import forms

# Create your models here.

class Lead(models.Model):
    email =             models.EmailField()
    referrer =          models.CharField(max_length=128)
    date_converted =    models.DateTimeField(auto_now_add=True)
    
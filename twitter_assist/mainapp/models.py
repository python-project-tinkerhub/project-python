from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, primary_key=True)
    password = models.CharField(max_length=20, default=None)
    twitterid = models.CharField(max_length=20)
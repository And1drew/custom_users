from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class custom_user(AbstractUser):
    displayname = models.CharField(max_length = 50) 
    age = models.IntegerField(null = True)

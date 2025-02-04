from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    is_vendor=models.BooleanField(default=False)
    is_buyer=models.BooleanField(default=False)

class Product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)


def __str__(self):
    return self.name
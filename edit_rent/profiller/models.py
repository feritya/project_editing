from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
GENDER_SELECTION = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('NS', 'Not Specified'),
]

class CustomUser(AbstractUser):
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION)
    phone_number = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    adress = models.CharField(max_length=200)








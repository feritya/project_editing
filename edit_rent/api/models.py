from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator
from profiller.models import CustomUser
from PIL import Image

VEHICLE_SELECTION = [
    ('M', 'Motocycle'),
    ('C', 'Car'),
    ('B', 'Bike'),
]


class Vehicle(models.Model):
    category               = models.CharField(max_length=20, choices=VEHICLE_SELECTION)
    vehicle_owner       = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name = 'car' )
    vehicle_location    = models.CharField(max_length=20,null=False)
    model                   = models.CharField(max_length=50)
    seating_capacity   =models.PositiveIntegerField(default=2)
    rent_per_day         = models.PositiveIntegerField( default=100,validators=[MinValueValidator(50)])
    availability             = models.BooleanField(default = True)   #True = available, False = not available   default = True

    about                    = models.TextField(max_length=355,null=True, blank=True)
    arac_foto_1           = models.ImageField(upload_to='car_fotolari/%Y/%m/')
    arac_foto_2           = models.ImageField(null=True,blank=True,upload_to='car_fotolari/%Y/%m/')
    arac_foto_3           = models.ImageField(null=True,blank=True,upload_to='car_fotolari/%Y/%m/')
    def __str__(self):

            return self.model

class Reservation(models.Model):
    customer        = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vehicle            = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    issue_date      = models.DateField()
    return_date    = models.DateField()
    rez_date         = models.DateField(auto_now_add=True)
    total_price      = models.IntegerField()
    
    def __str__(self):
        return str(self.customer) + "- " + str(self.vehicle)


class Favorite(models.Model):
    favorite_user           = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    favorite_vehicle      = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
def __str__(self):
        return self.favorite_vehicle.model







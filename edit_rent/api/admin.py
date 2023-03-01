from django.contrib import admin
from .models import (Car,
                                CarReservation,
                                Favorite
                                )
                                
admin.site.register(CarReservation)
admin.site.register(Car)

# admin.site.register(CarFavorite)

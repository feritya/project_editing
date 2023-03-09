from django.contrib import admin
from .models import (Vehicle,Reservation,Favorite )
                                
admin.site.register(Reservation)
admin.site.register(Vehicle)
admin.site.register(Favorite)


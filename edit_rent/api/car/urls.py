from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import routers
from api.car.views import (

VehicleAPIView,
VehicleSearchAPIView,
VehiclePastRezervationsAPIView,
VehicleReservationsAPIView,
FavoriteAPIView,



)


router = routers.DefaultRouter()   

router.register(r'vehicle', VehicleAPIView,basename ='vehicle' ),
router.register(r'vehicle_reservations',VehicleReservationsAPIView,basename='vehicle_reservations'),
router.register(r'vehicle_past_reservations',VehiclePastRezervationsAPIView,basename='vehicle_past_reservations'),
router.register(r'vehicle_search', VehicleSearchAPIView,basename ='vehicle_search' ),
router.register(r'favorite', FavoriteAPIView,basename ='favorite' ),


urlpatterns = [
    path('',include(router.urls)),
]

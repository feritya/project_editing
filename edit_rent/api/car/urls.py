from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import routers
from api.car.views import CarAPIView,CarReservationsAPIView,CarPastRezervationsAPIView,FavoriteViewSet


router = routers.DefaultRouter()   

router.register(r'car', CarAPIView),
router.register(r'car_reservations',CarReservationsAPIView),
router.register(r'car_past_reservations',CarPastRezervationsAPIView),
router.register(r'favorites', FavoriteViewSet),
urlpatterns = [
    path('',include(router.urls)),
]

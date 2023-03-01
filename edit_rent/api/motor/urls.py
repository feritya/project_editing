from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import routers
from api.motor.views import MotoAPIView,MotoReservationsAPIView,MotoPastRezervationsAPIView,MotoFavoriteViewSet


router = routers.DefaultRouter()   

router.register(r'moto', MotoAPIView),
router.register(r'moto_reservations',MotoReservationsAPIView),
router.register(r'moto_past_reservations',MotoPastRezervationsAPIView),
router.register(r'mfavorites', MotoFavoriteViewSet),
urlpatterns = [
    path('',include(router.urls)),
]

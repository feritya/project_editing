from api.models import (
Car,
CarReservation,
CarFavorite
)
from rest_framework import serializers
from PIL import Image

class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model  =Car
        fields    ='__all__'

class CarReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model    =CarReservation
        fields      = '__all__'

class CarPastReservationSerializer(serializers.ModelSerializer):
    car_model                = serializers.CharField(source='car.model')
    car_rent_per_day      =serializers.IntegerField(source='car.rent_per_day')
    car_arac_foto_1        = serializers.ImageField(source='car.arac_foto_1')


    class Meta:
        model   = CarReservation
        fields     = ('id','car_model','car_rent_per_day','car_arac_foto_1','total_price','rez_date')

class CarFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model   = CarFavorite
        fields     =  '__all__'



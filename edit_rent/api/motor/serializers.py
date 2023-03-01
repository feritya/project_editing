from rest_framework import serializers
from PIL import Image
from api.models import Moto,MotoFavorite,MotoReservation



class MotoSerializers(serializers.ModelSerializer):
    class Meta:
        model  =Moto
        fields    ='__all__'



class MotoReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model    =MotoReservation
        fields      = '__all__'



class MotoPastReservationSerializer(serializers.ModelSerializer):
    moto_model                = serializers.CharField(source='moto.model')
    moto_rent_per_day      =serializers.IntegerField(source='moto.rent_per_day')
    moto_moto_foto_1        = serializers.ImageField(source='moto.moto_foto_1')


    class Meta:
        model   = MotoReservation
        fields     = ('id','moto_model','moto_rent_per_day','moto_moto_foto_1','total_price','rez_date')

class MotoFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model   = MotoFavorite
        fields     =  '__all__'




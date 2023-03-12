from api.models import ( Vehicle,   Reservation,VEHICLE_SELECTION, Favorite
)
from rest_framework import serializers
from PIL import Image

class VehicleSerializers(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=VEHICLE_SELECTION)


    class Meta:
        model  =Vehicle
        fields    =('id','vehicle_owner','model','vehicle_location','category','seating_capacity','rent_per_day','availability','about','arac_foto_1','arac_foto_2','arac_foto_3')

class VehicleReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model    =Reservation
        fields      = '__all__'


class  VehiclePastReservationSerializer(serializers.ModelSerializer):
    vehicle_model = serializers.CharField(source='vehicle.model')
    vehicle_rent_per_day = serializers.IntegerField(source='vehicle.rent_per_day')
    vehicle_arac_foto_1 = serializers.ImageField(source='vehicle.arac_foto_1')

    class Meta:
        model = Reservation
        fields = ('id', 'vehicle_model', 'vehicle_rent_per_day', 'vehicle_arac_foto_1', 'total_price', 'rez_date')


class FavoriteSerializer(serializers.ModelSerializer):
    favorite_arac_foto_1 = serializers.ImageField(read_only=True,source='favorite_vehicle.arac_foto_1')
    
    class Meta:
        model = Favorite
        fields  = '__all__'
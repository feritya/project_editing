from django.shortcuts import get_object_or_404
from django.shortcuts import render

from rest_framework import permissions
import json
from datetime import date
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets
from rest_framework.response import Response

from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend,OrderingFilter

from api.models import (
Vehicle,
Reservation,
Favorite
)
from api.car.serializers import (
VehicleReservationSerializer,
VehicleSerializers,
VehiclePastReservationSerializer,
FavoriteSerializer,
)
from rest_framework import filters
from django_filters import rest_framework as django_filters

class VehicleFilter(django_filters.FilterSet):
    min_rent_per_day = django_filters.NumberFilter(field_name='rent_per_day', lookup_expr='gte')
    max_rent_per_day = django_filters.NumberFilter(field_name='rent_per_day', lookup_expr='lte')
    min_seating_capacity = django_filters.NumberFilter(field_name='seating_capacity', lookup_expr='gte')
    max_seating_capacity = django_filters.NumberFilter(field_name='seating_capacity', lookup_expr='lte')

class VehicleSearchAPIView(viewsets.ModelViewSet) :
    serializer_class  =VehicleSerializers
    queryset =Vehicle.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['availability', 'rent_per_day','seating_capacity','vehicle_location','model','category']
    




class VehicleAPIView(viewsets.ModelViewSet) :
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class  =VehicleSerializers
    queryset =Vehicle.objects.all()
    filterset_class = VehicleFilter
    filter_backends = [django_filters.DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['rent_per_day', 'seating_capacity']
    
    def get_queryset(self):
        queryset =Vehicle.objects.all()
        model     = self.request.query_params.get('model',None)
        category = self.request.query_params.get('category',None)
        vehicle_location  = self.request.query_params.get('vehicle_location',None)
        
  

        if vehicle_location is not None:
            queryset=queryset.filter(vehicle_location=vehicle_location)

        if category is not None:
            queryset=queryset.filter(category=category)

        if model is not None:
            queryset=queryset.filter(model=model)

        return queryset


class VehicleReservationsAPIView(viewsets.ModelViewSet):
     queryset           = Reservation.objects.all()
     serializer_class  = VehicleReservationSerializer

     permission_classes = [permissions.IsAuthenticated]
    
     def create(self, request):
         serializer = self.get_serializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         reservations = Reservation.objects.filter(vehicle=serializer.data['vehicle'])
         issue_date = serializer.data['issue_date']
         return_date = serializer.data['return_date']
         current_date = date.today()
      
         for r in reservations:
             if str(r.issue_date) <= str(issue_date) <= str(r.return_date):
                 content = {"message":"The selected car is not available on this date"}
                 return Response(content,status=status.HTTP_400_BAD_REQUEST)

         # Check whether issue_date is not older than today's date, and is less equal to return_date
         if str(current_date) <= str(issue_date) and str(issue_date) <= str(return_date):

             self.perform_create(serializer)
             headers = self.get_success_headers(serializer.data)
             return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
         else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VehiclePastRezervationsAPIView(viewsets.ModelViewSet) :
    permission_classes = [permissions.IsAuthenticated]
    serializer_class  =VehiclePastReservationSerializer
    queryset           =Reservation.objects.all()
    filter_backends = [DjangoFilterBackend]

#araba modeline göre rezervasyonları getirir
    def get_queryset(self):
        queryset =Reservation.objects.all()
        vehicle     = self.request.query_params.get('vehicle',None)
        if vehicle is not None:
            queryset=queryset.filter(vehicle__model=vehicle)
        return queryset


#favoriler clasını oluşturuyorum 
class FavoriteAPIView(viewsets.ModelViewSet) :

     queryset           = Favorite.objects.all()
     serializer_class  = FavoriteSerializer








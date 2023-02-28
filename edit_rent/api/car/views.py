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

from api.models import (Car,
CarReservation,
Favorite
)
from api.car.serializers import (CarSerializers,
CarReservationSerializer,
CarPastReservationSerializer,
FavoriteSerializer
)




class CarAPIView(viewsets.ModelViewSet) :
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class=         CarSerializers
    queryset =                  Car.objects.all()
class CarReservationsAPIView(viewsets.ModelViewSet):
     queryset = CarReservation.objects.all()
     serializer_class = CarReservationSerializer
     # permission_classes = [IsAccountAdminOrReadOnly]
    
     def create(self, request):
         serializer = self.get_serializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         reservations = CarReservation.objects.filter(car=serializer.data['car'])
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


class CarPastRezervationsAPIView(viewsets.ModelViewSet) :
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class=         CarPastReservationSerializer
    queryset =                  CarReservation.objects.all()

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer








    """
    queryset = Car.objects.all()
    serializer_class = CarSerializers

    @action(detail=True, methods=['POST'])
    def add_to_favorites(self, request, pk=None):
        car = self.get_object()
        user = request.user
        user.favorite_vehicles.add(car)
        return Response({'message': 'Vehicle added to favorites!'})

    @action(detail=True, methods=['POST'])
    def remove_from_favorites(self, request, pk=None):
        car = self.get_object()
        user = request.user
        user.favorite_vehicles.remove(car)
        return Response({'message': 'Vehicle removed from favorites!'})

"""




"""
class FavoriteViewSet(viewsets.ModelViewSet):
    queryset                    = Favorite.objects.all()
    serializer_class           = FavoriteSerializer
    def perform_create(self, serializer):


        content_type = get_object_or_404(ContentType, model=self.request.data.get('content_type'))
        object_id = int(self.request.data.get('object_id'))
        serializer.save(user=self.request.user, content_type=content_type, object_id=object_id)
        
"""

























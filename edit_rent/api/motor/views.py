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

from api.models import Moto,MotoFavorite,MotoReservation
from  api.motor.serializers import MotoSerializers,MotoFavoriteSerializer,MotoPastReservationSerializer,MotoReservationSerializer

class MotoAPIView(viewsets.ModelViewSet) :
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class=         MotoSerializers
    queryset =                  Moto.objects.all()



class MotoReservationsAPIView(viewsets.ModelViewSet):
     queryset = MotoReservation.objects.all()
     serializer_class = MotoReservationSerializer
     # permission_classes = [IsAccountAdminOrReadOnly]
    
     def create(self, request):
         serializer = self.get_serializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         reservations = MotoReservation.objects.filter(moto=serializer.data['moto'])
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

class MotoPastRezervationsAPIView(viewsets.ModelViewSet) :
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]-
    queryset =                  MotoReservation.objects.all()
    serializer_class=         MotoPastReservationSerializer


class MotoFavoriteViewSet(viewsets.ModelViewSet):
    queryset = MotoFavorite.objects.all()
    serializer_class = MotoFavoriteSerializer

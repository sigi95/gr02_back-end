from django.db.models import query
from django.http.response import JsonResponse
from rest_framework import generics, viewsets, views, status, filters
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from TourApp.serializers.ciudadSerializer import CiudadSerializer
from django_filters.rest_framework import DjangoFilterBackend

from TourApp.models.tour import Tour
from TourApp.models.ciudad import Ciudad
from TourApp.serializers.tourSerializer import TourSerializer
import json

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    #metodo para guardar
    def post(self, request, *args, **kwargs):
        serializer = TourSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

#este es para obtener los tours deacuerdo a una ciudad
class TourCiudadGetView(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ciu_nombre']

#para obtener por id del tour
class TourIdGetView(views.APIView):
    def get(self, request, pk):
        tour_id = list(Tour.objects.filter(id=pk).values()) #verifico si existen usuarios
        if len(tour_id) > 0:
            tour_id = Tour.objects.get(id=pk) #obtengo los datos del usuario mediante su id
            datos = {'message':'Success'}
            return Response(datos, status=status.HTTP_200_OK)
    

    """def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(tour__ciudad="Bogota")"""
    
    """queryset = Tour.objects.all()
    serializer_class = TourSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('ciu_nombre')"""



    """def get(self, request, ciudad):
        #tours = list(Tour.objects.filter(tour_nombre=ciudad).values()) #verifico si existen usuarios
        #if len(tours) > 0:
        tour = Tour.objects.filter(tour_transporte="BUS") #obtengo los datos del usuario mediante su id
        datos = {'message':'Success', 'tours transporte':tour}
        return JsonResponse(datos)"""


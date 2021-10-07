from rest_framework import viewsets

from TourApp.models.ciudad import Ciudad
from TourApp.serializers.ciudadSerializer import CiudadSerializer

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
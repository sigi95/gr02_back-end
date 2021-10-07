from rest_framework import viewsets

from TourApp.models.carrito import Carrito
from TourApp.serializers.carritoSerializer import CarritoSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
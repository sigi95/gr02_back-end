from rest_framework import viewsets

from TourApp.models.tour import Tour
from TourApp.serializers.tourSerializer import TourSerializer

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
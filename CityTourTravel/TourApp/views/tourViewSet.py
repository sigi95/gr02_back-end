from django.conf import settings
from django.http.response import JsonResponse
from rest_framework import generics,views, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from TourApp.models.tour import Tour
from TourApp.serializers.tourSerializer import TourSerializer

class TourViewSet(views.APIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    #metodo para guardar
    def post(self, request, *args, **kwargs):
        serializer = TourSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message':'Success', 'datos':request.data}
        return Response(data, status=status.HTTP_201_CREATED)

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
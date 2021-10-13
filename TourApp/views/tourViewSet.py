import json
from django.conf import settings
from django.http.response import JsonResponse
from rest_framework import generics,views, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

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
class TourIdGetView(generics.ListAPIView):
    def get(self, request, pk):
        tour_id = list(Tour.objects.filter(tour_id=pk).values()) #verifico si existen usuarios
        if len(tour_id) > 0:
            tour = tour_id[0]
            datos = {'message':'Success', 'data tour': tour_id[0]}
            #return Response(status=status.HTTP_200_OK)
            return JsonResponse(datos)

#metodo para editar el carrito de compras
class TourEditarView(views.APIView):
    permission_classes = (IsAuthenticated, )

    def put(self, request, pk):
        jd = json.loads(request.body) #cargamos los datos del usuario por medio de un json
        print(jd) #muestro tal informacion
        data_tour = list(Tour.objects.filter(tour_id=pk).values()) #verifico si existen tours
        if len(data_tour) > 0:
            data_tour = Tour.objects.get(tour_id=pk)

            #cargo los campos los cuales se van a modificar
            data_tour.tour_nombre = jd['tour_nombre']
            data_tour.ciu_nombre = jd['ciu_nombre']
            data_tour.tour_precio = jd['tour_precio']
            data_tour.tour_duracionHoras = jd['tour_duracionHoras']
            data_tour.save() #por ultimo los guarda y muestra un success
            datos = {'message':'Success'}
            return Response(datos, status=status.HTTP_200_OK)
        else:
            datos = {'message':'Error'}
            return Response(datos, status=status.HTTP_500_INTERNAL_SERVER_ERROR) #en caso de que el metodo no funcione
        return JsonResponse(datos)
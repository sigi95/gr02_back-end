from django.http.response import JsonResponse
from rest_framework import viewsets, views, status
from rest_framework.response import Response

from TourApp.models.ciudad import Ciudad
from TourApp.serializers.ciudadSerializer import CiudadSerializer

class CiudadView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = CiudadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def get(self, request):
        ciudades = list(Ciudad.objects.values())
        if len(ciudades) > 0:
            datos = {'message':'Success', 'Ciudades': ciudades}
            return Response(datos, status=status.HTTP_200_OK)
        else:
            datos = {'message':'No hay datos registrados'}
            return Response(datos, status=status.HTTP_404_NOT_FOUND)

class CiudadGetView(views.APIView):
    def get(self, reques, id):
        if id>0:
            ciudades_ = Ciudad.objects.values()
            tour = Ciudad.objects.get(ciudades_.ciu_id)
            datos = tour[0]
        return JsonResponse(datos)
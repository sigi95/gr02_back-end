import json
from django.conf import settings
from django.http.response import JsonResponse
from rest_framework import viewsets, views, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from TourApp.models.carrito import Carrito
from TourApp.serializers.carritoSerializer import CarritoSerializer

class CarritoView(views.APIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    permission_classes = (IsAuthenticated,)#funciona
    
    def post(self, request, *args, **kwargs):
        serializer = CarritoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class CarritoGetView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk):
        tour_id = list(Carrito.objects.filter(cc_usu_id=pk).values()) #verifico si existen usuarios
        if len(tour_id) > 0:
            tour = tour_id[0]
            datos = {'message':'Success', 'data tour': tour_id[0]}
            return JsonResponse(datos)
        

class EditarCarritoView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        jd = json.loads(request.body) #cargo los datos del carrito
        print(jd)
        carritos = list(Carrito.objects.filter(cc_id=pk).values()) #enumero la informacion de la tabla
        if len(carritos) > 0:
            carrito = Carrito.objects.get(cc_id=pk)
            carrito.cc_numeroPersonas = jd["cc_numeroPersonas"]
            carrito.save()
            datos = {'message':'Success'}
            return Response(datos, status=status.HTTP_200_OK)
        else:
            datos = {'message':'Informacion del carrito no se encuentra...'}


class EliminarCarritoView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self ,request, pk):
        data_carrito = list(Carrito.objects.filter(cc_id=pk).values()) #verifico que si existen usuarios en la tabla
        if len(data_carrito) > 0: #si la cantidad es mayor a cero
            Carrito.objects.filter(cc_id=pk).delete() #busca el usuario deacuerdo a su id
            datos = {'message':'Compra eliminada'} #en caso de que exista lo elimina
            return Response(datos, status=status.HTTP_200_OK)# y devuelve un estado de que a funcionado el metodo
        else:
            datos = {'message':'Compras no encontradas'} #de lo contrario muestra este mensaje
            return Response(datos, status=status.HTTP_404_NOT_FOUND) # seguido de enviar un not found
from rest_framework import viewsets, views, status
from rest_framework.response import Response

from TourApp.models.carrito import Carrito
from TourApp.serializers.carritoSerializer import CarritoSerializer
import json

class CarritoView(views.APIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = CarritoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

    def get(self, request, pk):
        carrito_id = list(Carrito.objects.filter(id=pk).values()) #verifico si existen usuarios
        if len(carrito_id) > 0:
            carrito_id = Carrito.objects.get(id=pk) #obtengo los datos del usuario mediante su id
            datos = {'message':'Success'}
            return Response(datos, status=status.HTTP_200_OK)

    def put(self, request, pk):
        jd = json.loads(request.body) #cargamos los datos del usuario por medio de un json
        print(jd) #muestro tal informacion
        data_carrito = list(Carrito.objects.filter(id=pk).values()) #verifico si existen usuarios
        if len(data_carrito) > 0:
            data_carrito = Carrito.objects.get(id=pk) #obtengo los datos del usuario mediante su id
            #cargo los campos los cuales se van a modificar
            data_carrito.cc_numeroPersonas = jd['cc_numeroPersonas']
            data_carrito.save() #por ultimo los guarda y muestra un success
            datos = {'message':'Success'}
            return Response(datos, status=status.HTTP_200_OK)
        else:
            datos = {'message':'Error'}
            return Response(datos, status=status.HTTP_500_INTERNAL_SERVER_ERROR) #en caso de que el metodo no funcione
        return JsonResponse(datos)

    def delete(self ,request, pk):
        data_carrito = list(Carrito.objects.filter(id=pk).values()) #verifico que si existen usuarios en la tabla
        if len(data_carrito) > 0: #si la cantidad es mayor a cero
            Carrito.objects.filter(id=pk).delete() #busca el usuario deacuerdo a su id
            datos = {'message':'Compra eliminada'} #en caso de que exista lo elimina
            return Response(datos, status=status.HTTP_200_OK)# y devuelve un estado de que a funcionado el metodo
        else:
            datos = {'message':'Compras no encontradas'} #de lo contrario muestra este mensaje
            return Response(datos, status=status.HTTP_404_NOT_FOUND) # seguido de enviar un not found
        return JsonResponse(datos)
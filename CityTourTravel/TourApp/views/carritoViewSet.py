import json
from django.conf import settings
from rest_framework import viewsets, views, status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend

from TourApp.models.carrito import Carrito
from TourApp.serializers.carritoSerializer import CarritoSerializer

class CarritoView(views.APIView):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != request.data['cc_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        serializer = CarritoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

class CarritoGetView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != request.data['cc_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        carrito_id = list(Carrito.objects.filter(id=pk).values()) #verifico si existen usuarios
        if len(carrito_id) > 0:
            carrito_id = Carrito.objects.get(id=pk) #obtengo los datos del usuario mediante su id
            datos = {'message':'Success'}
            return Response(datos, status=status.HTTP_200_OK)

class EditarCarritoView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, pk):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        jd = json.loads(request.body) #cargamos los datos del usuario por medio de un json
        print(jd) #muestro tal informacion
        data_carrito = list(Carrito.objects.filter(id=pk).values()) #verifico si existen usuarios
        if len(data_carrito) > 0:
            data_carrito = Carrito.objects.get(id=pk) #obtengo los datos del usuario mediante su id

            #Se verifica que el carrito si corresponda al usuario que hace la solicitud.
            if data_carrito.cc_usu_id !=  valid_data['user_id']:
                stringResponse = {'detail':'Unauthorized Request'}
                return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

            #cargo los campos los cuales se van a modificar
            data_carrito.cc_numeroPersonas = jd['cc_numeroPersonas']
            data_carrito.save() #por ultimo los guarda y muestra un success
            datos = {'message':'Success'}
            return Response(datos, status=status.HTTP_200_OK)
        else:
            datos = {'message':'Error'}
            return Response(datos, status=status.HTTP_500_INTERNAL_SERVER_ERROR) #en caso de que el metodo no funcione
        return JsonResponse(datos)

class EliminarCarritoView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self ,request, pk):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        data_carrito = list(Carrito.objects.filter(id=pk).values()) #verifico que si existen usuarios en la tabla
        if len(data_carrito) > 0: #si la cantidad es mayor a cero
            #Se verifica que el carrito si corresponda al usuario que hace la solicitud.
            if data_carrito.cc_usu_id !=  valid_data['user_id']:
                stringResponse = {'detail':'Unauthorized Request'}
                return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

            Carrito.objects.filter(id=pk).delete() #busca el usuario deacuerdo a su id
            datos = {'message':'Compra eliminada'} #en caso de que exista lo elimina
            return Response(datos, status=status.HTTP_200_OK)# y devuelve un estado de que a funcionado el metodo
        else:
            datos = {'message':'Compras no encontradas'} #de lo contrario muestra este mensaje
            return Response(datos, status=status.HTTP_404_NOT_FOUND) # seguido de enviar un not found
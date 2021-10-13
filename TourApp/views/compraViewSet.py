import json
from django.conf import settings
from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend


from TourApp.models.compra import Compras
from TourApp.serializers.compraSerializer import CompraSerializer

class CompraView(views.APIView):
    queryset = Compras.objects.all()
    serializer_class = CompraSerializer
    #permission_classes = (IsAuthenticated,)

    #metodo para guardar
    def post(self, request, *args, **kwargs):
        serializer = CompraSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message':'Success', 'datos compra':request.data}
        return Response(data, status=status.HTTP_201_CREATED)

#para obtener por id del tour
class CompraIdGetView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        tour_id = list(Compras.objects.filter(com_id=pk).values()) #verifico si existen compras
        if len(tour_id) > 0:
            tour_id = Compras.objects.get(com_id=pk) #obtengo los datos de la compra mediante su id
            datos = {'message':'Success', 'data compra': tour_id}
            return Response(datos, status=status.HTTP_200_OK)
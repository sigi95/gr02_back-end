from django.db.models import fields
from rest_framework import serializers
from TourApp.models.compra import Compras

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compras
        fields = ['com_id','usu_id','com_metodoPago','com_numeroCuenta','com_confirmarPago','com_fechaPago']
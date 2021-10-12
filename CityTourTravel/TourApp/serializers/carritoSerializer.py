from django.db.models import fields
from rest_framework import serializers
from TourApp.models.carrito import Carrito

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = ['cc_id', 'cc_usu_nombreUsuario','cc_tour_nombre','cc_numeroPersonas','cc_precioTotal']
from django.db.models import fields
from rest_framework import serializers
from TourApp.models.ciudad import Ciudad

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ['ciu_nombre', 'ciu_pais']
    
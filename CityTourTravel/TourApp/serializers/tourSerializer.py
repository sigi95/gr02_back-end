from django.db.models import fields
from rest_framework import serializers
from TourApp.models.ciudad import Ciudad
from TourApp.models.tour import Tour
from TourApp.serializers.ciudadSerializer import CiudadSerializer

class TourSerializer(serializers.ModelSerializer):
    #ciudad = CiudadSerializer()
    class Meta:
        model = Tour
        fields = ['tour_nombre', 'tour_descripcion','tour_precio','tour_fechaHoraInicio','tour_fechaHoraFin','tour_duracionHoras',
        'tour_transporte','tour_alimentacion','tour_hospedaje','tour_kilometros','tour_inicio','tour_fin', 'ciu_nombre']
    """
    def create(self, validated_data):
        ciudadData = validated_data.pop('ciudad')
        tourInstance = Tour.objects.create(**validated_data)
        Ciudad.objects.create(tour=tourInstance, **ciudadData)
        return tourInstance
    
    def to_representation(self, obj):
        tour = Tour.objects.get(id=obj.id)
        ciudad = Ciudad.objects.get(tour=obj.id)
        return {
            'tour_id': tour.id,
            'tour_nombre': tour.tour_nombre,
            'tour_descripcion': tour.tour_descripcion,
            'tour_precio': tour.tour_precio,
            'tour_fechaHoraInicio': tour.tour_fechaHoraInicio,
            'tour_fechaHoraFin': tour.tour_fechaHoraFin,
            'tour_duracionHoras': tour.tour_duracionHoras,
            'tour_transporte': tour.tour_transporte,
            'tour_alimentacion': tour.tour_alimentacion,
            'tour_hospedaje': tour.tour_hospedaje,
            'tour_kilometros': tour.tour_kilometros,
            'tour_inicio': tour.tour_inicio,
            'tour_fin': tour.tour_fin,
            'ciu_nombre_id': tour.ciu_nombre_id,
            'ciudad': {
                'ciu_id': ciudad.id,
                'ciu_nombre': ciudad.ciu_nombre,
                'ciu_pais': ciudad.ciu_pais
            }
        }"""
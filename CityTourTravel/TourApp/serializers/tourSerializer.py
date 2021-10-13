from django.db.models import fields
from rest_framework import serializers
from TourApp.models.tour import Tour

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ['tour_id','tour_nombre', 'tour_descripcion','tour_precio','tour_fechaHoraInicio','tour_fechaHoraFin','tour_duracionHoras',
        'tour_transporte','tour_alimentacion','tour_hospedaje','tour_kilometros','tour_inicio','tour_fin', 'ciu_nombre']
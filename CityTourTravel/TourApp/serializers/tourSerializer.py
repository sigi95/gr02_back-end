from django.db.models import fields
from rest_framework import serializers
from TourApp.models.tour import Tour

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'
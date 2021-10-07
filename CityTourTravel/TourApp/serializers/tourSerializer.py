from django.db.models import fields
from rest_framework import serializers
from TourApp.models.tour import Tour

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'

    def create(self, validated_data):
        tourInstance = Tour.objects.create(**validated_data)
        print("id: ",id)
        return tourInstance
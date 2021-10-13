from django.db.models import fields
from rest_framework import serializers
from TourApp.models.usuario import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'usu_tipoId', 'usu_nombreUsuario', 'password', 'usu_nombre', 'usu_apellido1', 'usu_apellido2', 'usu_email', 'usu_telefonoCelular', 'usu_pais', 'usu_ciudad']
    
    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance
from django.db.models import fields
from rest_framework import serializers
from models.usuario import Usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['usu_nombreUsuario', 'usu_nombre', 'usu_apellido1', 'usu_apellido2', 'usu_email', 'usu_telefonoCelular', 'usu_pais', 'usu_ciudad']
    
    def create(self, validated_data):
        userInstance = Usuario.objects.create(**validated_data)
        return userInstance
    
    def to_representation(self, obj):
        usuario = Usuario.objects.get(id=obj.id)
        return {
            'usu_nombreUsuario': usuario.usu_nombreUsuario,
            'usu_nombre': usuario.usu_nombre,
            'usu_apellido1': usuario.usu_apellido1,
            'usu_apellido2':usuario.usu_apellido2,
            'usu_email': usuario.usu_email,
            'usu_telefonoCelular': usuario.usu_telefonoCelular,
            'usu_pais': usuario.usu_pais,
            'usu_ciudad': usuario.usu_ciudad
        }
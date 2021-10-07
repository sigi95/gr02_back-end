from django.db.models import fields
from rest_framework import serializers
from TourApp.models.usuario import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['usu_nombreUsuario', 'usu_contrasena','usu_nombre', 'usu_apellido1', 'usu_apellido2', 'usu_email', 'usu_telefonoCelular', 'usu_pais', 'usu_ciudad']
    
    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance
    
    def to_representation(self, obj):
        usuario = User.objects.get(usu_nombreUsuario=obj.usu_nombreUsuario)
        return {
            'usu_nombreUsuario': usuario.usu_nombreUsuario,
            'usu_contrasena': usuario.usu_contrasena,
            'usu_nombre': usuario.usu_nombre,
            'usu_apellido1': usuario.usu_apellido1,
            'usu_apellido2':usuario.usu_apellido2,
            'usu_email': usuario.usu_email,
            'usu_telefonoCelular': usuario.usu_telefonoCelular,
            'usu_pais': usuario.usu_pais,
            'usu_ciudad': usuario.usu_ciudad
        }
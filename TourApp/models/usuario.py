from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, usu_nombreUsuario, password=None):
        if not usu_nombreUsuario:
            raise ValueError('User must have an username')
        usuario = self.model(usu_nombreUsuario=usu_nombreUsuario)
        usuario.set_password(password)
        usuario.save(usign=self._db)
        return usuario
    
    def create_superuser(self, usu_nombreUsuario, password):
        usuario = self.create_user(
            usu_nombreUsuario=usu_nombreUsuario,
            password=password,
        )
        usuario.is_admin = True
        usuario.save(usign=self.db)
        return usuario

class User(AbstractBaseUser, PermissionsMixin):
    #las opciones para el campo tipoId
    Tipo_identificacion = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjeria'),
        ('NIT', 'NIT')
    ]

    id = models.BigIntegerField('Identificacion',primary_key=True, null=False)
    usu_tipoId = models.CharField('Tipo identificacion', max_length=50, null=False, choices=Tipo_identificacion)
    usu_nombreUsuario = models.CharField('Nombre usuario', max_length=60, null=False, blank=False, unique=True)
    password = models.CharField('Contraseña', max_length=256, null=False)
    usu_nombre = models.CharField('Nombres', max_length=20, null=False)
    usu_apellido1 = models.CharField('Primer Apellido', max_length=40, null=False)
    usu_apellido2 = models.CharField('Segundo Apellido', max_length=40, null=False)
    usu_email = models.EmailField('Email', max_length=60, null=False)
    usu_telefonoCelular = models.CharField('Telefono Celular', max_length=20, null=False)
    usu_pais = models.CharField('Pais', max_length=20, null=False)
    usu_ciudad = models.CharField('Ciudad', max_length=20, null=False)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'usu_nombreUsuario'
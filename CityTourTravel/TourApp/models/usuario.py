from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, usu_nombreUsuario, usu_contrasena=None):
        if not usu_nombreUsuario:
            raise ValueError('User must have an username')
        usuario = self.model(usu_nombreUsuario=usu_nombreUsuario)
        usuario.set_password(usu_contrasena)
        usuario.save(usign=self._db)
        return usuario
    
    def create_superuser(self, usu_nombreUsuario, usu_contrasena):
        usuario = self.create_user(
            usu_nombreUsuario=usu_nombreUsuario,
            usu_contrasena=usu_contrasena,
        )
        usuario.is_admin = True
        usuario.save(usign=self.db)
        return usuario

class User(AbstractBaseUser, PermissionsMixin):
    usu_nombreUsuario = models.CharField('Nombre usuario', primary_key=True, max_length=60, null=False, blank=False, unique=True)
    usu_contrasena = models.CharField('Contraseña', max_length=256, null=False)
    usu_nombre = models.CharField('Nombre', max_length=20, null=False, blank=False)
    usu_apellido1 = models.CharField('Primer Apellido', max_length=40, null=True, blank=True)
    usu_apellido2 = models.CharField('Segundo Apellido', max_length=40, null=True, blank=True)
    usu_email = models.EmailField('Email', max_length=60, null=True, blank=True)
    usu_telefonoCelular = models.IntegerField('Telefono Celular', null=True, blank=True)
    usu_pais = models.CharField('Pais', max_length=20, null=True, blank=True)
    usu_ciudad = models.CharField('Ciudad', max_length=20, null=True, blank=True)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.usu_contrasena = make_password(self.usu_contrasena, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'usu_nombreUsuario'
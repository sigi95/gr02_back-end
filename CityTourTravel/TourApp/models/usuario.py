from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('User must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(usign=self._db)
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(usign=self.db)
        return user

class Usuario(AbstractBaseUser, PermissionsMixin):
    """id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length=15, unique=True)
    password = models.CharField('Password', max_length=256)
    name = models.CharField('Name', max_length=30)
    email = models.EmailField('Email', max_length=100)"""
    usu_nombreUsuario = models.CharField('Nombre usuario', primary_key=True, max_length=60, null=False, blank=False)
    usu_nombre = models.CharField('Nombre', max_length=20, null=False, blank=False)
    usu_apellido1 = models.CharField('Primer Apellido', max_length=40, null=True, blank=True)
    usu_apellido2 = models.CharField('Segundo Apellido', max_length=40, null=True, blank=True)
    usu_email = models.EmailField('Email', max_length=60, null=True, blank=True)
    usu_telefonoCelular = models.IntegerField('Telefono Celular', null=True, blank=True)
    usu_pais = models.CharField('Pais', max_length=20, null=True, blank=True)
    usu_ciudad = models.CharField('Ciudad', max_length=20, null=True, blank=True)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
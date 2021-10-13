from django.db.models import base
from rest_framework import routers, urlpatterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include

from .views.usuarioViewSet import CrearUsuarioViewSet, DetalleUsuarioView, EditarUsuarioView, EliminarUsuarioView, ListarUsuarioView
from .views.tourViewSet import TourCiudadGetView, TourIdGetView, TourViewSet
from .views.ciudadViewSet import CiudadGetView, CiudadView
from .views.carritoViewSet import CarritoGetView, CarritoView, EditarCarritoView, EliminarCarritoView
from .views.compraViewSet import CompraView, CompraIdGetView

urlpatterns = [
    #url para usuario
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
    path('api/usuario/registro/', CrearUsuarioViewSet.as_view()), #crea el usuario
    path('api/usuario/<int:pk>/', DetalleUsuarioView.as_view()), #ver los datos del usuario de manera individual
    path('api/usuario/editar/<int:pk>/', EditarUsuarioView.as_view()), #edita la informacion de usuario
    path('api/usuario/eliminar/<int:pk>/', EliminarUsuarioView.as_view()), #elimina el usuario
    path('api/usuario/listar/', ListarUsuarioView.as_view()), #trae todos los usuarios registrados
    #url para ciudad
    path('api/ciudad/registro/', CiudadView.as_view()), #crea las ciudades
    #url para tours
    path('api/tour/registro/', TourViewSet.as_view()),#registrar tour
    path('api/tour', TourCiudadGetView.as_view()), #usa el filtro para buscar por ciudad, se le agrega ?ciu_nombre=nombre de la ciudad
    path('api/tour/<int:pk>/', TourIdGetView.as_view()),#buscar tour por id
    #url para carrito
    path('api/carrito/registro/', CarritoView.as_view()), #registrar los tours que se piden
    path('api/carrito/<int:pk>/', CarritoGetView.as_view()), #listar lo que esta en el carrito por id
    path('api/carritoEditar/<int:pk>/', EditarCarritoView.as_view()), #editar la informacion del carrito por id
    path('api/carritoEliminar/<int:pk>/', EliminarCarritoView.as_view()), #para eliminar usando el id del carrito
    #url para compras
    path('api/compras/registro/', CompraView.as_view()), #crear la compra
    path('api/compras/<int:pk>/', CompraIdGetView.as_view()), #obtener la compra por su id
]
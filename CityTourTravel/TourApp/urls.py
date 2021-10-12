from django.db.models import base
from rest_framework import routers, urlpatterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include

from TourApp.serializers.carritoSerializer import CarritoSerializer

from .views.usuarioView import CrearUsuarioViewSet, DetalleUsuarioView, EditarUsuarioView, EliminarUsuarioView, ListarUsuarioView
from .views.tourViewSet import TourCiudadGetView, TourIdGetView, TourViewSet
from .views.ciudadView import CiudadGetView, CiudadView
from .views.carritoViewSet import CarritoGetView, CarritoView

router = routers.DefaultRouter()
router.register('tour', TourViewSet, basename='TourView')
#router.register('carrito', CarritoViewSet, basename='CarritoView')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
    path('api/registro/', CrearUsuarioViewSet.as_view()),
    path('api/usuario/<int:pk>/', DetalleUsuarioView.as_view()),
    path('api/editar/<int:pk>/', EditarUsuarioView.as_view()),
    path('api/eliminar/<int:pk>/', EliminarUsuarioView.as_view()),
    path('api/usuario/listar/', ListarUsuarioView.as_view()),
    path('api/ciudad/', CiudadView.as_view()),
    #path('api/registro_tour/', TourViewSet.as_view()),
    path('api/carrito/', CarritoView.as_view()),
    path('api/carrito/<int:pk>/', CarritoGetView.as_view()),
    path('api/tour', TourCiudadGetView.as_view()),
    path('api/tour_id/<int:pk>', TourIdGetView.as_view()),
    path('api/carritoEditar/<int:pk>/', CarritoView.as_view()),
    path('api/carritoEliminar/<int:pk>/', CarritoView.as_view()),
    #path('api/compras/', CompraView.as_view())
    #path('api/tour/<tour_nombre>/', TourView.as_view())
    #path('api/ciudad/<int:id>/', CiudadGetView.as_view())
]
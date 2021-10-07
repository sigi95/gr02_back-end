from django.db.models import base
from rest_framework import routers, urlpatterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include

from .views.crearusuarioViewSet import CrearUsuarioViewSet
from .views.tourViewSet import TourViewSet
from .views.ciudadViewSet import CiudadViewSet
from .views.carritoViewSet import CarritoViewSet

router = routers.DefaultRouter()
router.register('tour', TourViewSet, basename='TourView'),
router.register('ciudad', CiudadViewSet, basename='Ciudadview'),
router.register('carrito', CarritoViewSet, basename='CarritoView')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
    path('api/registro/', CrearUsuarioViewSet.as_view())
]
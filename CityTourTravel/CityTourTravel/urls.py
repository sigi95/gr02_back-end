from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from TourApp.views.crearusuarioViewSet import CrearUsuarioViewSet

urlpatterns = [
    path('', include('TourApp.urls'))
]

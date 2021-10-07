from rest_framework import routers, urlpatterns
from .views.userCreateViewSet import UserCreateView
from .views.userDetailView import UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include


router = routers.DefaultRouter()
router.register('user', UserCreateView, basename='crearUsuarioView')
#router.register('login', TokenObtainPairView, basename='TokenloginView'),
#router.register('refresh', TokenRefreshView, basename='TokenrecuperarsesionView'),

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view())
]
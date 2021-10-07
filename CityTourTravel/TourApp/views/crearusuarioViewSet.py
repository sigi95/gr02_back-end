from rest_framework import status, viewsets, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#models
from TourApp.models.usuario import User
from TourApp.serializers.usuarioSerializer import UsuarioSerializer

class CrearUsuarioViewSet(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"usu_nombreUsuario":request.data["usu_nombreUsuario"],
                    "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
    
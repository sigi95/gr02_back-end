from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#models
from TourApp.models.usuario.user import User
from TourApp.serializers.usuario.userSerializer import UserSerializer

class UserCreateView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"username":request.data["username"],
                    "password":request.data["password"]}
        
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)
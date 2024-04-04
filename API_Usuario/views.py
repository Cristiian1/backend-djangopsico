from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework import status
from django.http import Http404 
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class UsuarioView(APIView):
    def post(self, request, *args, **kwargs):
        # Obtener el nombre de usuario y la contraseña del cuerpo de la solicitud
        username = request.data.get('username')
        password = request.data.get('password')

        # Verificar si el usuario existe en la base de datos
        user = authenticate(request=request, username=username, password=password)
        
        if user:
            # Usuario autenticado correctamente
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # Credenciales incorrectas
            return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        


        # registro
        from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class RegistroUsuario(APIView):
    def post(self, request):
        # Obtener los datos del cuerpo de la solicitud
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            return Response({'error': 'El nombre de usuario ya está en uso'}, status=status.HTTP_400_BAD_REQUEST)

        # Crear un nuevo usuario
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        # Autenticar al usuario recién registrado
        user = authenticate(request=request, username=username, password=password)

        # Generar un token de autenticación
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Error al autenticar al usuario'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CiudadViewSet(viewsets.ModelViewSet):
    serializer_class = CiudadSerializers
    queryset = Ciudad.objects.all()

class DepartamentoViewSet(viewsets.ModelViewSet):
    serializer_class = DepartamentoSerializers
    queryset = Departamento.objects.all()

class TipoPersonaViewSet(viewsets.ModelViewSet):
    serializer_class = TipoPersonaSerializers
    queryset = TipoPersona.objects.all()

class EspecialidadesViewSet(viewsets.ModelViewSet):
    serializer_class = EspecialidadesSerializers
    queryset = Especialidades.objects.all()

class ProfesionViewSet(viewsets.ModelViewSet):
    serializer_class = ProfesionSerializers
    queryset = Profesion.objects.all()

class ProfesionPersonaViewSet(viewsets.ModelViewSet):
    serializer_class = ProfesionPersonaSerializers
    queryset = ProfesionPersona.objects.all()

class PersonaViewSet(viewsets.ModelViewSet):
    serializer_class = PersonaSerializers
    queryset = Persona.objects.all()

class PaisViewSet(viewsets.ModelViewSet):
    serializer_class = PaisSerializers
    queryset = Pais.objects.all()

class UsuarioView(viewsets.ModelViewSet):
    serializer_class = CustomTokenResponseSerializer
    queryset = User.objects.all()
    
    
    # este es para registar usuarios 
class UsuariosViewSet(viewsets.ModelViewSet):
    serializer_class = UsuariosSerializers
    queryset = Usuarios.objects.all()



class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        response_data = {
            'token': token.key,
            'user': user.username  # Cambiado para evitar usar otra serializadora
        }
        return Response(response_data)
    


    
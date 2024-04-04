from rest_framework import serializers
from API_Usuario.models import *
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import User

class CiudadSerializers (serializers.ModelSerializer):
    class Meta:
        model= Ciudad
        fields= '__all__'

class DepartamentoSerializers (serializers.ModelSerializer):
    class Meta:
        model= Departamento
        fields= '__all__'

class TipoPersonaSerializers (serializers.ModelSerializer):
    class Meta:
        model= TipoPersona
        fields= '__all__'
        
class EspecialidadesSerializers (serializers.ModelSerializer):
    class Meta:
        model= Especialidades
        fields= '__all__'

        
class PersonaSerializers (serializers.ModelSerializer):
    class Meta:
        model= Persona
        fields= '__all__'

class PaisSerializers (serializers.ModelSerializer):
    class Meta:
        model= Pais
        fields= '__all__'


        
class ProfesionSerializers (serializers.ModelSerializer):
    class Meta:
        model= Profesion
        fields= '__all__'
        
class ProfesionPersonaSerializers (serializers.ModelSerializer):
    class Meta:
        model= ProfesionPersona
        fields= '__all__'
        
class UsuariosSerializers (serializers.ModelSerializer):
    class Meta:
        model= Usuarios
        fields= '__all__'

class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(
                request=self.context.get('request'),
                username=username,
                password=password
            )

            if not user:
                raise serializers.ValidationError('Credenciales incorrectas')

            data['user'] = user
        else:
            raise serializers.ValidationError('Complete los campos')
        return data


    
    
    
class CustomTokenResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'




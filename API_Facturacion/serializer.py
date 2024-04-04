from rest_framework import serializers
from .models import *
from API_Facturacion import *


class CuerpoSerializers (serializers.ModelSerializer):
    class Meta:
        model= Cuerpo
        fields= '__all__'

        
class CabezaSerializers (serializers.ModelSerializer):
    class Meta:
        model= Cabeza
        fields= '__all__'

class PaquetesSerializers (serializers.ModelSerializer):
    class Meta:
        model= Paquetes
        fields= '__all__'


class TarifaSerializers (serializers.ModelSerializer):
    class Meta:
        model= Tarifa
        fields= '__all__'

  
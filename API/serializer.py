from rest_framework import serializers 
from API.models import *


   
   
    
class CategoriaSerializers (serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields= '__all__'
 
class ExperienciaPsicoSerializers (serializers.ModelSerializer):
    class Meta:
        model= ExperienciaPsico
        fields= '__all__'
    

    
class RecursosEducativosSerializers (serializers.ModelSerializer):
    class Meta:
        model= RecursosEducativos
        fields= '__all__'
    

    
class TareasSerializers (serializers.ModelSerializer):
    class Meta:
        model= Tareas
        fields= '__all__'
    

    



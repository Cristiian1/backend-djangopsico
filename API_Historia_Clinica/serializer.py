from rest_framework import serializers
from .models import *
from API_Historia_Clinica import*




class AntecedentesSerializers (serializers.ModelSerializer):
    class Meta:
        model= Antecedentes
        fields='__all__'

class DesarrolloSesionSerializers (serializers.ModelSerializer):
    class Meta:
        model= DesarrolloSesion
        fields='__all__'


class EvolucionSerializers (serializers.ModelSerializer):
    class Meta:
        model= Evolucion
        fields='__all__'

class ExamenMentalSerializers (serializers.ModelSerializer):
    class Meta:
        model= ExamenMental
        fields='__all__'
        
class DiagnosticoSerializers (serializers.ModelSerializer):
    class Meta:
        model= Diagnostico
        fields='__all__'




class FactoresProtectoresSerializers (serializers.ModelSerializer):
    class Meta:
        model= FactoresProtectores
        fields='__all__'

class FactoresRiesgoSerializers (serializers.ModelSerializer):
    class Meta:
        model= FactoresRiesgo
        fields='__all__'

class HistoriaClinicaSerializers (serializers.ModelSerializer):
    class Meta:
        model= HistoriaClinica
        fields='__all__'

class HistoriaVidaSerializers (serializers.ModelSerializer):
    class Meta:
        model= HistoriaVida
        fields='__all__'

class MotivoConsultaSerializers (serializers.ModelSerializer):
    class Meta:
        model= MotivoConsulta
        fields='__all__'


class RelacionFamiliarSerializers (serializers.ModelSerializer):
    class Meta:
        model= RelacionFamiliar
        fields='__all__'

class RemisionSerializers (serializers.ModelSerializer):
    class Meta:
        model= Remision
        fields='__all__'



class TratamientoSerializers (serializers.ModelSerializer):
    class Meta:
        model= Tratamiento
        fields='__all__'

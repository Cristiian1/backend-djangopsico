from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView


class AntecedentesHistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = AntecedentesSerializers
    queryset = Antecedentes.objects.all()

class DesarrolloSesionHistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = DesarrolloSesionSerializers
    queryset = DesarrolloSesion.objects.all()

class DiagnosticoHistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = DiagnosticoSerializers
    queryset = Diagnostico.objects.all()

class ExamenMentalHistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = ExamenMentalSerializers
    queryset = ExamenMental.objects.all()

class FactoresProtectoresHistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = FactoresProtectoresSerializers
    queryset = FactoresProtectores.objects.all()

class EvolucionHistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = EvolucionSerializers
    queryset = Evolucion.objects.all()

class FactoresRiesgoHistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = FactoresRiesgoSerializers
    queryset = FactoresRiesgo.objects.all()

class HistoriaClinicaHistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = HistoriaClinicaSerializers
    queryset = HistoriaClinica.objects.all()

class HistoriaVidaHistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = HistoriaVidaSerializers
    queryset = HistoriaVida.objects.all()

class MotivoConsultaHistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = MotivoConsultaSerializers
    queryset = MotivoConsulta.objects.all()

class RelacionFamiliarHistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = RelacionFamiliarSerializers
    queryset = RelacionFamiliar.objects.all()

class RemisionHistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = RemisionSerializers
    queryset = Remision.objects.all()

class TratamientoHistoriaViewSet(viewsets.ModelViewSet):
    serializer_class = TratamientoSerializers
    queryset = Tratamiento.objects.all()




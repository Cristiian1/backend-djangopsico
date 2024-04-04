
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets



class Cuerpo_API_FacturacionViewSet(viewsets.ModelViewSet):
    serializer_class = CuerpoSerializers
    queryset = Cuerpo.objects.all()

class Cabeza_API_FacturacionViewSet(viewsets.ModelViewSet):
    serializer_class = CabezaSerializers
    queryset = Cabeza.objects.all()


class Paquetes_API_FacturacionViewSet(viewsets.ModelViewSet):
    serializer_class = PaquetesSerializers
    queryset = Paquetes.objects.all()


class Tarifa_API_FacturacionViewSet(viewsets.ModelViewSet):
    serializer_class = TarifaSerializers
    queryset = Tarifa.objects.all()


from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from .models import *
from rest_framework import status
from django.http import Http404

# Create your views here.

# Definición de una clase basada en vistas para manejar operaciones CRUD en la entidad Cliente

#--------------vista deCategoria -----------------------
class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializers
    queryset = Categoria.objects.all()


class ExperienciaPsicoViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienciaPsicoSerializers
    queryset = ExperienciaPsico.objects.all()

class TareasViewSet(viewsets.ModelViewSet):
    serializer_class = TareasSerializers
    queryset = Tareas.objects.all()

class RecursosEducativosViewSet(viewsets.ModelViewSet):
    serializer_class = RecursosEducativosSerializers
    queryset = RecursosEducativos.objects.all()


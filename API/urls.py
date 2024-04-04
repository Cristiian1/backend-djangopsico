from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path,include
from rest_framework import routers


from API.views import *

router = routers.DefaultRouter()
router.register(r'Categoria', CategoriaViewSet, basename='Categoria')
router.register(r'ExperienciaPsico', ExperienciaPsicoViewSet, basename='ExperienciaPsico')

router.register(r'Tareas', TareasViewSet, basename='Tareas')
router.register(r'RecursosEducativos', RecursosEducativosViewSet, basename='RecursosEducativos')


# Define las rutas
urlpatterns = [
    path('', include(router.urls)),
  
]



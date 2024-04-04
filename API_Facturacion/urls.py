
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from API_Facturacion.views import *
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'CuerpoFacturacion', Cuerpo_API_FacturacionViewSet, basename='Cuerpo')
router.register(r'CabezaFacturacion', Cabeza_API_FacturacionViewSet, basename='Cabeza')
router.register(r'Paquetes', Paquetes_API_FacturacionViewSet, basename='Paquetes')
router.register(r'Tarifa', Tarifa_API_FacturacionViewSet, basename='Tarifa')



# Define las rutas
urlpatterns = [
    path('', include(router.urls)),
  
]
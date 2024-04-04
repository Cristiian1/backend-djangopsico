
from django.contrib.auth.views import LoginView, LogoutView
from API_Historia_Clinica.views import *
from django.urls import path, include
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Antecedentes', AntecedentesHistoriaViewSet, basename='Antecedentes')
router.register(r'DesarrolloSesion',  DesarrolloSesionHistoriaViewSet, basename='DesarrolloSesion')
router.register(r'Diagnostico', DiagnosticoHistoriaViewSet, basename='Diagnostico')
router.register(r'ExamenMental', ExamenMentalHistoriaViewSet, basename='ExamenMental')
router.register(r'FactoresProtectores', FactoresProtectoresHistoriaViewSet, basename='FactoresProtectores')
router.register(r'Evolucion',  EvolucionHistoriaViewSet, basename='Evolucion')
router.register(r'FactoresRiesgo', FactoresRiesgoHistoriaViewSet, basename='FactoresRiesgo')
router.register(r'HistoriaClinica', HistoriaClinicaHistoriaViewSet, basename='HistoriaClinica')
router.register(r'HistoriaVida', HistoriaVidaHistoriaViewSet, basename='HistoriaVida')
router.register(r'MotivoConsulta',  MotivoConsultaHistoriaViewSet, basename='MotivoConsulta')
router.register(r'RelacionFamiliar', RelacionFamiliarHistoriaViewSet, basename='RelacionFamiliar')
router.register(r'RemisionHistoria', RemisionHistoriaViewSet, basename='RemisionHistoria')
router.register(r'Tratamiento', TratamientoHistoriaViewSet, basename='Tratamiento')


# Define las rutas
urlpatterns = [
    path('', include(router.urls)),
  
]

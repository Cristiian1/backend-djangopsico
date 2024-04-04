from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from API_Usuario.views import *
from rest_framework import routers


from django.contrib.auth.views import LoginView, LogoutView
from API_Historia_Clinica.views import *
from django.urls import path, include
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Ciudad', CiudadViewSet, basename='Ciudad')
router.register(r'Departamento',  DepartamentoViewSet, basename='Departamento')
router.register(r'Especialidades', EspecialidadesViewSet, basename='Especialidades')
router.register(r'Profesion', ProfesionViewSet, basename='Profesion')
router.register(r'ProfesionPersona',  ProfesionPersonaViewSet, basename='ProfesionPersona')
router.register(r'Persona', PersonaViewSet, basename='Persona')
router.register(r'Pais', PaisViewSet, basename='Pais')
router.register(r'TipoPersona', TipoPersonaViewSet, basename='TipoPersona')
router.register(r'usuario', UsuarioView)
router.register(r'Usuarios',UsuariosViewSet, basename='Usuarios')





# Define las rutas
urlpatterns = [
    path('', include(router.urls)),
    path('login', CreateTokenView.as_view()),
  
]

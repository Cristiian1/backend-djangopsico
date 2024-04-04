"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from principal.views import *
from django.contrib.auth.views import LoginView, LogoutView
from principal.views import usuarios, pantallainicio, historiaClinica
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('principal/', include(('principal.urls','principal'))),
    path('API/', include(('API.urls','API'))),
    path('API_Historia_Clinica/', include(('API_Historia_Clinica.urls','Historia_Clinica'))),
     path('API_Usuario/', include(('API_Usuario.urls','API_Usuario'))),
    path('home/', Home, name= 'index'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='login.html'), name="logout"),
    path('catalogo/', Listadocatalogo.as_view(template_name='tienda/index1.html'), name="catalogo"),
    path('catalogo/detalle/<int:pk>/', catalogodetalle.as_view(template_name='tienda/index2.html'), name="detallesre"),

    
    path('usuarios/', usuarios, name="usuarios"),
    path('', pantallainicio, name="pantallainicio"),
    path('registro/', SignUpView.as_view(template_name='register.html'), name="registro"),
    
    path('historiaClinica', historiaClinica, name="historiaClinica"),
    path('evolucion/', evolucion, name='evolucion'),
    path('docs/', include_docs_urls(title='Api Documentation')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

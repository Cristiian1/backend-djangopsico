from rest_framework import generics 
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Categoria


# Create your views here.
from django.shortcuts import render, redirect
from django import forms 
from principal.models import *
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 

from django.forms.models import modelform_factory
from principal.models import Persona
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,get_user_model,authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import CreateView, TemplateView
from .models import Categoria 





from .forms import SignUpForm

class CrearCategoriaView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            nombre = request.data.get('nombre')
            descripcion = request.data.get('descripcion')
            imagen = request.data.get('imagen')  # Cambiado de 'imagen_nombre' a 'imagen'

            # Verifica si los campos obligatorios están presentes
            if not nombre or not descripcion:
                return JsonResponse({'error': 'El nombre y la descripción son campos obligatorios'}, status=400)

            # Crea la nueva categoría
            nueva_categoria = Categoria(nombre=nombre, descripcion=descripcion, imagen=imagen)
            nueva_categoria.save()

            return JsonResponse({'mensaje': 'Categoría creada correctamente'}, status=201)
        except Exception as e:
            # Manejo de errores genérico
            return JsonResponse({'error': str(e)}, status=500)

from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def obtener_categorias(request):
    """
    Esta función devuelve todas las categorías disponibles en formato JSON.
    """
    try:
        categorias = Categoria.objects.all()
        categorias_json = []

        for categoria in categorias:
            categoria_json = {
                'id': categoria.id,
                'nombre': categoria.nombre,
                'descripcion': categoria.descripcion,
                'imagen': request.build_absolute_uri(categoria.imagen.url) if categoria.imagen else None,
            }
            categorias_json.append(categoria_json)

        return JsonResponse({'categorias': categorias_json}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@require_http_methods(["DELETE"])

def eliminar_categoria(request, id):
    

    try:
        categoria = Categoria.objects.get(id=id)
        categoria.delete()
        return JsonResponse({'mensaje': 'Categoría eliminada correctamente'}, status=200)
    except Categoria.DoesNotExist:
        return JsonResponse({'error': 'La categoría no existe'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

class UploadImageView(APIView):
    def post(self, request):
        image_file = request.FILES.get('imagen')

        # Guarda la imagen en el directorio de tu elección
        # Por ejemplo, puedes usar el atributo `name` del archivo para asignar un nombre único
        # y luego guardar el archivo en el directorio de medios de Django
        # Aquí un ejemplo básico:
        with open('media/' + image_file.name, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

        # Retorna la URL de la imagen guardada (si es necesario)
        # Por ejemplo, puedes retornar la URL relativa o absoluta de la imagen
        # dependiendo de cómo estés sirviendo tus archivos estáticos
        image_url = '/media/' + image_file.name
        return Response({'image_url': image_url})
    
@require_http_methods(["PUT", "PATCH"])
def editar_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return JsonResponse({'error': 'La categoría no existe'}, status=404)

    if request.method == "PUT":
        # Lógica para el método PUT
        nombre = request.data.get('nombre')
        descripcion = request.data.get('descripcion')
        imagen = request.data.get('imagen')

        # Verifica si los campos obligatorios están presentes
        if not nombre or not descripcion:
            return JsonResponse({'error': 'El nombre y la descripción son campos obligatorios'}, status=400)

        categoria.nombre = nombre
        categoria.descripcion = descripcion
        categoria.imagen = imagen
        categoria.save()

        return JsonResponse({'mensaje': 'Categoría actualizada correctamente'}, status=200)
        
    elif request.method == "PATCH":
        # Lógica para el método PATCH
        nombre = request.data.get('nombre')
        descripcion = request.data.get('descripcion')
        imagen = request.data.get('imagen')

        if nombre:
            categoria.nombre = nombre
        if descripcion:
            categoria.descripcion = descripcion
        if imagen:
            categoria.imagen = imagen

        categoria.save()

        return JsonResponse({'mensaje': 'Categoría actualizada correctamente'}, status=200)














def Home(request):
    
    return render (request, "index.html")






class SignUpView(CreateView):
    model = User
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('login') 

def Parametros (request):
    return render (request, "crud/index.html")  

def Login(request):
    return render (request, "login.html")

class Listadocatalogo(ListView):
    model =Categoria

class catalogodetalle (DetailView):
    model =Categoria

def usuarios (request):
     
     usuarioFormulario=modelform_factory(Persona,exclude=['pais_idpais','tpersona_id','identificacion', 'genero_idgenero', 'apellido2','telefono','nombre2', 'ciudad', 'tpersona_id1'])
     formulario=usuarioFormulario()
     data={
          'formulario':formulario
     }
     
     return render(request,'usuarios.html', data)

def pantallainicio(request):
    
    return render (request, "pantalladeinicio.html")

def historiaClinica(request):
    
    return render (request, "ModuloHC/historiaClinica.html")

def evolucion(request):
    return render(request, "ModuloHc/evolucion.html")


     

 
 #-----------------------------------RecursosEducativos-----------------------------------------------------#
class ListadoRecursosEducativos(CreateView,ListView,SuccessMessageMixin):

    model = RecursosEducativos
    form = RecursosEducativos
    fields = "__all__"

    success_message ='RecursosEducativos creado correctamente'
    def get_success_url(self):
        return reverse('principal:leerrecurso') # Redireccionamos a la vista principal 'leer'

class RecursosEducativosDetalle (DetailView):
    model = RecursosEducativos

class RecursosEducativosActualizar(SuccessMessageMixin,UpdateView):
    model = RecursosEducativos
    form = RecursosEducativos
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'RecursosEducativos' de nuestra Base de Datos 
    success_message = 'RecursosEducativos Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):
        return reverse('principal:leerrecurso') # Redireccionamos a la vista principal 'leer'

class RecursosEducativosEliminar(SuccessMessageMixin, DeleteView):
    model = RecursosEducativos
    form = RecursosEducativos
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        success_message = 'Actividad Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar una  Actividad
        messages.success (self.request, (success_message))
        return reverse('principal:leerrecurso') # Redireccionamos a la vista principal 'leer'

    #-----------------------------------RecursosEducativos-----------------------------------------------------#
    
    
    #-----------------------------------Categoria-----------------------------------------------------#
class ListadoCategoria(CreateView,ListView,SuccessMessageMixin):

    model = Categoria
    form = Categoria
    fields = "__all__"
    
    success_message ='Categoria creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerCategoria') # Redireccionamos a la vista principal 'leer' 
    
class CategoriaDetalle (DetailView):
    model =Categoria

class CategoriaActualizar(SuccessMessageMixin,UpdateView):
    model =Categoria
    form = Categoria
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Categoria' de nuestra Base de Datos 
    success_message = 'Categoria Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leerCategoria') # Redireccionamos a la vista principal 'leer'
    
class CategoriaEliminar(SuccessMessageMixin, DeleteView): 
    model = Categoria
    form = Categoria
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoria Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerCategoria') # Redireccionamos a la vista principal 'leer'
    
    #-----------------------------------Categoria-----------------------------------------------------#

 #-----------------------------------Ciudad-----------------------------------------------------#
class ListadoCiudad(CreateView,ListView,SuccessMessageMixin):

    model = Ciudad
    form = Ciudad
    fields = "__all__"
    
    success_message ='Ciudad creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerCiudad') # Redireccionamos a la vista principal 'leer' 
    
class CiudadDetalle (DetailView):
    model =Ciudad

class CiudadActualizar(SuccessMessageMixin,UpdateView):
    model =Ciudad
    form = Ciudad
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Ciudad' de nuestra Base de Datos 
    success_message = 'Ciudad Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leerCiudad') # Redireccionamos a la vista principal 'leer'
    
class CiudadEliminar(SuccessMessageMixin, DeleteView): 
    model = Ciudad
    form = Ciudad
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Ciudad Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerCiudad') # Redireccionamos a la vista principal 'leer'
    
#-----------------------------------Ciudad-----------------------------------------------------#
#-----------------------------------Profesion-----------------------------------------------------#
class ListadoProfesion(CreateView,ListView,SuccessMessageMixin):
 
     model = Profesion
     form = Profesion
     fields = "__all__"
     
     success_message ='Profesion creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerProfesion') # Redireccionamos a la vista principal 'leer' 
     
class ProfesionDetalle (DetailView):
     model =Profesion
 
class ProfesionActualizar(SuccessMessageMixin,UpdateView):
     model =Profesion
     form = Profesion
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Profesion' de nuestra Base de Datos 
     success_message = 'Profesion Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerProfesion') # Redireccionamos a la vista principal 'leer'
     
class ProfesionEliminar(SuccessMessageMixin, DeleteView): 
     model = Profesion
     form = Profesion
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'Profesion Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerProfesion') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------Profesion-----------------------------------------------------#
 
    
    
  #-----------------------------------Departamento-----------------------------------------------------#
class ListadoDepartamento(CreateView,ListView,SuccessMessageMixin):
  
      model = Departamento
      form = Departamento
      fields = "__all__"
      
      success_message ='Departamento creado correctamente'
      def get_success_url(self):        
          return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer' 
      
class DepartamentoDetalle (DetailView):
      model =Departamento
  
class DepartamentoActualizar(SuccessMessageMixin,UpdateView):
      model =Departamento
      form = Departamento
      fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Departamento' de nuestra Base de Datos 
      success_message = 'Departamento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
  
      def get_success_url(self):               
          return reverse('principal:leerDepartamento') # Redireccionamos a la vista principal 'leer'
      
class DepartamentoEliminar(SuccessMessageMixin, DeleteView): 
      model = Departamento
      form = Departamento
      fields = "__all__"     
   
      # Redireccionamos a la página principal luego de eliminar un registro o postre
      def get_success_url(self): 
          success_message = 'Departamento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
          messages.success (self.request, (success_message))       
          return reverse('principal:leerDepartamento') # Redireccionamos a la vista principal 'leer'
      
      #-----------------------------------Departamento-----------------------------------------------------#
  
   
   
 
 
 #-----------------------------------Pais-----------------------------------------------------#
class ListadoPais(CreateView,ListView,SuccessMessageMixin):
     
         model = Pais
         form = Pais
         fields = "__all__"
         
         success_message ='Pais creado correctamente'
         def get_success_url(self):        
             return reverse('principal:leerPais') # Redireccionamos a la vista principal 'leer' 
         
class PaisDetalle (DetailView):
         model =Pais
     
class PaisActualizar(SuccessMessageMixin,UpdateView):
         model =Pais
         form = Pais
         fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Pais' de nuestra Base de Datos 
         success_message = 'Pais Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
     
         def get_success_url(self):               
             return reverse('principal:leerPais') # Redireccionamos a la vista principal 'leer'
         
class PaisEliminar(SuccessMessageMixin, DeleteView): 
         model = Pais
         form = Pais
         fields = "__all__"     
      
         # Redireccionamos a la página principal luego de eliminar un registro o postre
         def get_success_url(self): 
             success_message = 'Pais Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
             messages.success (self.request, (success_message))       
             return reverse('principal:leerPais') # Redireccionamos a la vista principal 'leer'
         
         #-----------------------------------Pais-----------------------------------------------------#
 
 #-----------------------------------Personas-----------------------------------------------------#
class ListadoPersona(CreateView,ListView,SuccessMessageMixin):
     
         model = Persona
         form = Persona
         fields = "__all__"
         
         success_message ='Personas creado correctamente'
         def get_success_url(self):        
             return reverse('principal:leerPersona') # Redireccionamos a la vista principal 'leer' 
         
class PersonaDetalle (DetailView):
         model =Persona
     
class PersonaActualizar(SuccessMessageMixin,UpdateView):
         model =Persona
         form = Persona
         fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Personas' de nuestra Base de Datos 
         success_message = 'Personas Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
     
         def get_success_url(self):               
             return reverse('principal:leerPersona') # Redireccionamos a la vista principal 'leer'
         
class PersonaEliminar(SuccessMessageMixin, DeleteView): 
         model = Persona
         form = Persona
         fields = "__all__"     
      
         # Redireccionamos a la página principal luego de eliminar un registro o postre
         def get_success_url(self): 
             success_message = 'Persona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
             messages.success (self.request, (success_message))       
             return reverse('principal:leerPersona') # Redireccionamos a la vista principal 'leer'
         
         #-----------------------------------Personas-----------------------------------------------------#


 #-----------------------------------ExperienciaPsico-----------------------------------------------------#
class ListadoExperienciaPsico(CreateView,ListView,SuccessMessageMixin):

    model = ExperienciaPsico
    form = ExperienciaPsico
    fields = "__all__"
    
    success_message ='ExperienciaPsico creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerExperienciaPsico') # Redireccionamos a la vista principal 'leer' 
    
class ExperienciaPsicoDetalle (DetailView):
    model =ExperienciaPsico

class ExperienciaPsicoActualizar(SuccessMessageMixin,UpdateView):
    model =ExperienciaPsico
    form = ExperienciaPsico
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'ExperienciaPsico' de nuestra Base de Datos 
    success_message = 'ExperienciaPsico Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leerExperienciaPsico') # Redireccionamos a la vista principal 'leer'
    
class ExperienciaPsicoEliminar(SuccessMessageMixin, DeleteView): 
    model = ExperienciaPsico
    form = ExperienciaPsico
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'ExperienciaPsico Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerExperienciaPsico') # Redireccionamos a la vista principal 'leer'
    
    #-----------------------------------ExperienciaPsico-----------------------------------------------------#
 
  #-----------------------------------Tarifa-----------------------------------------------------#
class ListadoTarifa(CreateView,ListView,SuccessMessageMixin):

    model = Tarifa
    form = Tarifa
    fields = "__all__"
    
    success_message ='Tarifa creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerTarifa') # Redireccionamos a la vista principal 'leer' 
    
class TarifaDetalle (DetailView):
    model =Tarifa

class TarifaActualizar(SuccessMessageMixin,UpdateView):
    model =Tarifa
    form = Tarifa
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Tarifa' de nuestra Base de Datos 
    success_message = 'Tarifa Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leerTarifa') # Redireccionamos a la vista principal 'leer'
    
class TarifaEliminar(SuccessMessageMixin, DeleteView): 
    model = Tarifa
    form = Tarifa
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Tarifa Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerTarifa') # Redireccionamos a la vista principal 'leer'
    
    #-----------------------------------Tarifa-----------------------------------------------------#
  
  
 #-----------------------------------Tratamiento-----------------------------------------------------#
class ListadoTratamiento(CreateView,ListView,SuccessMessageMixin):
 
     model = Tratamiento
     form = Tratamiento
     fields = "__all__"
     
     success_message ='Tratamiento creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerTratamiento') # Redireccionamos a la vista principal 'leer' 
     
class TratamientoDetalle (DetailView):
     model =Tratamiento
 
class TratamientoActualizar(SuccessMessageMixin,UpdateView):
     model =Tratamiento
     form = Tratamiento
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Tratamiento' de nuestra Base de Datos 
     success_message = 'Tratamiento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerTratamiento') # Redireccionamos a la vista principal 'leer'
     
class TratamientoEliminar(SuccessMessageMixin, DeleteView): 
     model = Tratamiento
     form = Tratamiento
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'Tratamiento Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerTratamiento') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------Tratamiento-----------------------------------------------------#
 
 #-----------------------------------TipoPersona-----------------------------------------------------#
class ListadoTipoPersona(CreateView,ListView,SuccessMessageMixin):
 
     model = TipoPersona
     form = TipoPersona
     fields = "__all__"
     
     success_message ='TipoPersona creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerTipoPersona') # Redireccionamos a la vista principal 'leer' 
     
class TipoPersonaDetalle (DetailView):
     model =TipoPersona
 
class TipoPersonaActualizar(SuccessMessageMixin,UpdateView):
     model =TipoPersona
     form = TipoPersona
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'TipoPersona' de nuestra Base de Datos 
     success_message = 'TipoPersona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerTipoPersona') # Redireccionamos a la vista principal 'leer'
     
class TipoPersonaEliminar(SuccessMessageMixin, DeleteView): 
     model = TipoPersona
     form = TipoPersona
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'TipoPersona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerTipoPersona') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------TipoPersona-----------------------------------------------------#
 

  
      #-----------------------------------Antecedentes-----------------------------------------------------#
class ListadoAntecedentes(CreateView,ListView,SuccessMessageMixin):
 
     model = Antecedentes
     form = Antecedentes
     fields = "__all__"
     
     success_message ='Antecedentes creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerAntecedentes') # Redireccionamos a la vista principal 'leer' 
     
class AntecedentesDetalle (DetailView):
     model =Antecedentes
 
class AntecedentesActualizar(SuccessMessageMixin,UpdateView):
     model =Antecedentes
     form = Antecedentes
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Antecedentes' de nuestra Base de Datos 
     success_message = 'Antecedentes Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerAntecedentes') # Redireccionamos a la vista principal 'leer'
     
class AntecedentesEliminar(SuccessMessageMixin, DeleteView): 
     model = Antecedentes
     form = Antecedentes
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'Antecedentes Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerAntecedentes') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------Antecedentes-----------------------------------------------------#
     
  
      #-----------------------------------Cabeza-----------------------------------------------------#
class ListadoCabeza(CreateView,ListView,SuccessMessageMixin):
 
     model = Cabeza
     form = Cabeza
     fields = "__all__"
     
     success_message ='Cabeza creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerCabeza') # Redireccionamos a la vista principal 'leer' 
     
class CabezaDetalle (DetailView):
     model =Cabeza
 
class CabezaActualizar(SuccessMessageMixin,UpdateView):
     model =Cabeza
     form = Cabeza
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cabeza' de nuestra Base de Datos 
     success_message = 'Cabeza Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerCabeza') # Redireccionamos a la vista principal 'leer'
     
class CabezaEliminar(SuccessMessageMixin, DeleteView): 
     model = Cabeza
     form = Cabeza
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'Cabeza Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerCabeza') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------Cabeza-----------------------------------------------------#
      #-----------------------------------Cuerpo-----------------------------------------------------#
class ListadoCuerpo(CreateView,ListView,SuccessMessageMixin):
 
     model = Cuerpo
     form = Cuerpo
     fields = "__all__"
     
     success_message ='Cuerpo creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerCuerpo') # Redireccionamos a la vista principal 'leer' 
     
class CuerpoDetalle (DetailView):
     model =Cuerpo
 
class CuerpoActualizar(SuccessMessageMixin,UpdateView):
     model =Cuerpo
     form = Cuerpo
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cuerpo' de nuestra Base de Datos 
     success_message = 'Cuerpo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerCuerpo') # Redireccionamos a la vista principal 'leer'
     
class CuerpoEliminar(SuccessMessageMixin, DeleteView): 
     model = Cuerpo
     form = Cuerpo
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'Cuerpo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerCuerpo') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------Cuerpo-----------------------------------------------------#
      #-----------------------------------DesarrolloSesion-----------------------------------------------------#
class ListadoDesarrolloSesion(CreateView,ListView,SuccessMessageMixin):
 
     model = DesarrolloSesion
     form = DesarrolloSesion
     fields = "__all__"
     
     success_message ='DesarrolloSesion creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerDesarrolloSesion') # Redireccionamos a la vista principal 'leer' 
     
class DesarrolloSesionDetalle (DetailView):
     model =DesarrolloSesion
 
class DesarrolloSesionActualizar(SuccessMessageMixin,UpdateView):
     model =DesarrolloSesion
     form = DesarrolloSesion
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'DesarrolloSesion' de nuestra Base de Datos 
     success_message = 'DesarrolloSesion Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerDesarrolloSesion') # Redireccionamos a la vista principal 'leer'
     
class DesarrolloSesionEliminar(SuccessMessageMixin, DeleteView): 
     model = DesarrolloSesion
     form = DesarrolloSesion
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'DesarrolloSesion Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerDesarrolloSesion') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------DesarrolloSesion-----------------------------------------------------#
      #-----------------------------------Diagnostico-----------------------------------------------------#
class ListadoDiagnostico(CreateView,ListView,SuccessMessageMixin):
 
     model = Diagnostico
     form = Diagnostico
     fields = "__all__"
     
     success_message ='Diagnostico creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerDiagnostico') # Redireccionamos a la vista principal 'leer' 
     
class DiagnosticoDetalle (DetailView):
     model =Diagnostico
 
class DiagnosticoActualizar(SuccessMessageMixin,UpdateView):
     model =Diagnostico
     form = Diagnostico
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Diagnostico' de nuestra Base de Datos 
     success_message = 'Diagnostico Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerDiagnostico') # Redireccionamos a la vista principal 'leer'
     
class DiagnosticoEliminar(SuccessMessageMixin, DeleteView): 
     model = Diagnostico
     form = Diagnostico
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'Diagnostico Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerDiagnostico') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------Diagnostico-----------------------------------------------------#
      #-----------------------------------tareas-----------------------------------------------------#
class ListadoTareas(CreateView,ListView,SuccessMessageMixin):
 
     model = Tareas
     form = Tareas
     fields = "__all__"
     
     success_message ='Tareas creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerTareas') # Redireccionamos a la vista principal 'leer' 
     
class TareasDetalle (DetailView):
     model =Tareas
 
class TareasActualizar(SuccessMessageMixin,UpdateView):
     model =Tareas
     form = Tareas
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Tareas' de nuestra Base de Datos 
     success_message = 'Tareas Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerTareas') # Redireccionamos a la vista principal 'leer'
     
class TareasEliminar(SuccessMessageMixin, DeleteView): 
     model = Tareas
     form = Tareas
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'Tareas Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerTareas') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------DiagnosticoRelacionado-----------------------------------------------------#
      #-----------------------------------Especialidades-----------------------------------------------------#
class ListadoEspecialidades(CreateView,ListView,SuccessMessageMixin):
 
     model = Especialidades
     form = Especialidades
     fields = "__all__"
     
     success_message ='Especialidades creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerEspecialidades') # Redireccionamos a la vista principal 'leer' 
     
class EspecialidadesDetalle (DetailView):
     model =Especialidades
 
class EspecialidadesActualizar(SuccessMessageMixin,UpdateView):
     model =Especialidades
     form = Especialidades
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Especialidades' de nuestra Base de Datos 
     success_message = 'Especialidades Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerEspecialidades') # Redireccionamos a la vista principal 'leer'
     
class EspecialidadesEliminar(SuccessMessageMixin, DeleteView): 
     model = Especialidades
     form = Especialidades
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'Especialidades Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerEspecialidades') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------Especialidades-----------------------------------------------------#
     
      #-----------------------------------Evolucion-----------------------------------------------------#
class ListadoEvolucion(CreateView,ListView,SuccessMessageMixin):
 
     model = Evolucion
     form = Evolucion
     fields = "__all__"
     
     success_message ='Evolucion creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerEvolucion') # Redireccionamos a la vista principal 'leer' 
     
class EvolucionDetalle (DetailView):
     model =Evolucion
 
class EvolucionActualizar(SuccessMessageMixin,UpdateView):
     model =Evolucion
     form = Evolucion
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Evolucion' de nuestra Base de Datos 
     success_message = 'Evolucion Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerEvolucion') # Redireccionamos a la vista principal 'leer'
     
class EvolucionEliminar(SuccessMessageMixin, DeleteView): 
     model = Evolucion
     form = Evolucion
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'Evolucion Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerEvolucion') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------Evolucion-----------------------------------------------------#
      #-----------------------------------ExamenMental-----------------------------------------------------#
class ListadoExamenMental(CreateView,ListView,SuccessMessageMixin):
 
     model = ExamenMental
     form = ExamenMental
     fields = "__all__"
     
     success_message ='ExamenMental creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerExamenMental') # Redireccionamos a la vista principal 'leer' 
     
class ExamenMentalDetalle (DetailView):
     model =ExamenMental
 
class ExamenMentalActualizar(SuccessMessageMixin,UpdateView):
     model =ExamenMental
     form = ExamenMental
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'ExamenMental' de nuestra Base de Datos 
     success_message = 'ExamenMental Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerExamenMental') # Redireccionamos a la vista principal 'leer'
     
class ExamenMentalEliminar(SuccessMessageMixin, DeleteView): 
     model = ExamenMental
     form = ExamenMental
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'ExamenMental Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerExamenMental') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------ExamenMental-----------------------------------------------------#
      #-----------------------------------FactoresProtectores-----------------------------------------------------#
class ListadoFactoresProtectores(CreateView,ListView,SuccessMessageMixin):
 
     model = FactoresProtectores
     form = FactoresProtectores
     fields = "__all__"
     
     success_message ='FactoresProtectores creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerFactoresProtectores') # Redireccionamos a la vista principal 'leer' 
     
class FactoresProtectoresDetalle (DetailView):
     model =FactoresProtectores
 
class FactoresProtectoresActualizar(SuccessMessageMixin,UpdateView):
     model =FactoresProtectores
     form = FactoresProtectores
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'FactoresProtectores' de nuestra Base de Datos 
     success_message = 'FactoresProtectores Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerFactoresProtectores') # Redireccionamos a la vista principal 'leer'
     
class FactoresProtectoresEliminar(SuccessMessageMixin, DeleteView): 
     model = FactoresProtectores
     form = FactoresProtectores
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'FactoresProtectores Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerFactoresProtectores') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------FactoresProtectores-----------------------------------------------------#
      #-----------------------------------FactoresRiesgo-----------------------------------------------------#
class ListadoFactoresRiesgo(CreateView,ListView,SuccessMessageMixin):
 
     model = FactoresRiesgo
     form = FactoresRiesgo
     fields = "__all__"
     
     success_message ='FactoresRiesgo creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerFactoresRiesgo') # Redireccionamos a la vista principal 'leer' 
     
class FactoresRiesgoDetalle (DetailView):
     model =FactoresRiesgo
 
class FactoresRiesgoActualizar(SuccessMessageMixin,UpdateView):
     model =FactoresRiesgo
     form = FactoresRiesgo
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'FactoresRiesgo' de nuestra Base de Datos 
     success_message = 'FactoresRiesgo Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerFactoresRiesgo') # Redireccionamos a la vista principal 'leer'
     
class FactoresRiesgoEliminar(SuccessMessageMixin, DeleteView): 
     model = FactoresRiesgo
     form = FactoresRiesgo
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'FactoresRiesgo Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerFactoresRiesgo') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------FactoresRiesgo-----------------------------------------------------#
      #-----------------------------------HistoriaClinica-----------------------------------------------------#
class ListadoHistoriaClinica(CreateView,ListView,SuccessMessageMixin):
 
     model = HistoriaClinica
     form = HistoriaClinica
     fields = "__all__"
     
     success_message ='HistoriaClinica creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerHistoriaClinica') # Redireccionamos a la vista principal 'leer' 
     
class HistoriaClinicaDetalle (DetailView):
     model =HistoriaClinica
 
class HistoriaClinicaActualizar(SuccessMessageMixin,UpdateView):
     model =HistoriaClinica
     form = HistoriaClinica
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'HistoriaClinica' de nuestra Base de Datos 
     success_message = 'HistoriaClinica Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerHistoriaClinica') # Redireccionamos a la vista principal 'leer'
     
class HistoriaClinicaEliminar(SuccessMessageMixin, DeleteView): 
     model = HistoriaClinica
     form = HistoriaClinica
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'HistoriaClinica Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerHistoriaClinica') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------HistoriaClinica-----------------------------------------------------#
      #-----------------------------------HistoriaVida-----------------------------------------------------#
class ListadoHistoriaVida(CreateView,ListView,SuccessMessageMixin):
 
     model = HistoriaVida
     form = HistoriaVida
     fields = "__all__"
     
     success_message ='HistoriaVida creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerHistoriaVida') # Redireccionamos a la vista principal 'leer' 
     
class HistoriaVidaDetalle (DetailView):
     model =HistoriaVida
 
class HistoriaVidaActualizar(SuccessMessageMixin,UpdateView):
     model =HistoriaVida
     form = HistoriaVida
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'HistoriaVida' de nuestra Base de Datos 
     success_message = 'HistoriaVida Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerHistoriaVida') # Redireccionamos a la vista principal 'leer'
     
class HistoriaVidaEliminar(SuccessMessageMixin, DeleteView): 
     model = HistoriaVida
     form = HistoriaVida
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'HistoriaVida Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerHistoriaVida') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------HistoriaVida-----------------------------------------------------#
      #-----------------------------------MotivoConsulta-----------------------------------------------------#
class ListadoMotivoConsulta(CreateView,ListView,SuccessMessageMixin):
 
     model = MotivoConsulta
     form = MotivoConsulta
     fields = "__all__"
     
     success_message ='MotivoConsulta creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerMotivoConsulta') # Redireccionamos a la vista principal 'leer' 
     
class MotivoConsultaDetalle (DetailView):
     model =MotivoConsulta
 
class MotivoConsultaActualizar(SuccessMessageMixin,UpdateView):
     model =MotivoConsulta
     form = MotivoConsulta
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'MotivoConsulta' de nuestra Base de Datos 
     success_message = 'MotivoConsulta Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerMotivoConsulta') # Redireccionamos a la vista principal 'leer'
     
class MotivoConsultaEliminar(SuccessMessageMixin, DeleteView): 
     model = MotivoConsulta
     form = MotivoConsulta
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'MotivoConsulta Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerMotivoConsulta') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------MotivoConsulta-----------------------------------------------------#
      #-----------------------------------Paquetes-----------------------------------------------------#
class ListadoPaquetes(CreateView,ListView,SuccessMessageMixin):
 
     model = Paquetes
     form = Paquetes
     fields = "__all__"
     
     success_message ='Paquetes creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerPaquetes') # Redireccionamos a la vista principal 'leer' 
     
class PaquetesDetalle (DetailView):
     model =Paquetes
 
class PaquetesActualizar(SuccessMessageMixin,UpdateView):
     model =Paquetes
     form = Paquetes
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Paquetes' de nuestra Base de Datos 
     success_message = 'Paquetes Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerPaquetes') # Redireccionamos a la vista principal 'leer'
     
class PaquetesEliminar(SuccessMessageMixin, DeleteView): 
     model = Paquetes
     form = Paquetes
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'Paquetes Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerPaquetes') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------Paquetes-----------------------------------------------------#
      #-----------------------------------ProfesionPersona-----------------------------------------------------#
class ListadoProfesionPersona(CreateView,ListView,SuccessMessageMixin):
 
     model = ProfesionPersona
     form = ProfesionPersona
     fields = "__all__"
     
     success_message ='ProfesionPersona creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerProfesionPersona') # Redireccionamos a la vista principal 'leer' 
     
class ProfesionPersonaDetalle (DetailView):
     model =ProfesionPersona
 
class ProfesionPersonaActualizar(SuccessMessageMixin,UpdateView):
     model =ProfesionPersona
     form = ProfesionPersona
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'ProfesionPersona' de nuestra Base de Datos 
     success_message = 'ProfesionPersona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerProfesionPersona') # Redireccionamos a la vista principal 'leer'
     
class ProfesionPersonaEliminar(SuccessMessageMixin, DeleteView): 
     model = ProfesionPersona
     form = ProfesionPersona
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'ProfesionPersona Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerProfesionPersona') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------ProfesionPersona-----------------------------------------------------#
     
      #-----------------------------------RelacionFamiliar-----------------------------------------------------#
class ListadoRelacionFamiliar(CreateView,ListView,SuccessMessageMixin):
 
     model = RelacionFamiliar
     form = RelacionFamiliar
     fields = "__all__"
     
     success_message ='RelacionFamiliar creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerRelacionFamiliar') # Redireccionamos a la vista principal 'leer' 
     
class RelacionFamiliarDetalle (DetailView):
     model =RelacionFamiliar
 
class RelacionFamiliarActualizar(SuccessMessageMixin,UpdateView):
     model =RelacionFamiliar
     form = RelacionFamiliar
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'RelacionFamiliar' de nuestra Base de Datos 
     success_message = 'RelacionFamiliar Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerRelacionFamiliar') # Redireccionamos a la vista principal 'leer'
     
class RelacionFamiliarEliminar(SuccessMessageMixin, DeleteView): 
     model = RelacionFamiliar
     form = RelacionFamiliar
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'RelacionFamiliar Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerRelacionFamiliar') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------RelacionFamiliar-----------------------------------------------------#
      #-----------------------------------Remision-----------------------------------------------------#
class ListadoRemision(CreateView,ListView,SuccessMessageMixin):
 
     model = Remision
     form = Remision
     fields = "__all__"
     
     success_message ='Remision creado correctamente'
     def get_success_url(self):        
         return reverse('principal:leerRemision') # Redireccionamos a la vista principal 'leer' 
     
class RemisionDetalle (DetailView):
     model =Remision
 
class RemisionActualizar(SuccessMessageMixin,UpdateView):
     model =Remision
     form = Remision
     fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Remision' de nuestra Base de Datos 
     success_message = 'Remision Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
     def get_success_url(self):               
         return reverse('principal:leerRemision') # Redireccionamos a la vista principal 'leer'
     
class RemisionEliminar(SuccessMessageMixin, DeleteView): 
     model = Remision
     form = Remision
     fields = "__all__"     
  
     # Redireccionamos a la página principal luego de eliminar un registro o postre
     def get_success_url(self): 
         success_message = 'Remision Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
         messages.success (self.request, (success_message))       
         return reverse('principal:leerRemision') # Redireccionamos a la vista principal 'leer'
     
     #-----------------------------------Remision-----------------------------------------------------#
     
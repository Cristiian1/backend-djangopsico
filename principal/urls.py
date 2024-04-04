
from django.urls import path
from .views import *
from .views import obtener_categorias
from .views import eliminar_categoria
from .views import editar_categoria


urlpatterns = [
    
path('parametros/',Parametros, name='leerpar'),
path('api/categorias/', obtener_categorias, name='obtener_categorias'),
path('crear_categoria/', CrearCategoriaView.as_view(), name='crear_categoria'),
path('API/Categoria/<int:pk>/', eliminar_categoria, name='eliminar_categoria'), 
path('API/Categoria/<int:pk>/', editar_categoria, name='editar_categoria'),


#  #--------------------------------------------URL Categoria ------------------------------------------------------------------------#
    
# path('Categoria/', ListadoCategoria.as_view(template_name = "crud/Categoria/tables.html"), name='leerCategoria'),

# # La ruta 'detalles' en donde mostraremos una página con los detalles de un Categoria o registro 
# path('Categoria/detalle/<int:pk>',CategoriaDetalle.as_view(template_name = "crud/Categoria/detalle.html"), name='leerCategoria'),

# # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Categoria registro de la Base de Datos 
# path('Categoria/editar/<int:pk>', CategoriaActualizar.as_view(template_name = "crud/Categoria/actualizar.html"), name='leerCategoria'), 

# # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
# path('Categoria/eliminar/<int:pk>', CategoriaEliminar.as_view(), name='crud/Categoria/eliminar.html'),     
#  #--------------------------------------------URL Categoria ------------------------------------------------------------------------#
  
  #--------------------------------------------URL Ciudad ------------------------------------------------------------------------#
    
path('Ciudad/', ListadoCiudad.as_view(template_name = "crud/Ciudad/tables.html"), name='leerCiudad'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Ciudad o registro 
path('Ciudad/detalle/<int:pk>',CiudadDetalle.as_view(template_name = "crud/Ciudad/detalle.html"), name='leerCiudad'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Ciudad registro de la Base de Datos 
path('Ciudad/editar/<int:pk>', CiudadActualizar.as_view(template_name = "crud/Ciudad/actualizar.html"), name='leerCiudad'), 

# La ruta 'eliminar' que usaremos para eliminar un Ciudad o registro de la Base de Datos 
path('Ciudad/eliminar/<int:pk>', CiudadEliminar.as_view(), name='crud/Ciudad/eliminar.html'),        
 #--------------------------------------------URL Ciudad ------------------------------------------------------------------------#
  
  #--------------------------------------------URL Profesion ------------------------------------------------------------------------#
    
path('Profesion/', ListadoProfesion.as_view(template_name = "crud/Profesion/tables.html"), name='leerProfesion'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Profesion o registro 
path('Profesion/detalle/<int:pk>',ProfesionDetalle.as_view(template_name = "crud/Profesion/detalle.html"), name='leerProfesion'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Profesion registro de la Base de Datos 
path('Profesion/editar/<int:pk>', ProfesionActualizar.as_view(template_name = "crud/Profesion/actualizar.html"), name='leerProfesion'), 

# La ruta 'eliminar' que usaremos para eliminar un Profesion o registro de la Base de Datos 
path('Profesion/eliminar/<int:pk>', ProfesionEliminar.as_view(), name='crud/Profesion/eliminar.html'),     
 #--------------------------------------------URL Profesion ------------------------------------------------------------------------#


 #--------------------------------------------URL Departamento ------------------------------------------------------------------------#
    
path('Departamento/', ListadoDepartamento.as_view(template_name = "crud/Departamento/tables.html"), name='leerDepartamento'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Departamento o registro 
path('Departamento/detalle/<int:pk>',DepartamentoDetalle.as_view(template_name = "crud/Departamento/detalle.html"), name='leerDepartamento'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Departamento registro de la Base de Datos 
path('Departamento/editar/<int:pk>', DepartamentoActualizar.as_view(template_name = "crud/Departamento/actualizar.html"), name='leerDepartamento'), 

# La ruta 'eliminar' que usaremos para eliminar un Departamento o registro de la Base de Datos 
path('Departamento/eliminar/<int:pk>', DepartamentoEliminar.as_view(), name='crud/Departamento/eliminar.html'),     
 #--------------------------------------------URL Departamento ------------------------------------------------------------------------#
  
  

#--------------------------------------------URL Pais ------------------------------------------------------------------------#
    
path('Pais/', ListadoPais.as_view(template_name = "crud/Pais/tables.html"), name='leerPais'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Pais o registro 
path('Pais/detalle/<int:pk>',PaisDetalle.as_view(template_name = "crud/Pais/detalle.html"), name='leerPais'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Pais registro de la Base de Datos 
path('Pais/editar/<int:pk>', PaisActualizar.as_view(template_name = "crud/Pais/actualizar.html"), name='leerPais'), 

# La ruta 'eliminar' que usaremos para eliminar un Pais o registro de la Base de Datos 
path('Pais/eliminar/<int:pk>', PaisEliminar.as_view(), name='crud/Pais/eliminar.html'),     
 #--------------------------------------------URL Pais ------------------------------------------------------------------------#
  
  #--------------------------------------------URL Persona ------------------------------------------------------------------------#
    
path('Persona/', ListadoPersona.as_view(template_name = "crud/Persona/tables.html"), name='leerPersona'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Persona o registro 
path('Persona/detalle/<int:pk>',PersonaDetalle.as_view(template_name = "crud/Persona/detalle.html"), name='leerPersona'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Persona registro de la Base de Datos 
path('Persona/editar/<int:pk>', PersonaActualizar.as_view(template_name = "crud/Persona/actualizar.html"), name='leerPersona'), 

# La ruta 'eliminar' que usaremos para eliminar un Persona o registro de la Base de Datos 
path('Persona/eliminar/<int:pk>', PersonaEliminar.as_view(), name='crud/Persona/eliminar.html'),     
 #--------------------------------------------URL Persona ------------------------------------------------------------------------#
  
#-------------------------------------------
#--------------------------------------------URL ExperienciaPsico ------------------------------------------------------------------------#
    
path('ExperienciaPsico/', ListadoExperienciaPsico.as_view(template_name = "crud/ExperienciaPsico/tables.html"), name='leerExperienciaPsico'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un ExperienciaPsico o registro 
path('ExperienciaPsico/detalle/<int:pk>',ExperienciaPsicoDetalle.as_view(template_name = "crud/ExperienciaPsico/detalle.html"), name='leerExperienciaPsico'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un ExperienciaPsico registro de la Base de Datos 
path('ExperienciaPsico/editar/<int:pk>', ExperienciaPsicoActualizar.as_view(template_name = "crud/ExperienciaPsico/actualizar.html"), name='leerExperienciaPsico'), 

# La ruta 'eliminar' que usaremos para eliminar un ExperienciaPsico o registro de la Base de Datos 
path('ExperienciaPsico/eliminar/<int:pk>', ExperienciaPsicoEliminar.as_view(), name='crud/ExperienciaPsico/eliminar.html'),     
 #--------------------------------------------URL ExperienciaPsico ------------------------------------------------------------------------#
  
 
#--------------------------------------------URL Tarifa ------------------------------------------------------------------------#
    
path('Tarifa/', ListadoTarifa.as_view(template_name = "crud/Tarifa/tables.html"), name='leerTarifa'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Tarifa o registro 
path('Tarifa/detalle/<int:pk>',TarifaDetalle.as_view(template_name = "crud/Tarifa/detalle.html"), name='leerTarifa'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tarifa registro de la Base de Datos 
path('Tarifa/editar/<int:pk>', TarifaActualizar.as_view(template_name = "crud/Tarifa/actualizar.html"), name='leerTarifa'), 

# La ruta 'eliminar' que usaremos para eliminar un Tarifa o registro de la Base de Datos 
path('Tarifa/eliminar/<int:pk>', TarifaEliminar.as_view(), name='crud/Tarifa/eliminar.html'),     
 #--------------------------------------------URL Tarifa ------------------------------------------------------------------------#
  

#--------------------------------------------URL TipoPersona ------------------------------------------------------------------------#
    
path('TipoPersona/', ListadoTipoPersona.as_view(template_name = "crud/TipoPersona/tables.html"), name='leerTipoPersona'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un TipoPersona o registro 
path('TipoPersona/detalle/<int:pk>',TipoPersonaDetalle.as_view(template_name = "crud/TipoPersona/detalle.html"), name='leerTipoPersona'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un TipoPersona registro de la Base de Datos 
path('TipoPersona/editar/<int:pk>', TipoPersonaActualizar.as_view(template_name = "crud/TipoPersona/actualizar.html"), name='leerTipoPersona'), 

# La ruta 'eliminar' que usaremos para eliminar un TipoPersona o registro de la Base de Datos 
path('TipoPersona/eliminar/<int:pk>', TipoPersonaEliminar.as_view(), name='crud/TipoPersona/eliminar.html'),     
 #

#---------------------------------------
#--------------------------------------------URL Antecedentes ------------------------------------------------------------------------#
    
path('Antecedentes/', ListadoAntecedentes.as_view(template_name = "crud/Antecedentes/tables.html"), name='leerAntecedentes'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Antecedentes o registro 
path('Antecedentes/detalle/<int:pk>',AntecedentesDetalle.as_view(template_name = "crud/Antecedentes/detalle.html"), name='leerAntecedentes'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Antecedentes registro de la Base de Datos 
path('Antecedentes/editar/<int:pk>', AntecedentesActualizar.as_view(template_name = "crud/Antecedentes/actualizar.html"), name='leerAntecedentes'), 

# La ruta 'eliminar' que usaremos para eliminar un Antecedentes o registro de la Base de Datos 
path('Antecedentes/eliminar/<int:pk>', AntecedentesEliminar.as_view(), name='crud/Antecedentes/eliminar.html'),     
 #--------------------------------------------URL Antecedentes ------------------------------------------------------------------------#

 
#--------------------------------------------URL Cabeza ------------------------------------------------------------------------#
    
path('Cabeza/', ListadoCabeza.as_view(template_name = "crud/Cabeza/tables.html"), name='leerCabeza'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Cabeza o registro 
path('Cabeza/detalle/<int:pk>',CabezaDetalle.as_view(template_name = "crud/Cabeza/detalle.html"), name='leerCabeza'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cabeza registro de la Base de Datos 
path('Cabeza/editar/<int:pk>', CabezaActualizar.as_view(template_name = "crud/Cabeza/actualizar.html"), name='leerCabeza'), 

# La ruta 'eliminar' que usaremos para eliminar un Cabeza o registro de la Base de Datos 
path('Cabeza/eliminar/<int:pk>', CabezaEliminar.as_view(), name='crud/Cabeza/eliminar.html'),     
 #--------------------------------------------URL Cabeza ------------------------------------------------------------------------#
#--------------------------------------------URL Cuerpo ------------------------------------------------------------------------#
    
path('Cuerpo/', ListadoCuerpo.as_view(template_name = "crud/Cuerpo/tables.html"), name='leerCuerpo'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Cuerpo o registro 
path('Cuerpo/detalle/<int:pk>',CuerpoDetalle.as_view(template_name = "crud/Cuerpo/detalle.html"), name='leerCuerpo'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Cuerpo registro de la Base de Datos 
path('Cuerpo/editar/<int:pk>', CuerpoActualizar.as_view(template_name = "crud/Cuerpo/actualizar.html"), name='leerCuerpo'), 

# La ruta 'eliminar' que usaremos para eliminar un Cuerpo o registro de la Base de Datos 
path('Cuerpo/eliminar/<int:pk>', CuerpoEliminar.as_view(), name='crud/Cuerpo/eliminar.html'),     
 #--------------------------------------------URL Cuerpo ------------------------------------------------------------------------#
#--------------------------------------------URL DesarrolloSesion ------------------------------------------------------------------------#
    
path('DesarrolloSesion/', ListadoDesarrolloSesion.as_view(template_name = "crud/DesarrolloSesion/tables.html"), name='leerDesarrolloSesion'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un DesarrolloSesion o registro 
path('DesarrolloSesion/detalle/<int:pk>',DesarrolloSesionDetalle.as_view(template_name = "crud/DesarrolloSesion/detalle.html"), name='leerDesarrolloSesion'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un DesarrolloSesion registro de la Base de Datos 
path('DesarrolloSesion/editar/<int:pk>', DesarrolloSesionActualizar.as_view(template_name = "crud/DesarrolloSesion/actualizar.html"), name='leerDesarrolloSesion'), 

# La ruta 'eliminar' que usaremos para eliminar un DesarrolloSesion o registro de la Base de Datos 
path('DesarrolloSesion/eliminar/<int:pk>', DesarrolloSesionEliminar.as_view(), name='crud/DesarrolloSesion/eliminar.html'),     
 #--------------------------------------------URL DesarrolloSesion ------------------------------------------------------------------------#

#--------------------------------------------URL Diagnostico ------------------------------------------------------------------------#
    
path('Diagnostico/', ListadoDiagnostico.as_view(template_name = "crud/Diagnostico/tables.html"), name='leerDiagnostico'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Diagnostico o registro 
path('Diagnostico/detalle/<int:pk>',DiagnosticoDetalle.as_view(template_name = "crud/Diagnostico/detalle.html"), name='leerDiagnostico'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Diagnostico registro de la Base de Datos 
path('Diagnostico/editar/<int:pk>', DiagnosticoActualizar.as_view(template_name = "crud/Diagnostico/actualizar.html"), name='leerDiagnostico'), 

# La ruta 'eliminar' que usaremos para eliminar un Diagnostico o registro de la Base de Datos 
path('Diagnostico/eliminar/<int:pk>', DiagnosticoEliminar.as_view(), name='crud/Diagnostico/eliminar.html'),     
 #--------------------------------------------URL Diagnostico ------------------------------------------------------------------------#


#--------------------------------------------URL Especialidades ------------------------------------------------------------------------#
    
path('Especialidades/', ListadoEspecialidades.as_view(template_name = "crud/Especialidades/tables.html"), name='leerEspecialidades'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Especialidades o registro 
path('Especialidades/detalle/<int:pk>',EspecialidadesDetalle.as_view(template_name = "crud/Especialidades/detalle.html"), name='leerEspecialidades'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Especialidades registro de la Base de Datos 
path('Especialidades/editar/<int:pk>', EspecialidadesActualizar.as_view(template_name = "crud/Especialidades/actualizar.html"), name='leerEspecialidades'), 

# La ruta 'eliminar' que usaremos para eliminar un Especialidades o registro de la Base de Datos 
path('Especialidades/eliminar/<int:pk>', EspecialidadesEliminar.as_view(), name='crud/Especialidades/eliminar.html'),     
 #--------------------------------------------URL Especialidades ------------------------------------------------------------------------#

#--------------------------------------------URL Evolucion ------------------------------------------------------------------------#
    
path('Evolucion/', ListadoEvolucion.as_view(template_name = "crud/Evolucion/tables.html"), name='leerEvolucion'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Evolucion o registro 
path('Evolucion/detalle/<int:pk>',EvolucionDetalle.as_view(template_name = "crud/Evolucion/detalle.html"), name='leerEvolucion'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Evolucion registro de la Base de Datos 
path('Evolucion/editar/<int:pk>', EvolucionActualizar.as_view(template_name = "crud/Evolucion/actualizar.html"), name='leerEvolucion'), 

# La ruta 'eliminar' que usaremos para eliminar un Evolucion o registro de la Base de Datos 
path('Evolucion/eliminar/<int:pk>', EvolucionEliminar.as_view(), name='crud/Evolucion/eliminar.html'),     
 #--------------------------------------------URL Evolucion ------------------------------------------------------------------------#
#--------------------------------------------URL ExamenMental ------------------------------------------------------------------------#
    
path('ExamenMental/', ListadoExamenMental.as_view(template_name = "crud/ExamenMental/tables.html"), name='leerExamenMental'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un ExamenMental o registro 
path('ExamenMental/detalle/<int:pk>',ExamenMentalDetalle.as_view(template_name = "crud/ExamenMental/detalle.html"), name='leerExamenMental'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un ExamenMental registro de la Base de Datos 
path('ExamenMental/editar/<int:pk>', ExamenMentalActualizar.as_view(template_name = "crud/ExamenMental/actualizar.html"), name='leerExamenMental'), 

# La ruta 'eliminar' que usaremos para eliminar un ExamenMental o registro de la Base de Datos 
path('ExamenMental/eliminar/<int:pk>', ExamenMentalEliminar.as_view(), name='crud/ExamenMental/eliminar.html'),     
 #--------------------------------------------URL ExamenMental ------------------------------------------------------------------------#
#--------------------------------------------URL FactoresProtectores ------------------------------------------------------------------------#
    
path('FactoresProtectores/', ListadoFactoresProtectores.as_view(template_name = "crud/FactoresProtectores/tables.html"), name='leerFactoresProtectores'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un FactoresProtectores o registro 
path('FactoresProtectores/detalle/<int:pk>',FactoresProtectoresDetalle.as_view(template_name = "crud/FactoresProtectores/detalle.html"), name='leerFactoresProtectores'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un FactoresProtectores registro de la Base de Datos 
path('FactoresProtectores/editar/<int:pk>', FactoresProtectoresActualizar.as_view(template_name = "crud/FactoresProtectores/actualizar.html"), name='leerFactoresProtectores'), 

# La ruta 'eliminar' que usaremos para eliminar un FactoresProtectores o registro de la Base de Datos 
path('FactoresProtectores/eliminar/<int:pk>', FactoresProtectoresEliminar.as_view(), name='crud/FactoresProtectores/eliminar.html'),     
 #--------------------------------------------URL FactoresProtectores ------------------------------------------------------------------------#
#--------------------------------------------URL FactoresRiesgo ------------------------------------------------------------------------#
    
path('FactoresRiesgo/', ListadoFactoresRiesgo.as_view(template_name = "crud/FactoresRiesgo/tables.html"), name='leerFactoresRiesgo'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un FactoresRiesgo o registro 
path('FactoresRiesgo/detalle/<int:pk>',FactoresRiesgoDetalle.as_view(template_name = "crud/FactoresRiesgo/detalle.html"), name='leerFactoresRiesgo'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un FactoresRiesgo registro de la Base de Datos 
path('FactoresRiesgo/editar/<int:pk>', FactoresRiesgoActualizar.as_view(template_name = "crud/FactoresRiesgo/actualizar.html"), name='leerFactoresRiesgo'), 

# La ruta 'eliminar' que usaremos para eliminar un FactoresRiesgo o registro de la Base de Datos 
path('FactoresRiesgo/eliminar/<int:pk>', FactoresRiesgoEliminar.as_view(), name='crud/FactoresRiesgo/eliminar.html'),     
 #--------------------------------------------URL FactoresRiesgo ------------------------------------------------------------------------#
#--------------------------------------------URL HistoriaClinica ------------------------------------------------------------------------#
    
path('HistoriaClinica/', ListadoHistoriaClinica.as_view(template_name = "crud/HistoriaClinica/tables.html"), name='leerHistoriaClinica'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un HistoriaClinica o registro 
path('HistoriaClinica/detalle/<int:pk>',HistoriaClinicaDetalle.as_view(template_name = "crud/HistoriaClinica/detalle.html"), name='leerHistoriaClinica'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un HistoriaClinica registro de la Base de Datos 
path('HistoriaClinica/editar/<int:pk>', HistoriaClinicaActualizar.as_view(template_name = "crud/HistoriaClinica/actualizar.html"), name='leerHistoriaClinica'), 

# La ruta 'eliminar' que usaremos para eliminar un HistoriaClinica o registro de la Base de Datos 
path('HistoriaClinica/eliminar/<int:pk>', HistoriaClinicaEliminar.as_view(), name='crud/HistoriaClinica/eliminar.html'),     
 #--------------------------------------------URL HistoriaClinica ------------------------------------------------------------------------#
#--------------------------------------------URL HistoriaVida ------------------------------------------------------------------------#
    
path('HistoriaVida/', ListadoHistoriaVida.as_view(template_name = "crud/HistoriaVida/tables.html"), name='leerHistoriaVida'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un HistoriaVida o registro 
path('HistoriaVida/detalle/<int:pk>',HistoriaVidaDetalle.as_view(template_name = "crud/HistoriaVida/detalle.html"), name='leerHistoriaVida'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un HistoriaVida registro de la Base de Datos 
path('HistoriaVida/editar/<int:pk>', HistoriaVidaActualizar.as_view(template_name = "crud/HistoriaVida/actualizar.html"), name='leerHistoriaVida'), 

# La ruta 'eliminar' que usaremos para eliminar un HistoriaVida o registro de la Base de Datos 
path('HistoriaVida/eliminar/<int:pk>', HistoriaVidaEliminar.as_view(), name='crud/HistoriaVida/eliminar.html'),     
 #--------------------------------------------URL HistoriaVida ------------------------------------------------------------------------#








#--------------------------------------------URL MotivoConsulta ------------------------------------------------------------------------#
    

path('MotivoConsulta/', ListadoMotivoConsulta.as_view(template_name="crud/MotivoConsulta/tables.html"), name='listaMotivosConsulta'),
path('MotivoConsulta/detalle/<int:pk>/', MotivoConsultaDetalle.as_view(template_name="crud/MotivoConsulta/detalle.html"), name='detalleMotivoConsulta'),
path('MotivoConsulta/editar/<int:pk>/', MotivoConsultaActualizar.as_view(template_name="crud/MotivoConsulta/actualizar.html"), name='editarMotivoConsulta'),
path('MotivoConsulta/eliminar/<int:pk>/', MotivoConsultaEliminar.as_view(template_name="crud/MotivoConsulta/eliminar.html"), name='eliminarMotivoConsulta'),

 #--------------------------------------------URL MotivoConsulta ------------------------------------------------------------------------#









#--------------------------------------------URL Paquetes ------------------------------------------------------------------------#
    
path('Paquetes/', ListadoPaquetes.as_view(template_name = "crud/Paquetes/tables.html"), name='leerPaquetes'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Paquetes o registro 
path('Paquetes/detalle/<int:pk>',PaquetesDetalle.as_view(template_name = "crud/Paquetes/detalle.html"), name='leerPaquetes'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Paquetes registro de la Base de Datos 
path('Paquetes/editar/<int:pk>', PaquetesActualizar.as_view(template_name = "crud/Paquetes/actualizar.html"), name='leerPaquetes'), 

# La ruta 'eliminar' que usaremos para eliminar un Paquetes o registro de la Base de Datos 
path('Paquetes/eliminar/<int:pk>', PaquetesEliminar.as_view(), name='crud/Paquetes/eliminar.html'),     
 #--------------------------------------------URL Paquetes ------------------------------------------------------------------------#
#--------------------------------------------URL ProfesionPersona ------------------------------------------------------------------------#
    
path('ProfesionPersona/', ListadoProfesionPersona.as_view(template_name = "crud/ProfesionPersona/tables.html"), name='leerProfesionPersona'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un ProfesionPersona o registro 
path('ProfesionPersona/detalle/<int:pk>',ProfesionPersonaDetalle.as_view(template_name = "crud/ProfesionPersona/detalle.html"), name='leerProfesionPersona'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un ProfesionPersona registro de la Base de Datos 
path('ProfesionPersona/editar/<int:pk>', ProfesionPersonaActualizar.as_view(template_name = "crud/ProfesionPersona/actualizar.html"), name='leerProfesionPersona'), 

# La ruta 'eliminar' que usaremos para eliminar un ProfesionPersona o registro de la Base de Datos 
path('ProfesionPersona/eliminar/<int:pk>', ProfesionPersonaEliminar.as_view(), name='crud/ProfesionPersona/eliminar.html'),     
 #--------------------------------------------URL ProfesionPersona ------------------------------------------------------------------------#

#--------------------------------------------URL RecursosEducativos ------------------------------------------------------------------------#
    
path('RecursosEducativos/', ListadoRecursosEducativos.as_view(template_name = "crud/RecursosEducativos/tables.html"), name='leerRecursosEducativos'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un RecursosEducativos o registro 
path('RecursosEducativos/detalle/<int:pk>',RecursosEducativosDetalle.as_view(template_name = "crud/RecursosEducativos/detalle.html"), name='leerRecursosEducativos'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un RecursosEducativos registro de la Base de Datos 
path('RecursosEducativos/editar/<int:pk>', RecursosEducativosActualizar.as_view(template_name = "crud/RecursosEducativos/actualizar.html"), name='leerRecursosEducativos'), 

# La ruta 'eliminar' que usaremos para eliminar un RecursosEducativos o registro de la Base de Datos 
path('RecursosEducativos/eliminar/<int:pk>', RecursosEducativosEliminar.as_view(), name='crud/RecursosEducativos/eliminar.html'),     
 #--------------------------------------------URL RecursosEducativos ------------------------------------------------------------------------#
#--------------------------------------------URL RelacionFamiliar ------------------------------------------------------------------------#
    
path('RelacionFamiliar/', ListadoRelacionFamiliar.as_view(template_name = "crud/RelacionFamiliar/tables.html"), name='leerRelacionFamiliar'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un RelacionFamiliar o registro 
path('RelacionFamiliar/detalle/<int:pk>',RelacionFamiliarDetalle.as_view(template_name = "crud/RelacionFamiliar/detalle.html"), name='leerRelacionFamiliar'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un RelacionFamiliar registro de la Base de Datos 
path('RelacionFamiliar/editar/<int:pk>', RelacionFamiliarActualizar.as_view(template_name = "crud/RelacionFamiliar/actualizar.html"), name='leerRelacionFamiliar'), 

# La ruta 'eliminar' que usaremos para eliminar un RelacionFamiliar o registro de la Base de Datos 
path('RelacionFamiliar/eliminar/<int:pk>', RelacionFamiliarEliminar.as_view(), name='crud/RelacionFamiliar/eliminar.html'),     
 #--------------------------------------------URL RelacionFamiliar ------------------------------------------------------------------------#
#--------------------------------------------URL Remision ------------------------------------------------------------------------#
    
path('Remision/', ListadoRemision.as_view(template_name = "crud/Remision/tables.html"), name='leerRemision'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Remision o registro 
path('Remision/detalle/<int:pk>',RemisionDetalle.as_view(template_name = "crud/Remision/detalle.html"), name='leerRemision'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Remision registro de la Base de Datos 
path('Remision/editar/<int:pk>', RemisionActualizar.as_view(template_name = "crud/Remision/actualizar.html"), name='leerRemision'), 

# La ruta 'eliminar' que usaremos para eliminar un Remision o registro de la Base de Datos 
path('Remision/eliminar/<int:pk>', RemisionEliminar.as_view(), name='crud/Remision/eliminar.html'),     
 #--------------------------------------------URL Remision ------------------------------------------------------------------------#
#-----------------------------------------
#--------------------------------------------URL Tareas ------------------------------------------------------------------------#
    
path('TipoDiagnostico/', ListadoTareas.as_view(template_name = "crud/Tareas/tables.html"), name='leerTareas'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Tareas o registro 
path('Tareas/detalle/<int:pk>',TareasDetalle.as_view(template_name = "crud/Tareas/detalle.html"), name='leerTareas'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tareas registro de la Base de Datos 
path('Tareas/editar/<int:pk>', TareasActualizar.as_view(template_name = "crud/Tareas/actualizar.html"), name='leerTareas'), 

# La ruta 'eliminar' que usaremos para eliminar un Tareas o registro de la Base de Datos 
path('Tareas/eliminar/<int:pk>', TareasEliminar.as_view(), name='crud/Tareas/eliminar.html'),     
 #--------------------------------------------URL Tareas ------------------------------------------------------------------------#

#-
#--------------------------------------------URL Tratamiento ------------------------------------------------------------------------#
    
path('Tratamiento/', ListadoTratamiento.as_view(template_name = "crud/Tratamiento/tables.html"), name='leerTratamiento'),

# La ruta 'detalles' en donde mostraremos una página con los detalles de un Tratamiento o registro 
path('Tratamiento/detalle/<int:pk>',TratamientoDetalle.as_view(template_name = "crud/Tratamiento/detalle.html"), name='leerTratamiento'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un Tratamiento registro de la Base de Datos 
path('Tratamiento/editar/<int:pk>', TratamientoActualizar.as_view(template_name = "crud/Tratamiento/actualizar.html"), name='leerTratamiento'), 

# La ruta 'eliminar' que usaremos para eliminar un Tratamiento o registro de la Base de Datos 
path('Tratamiento/eliminar/<int:pk>', TratamientoEliminar.as_view(), name='crud/Tratamiento/eliminar.html'),     
 #--------------------------------------------URL Tratamiento ------------------------------------------------------------------------#



]
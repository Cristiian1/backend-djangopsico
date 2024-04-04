from django.db import models


class Antecedentes(models.Model):
    idantecedentes = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antecedentes'


class Cabeza(models.Model):
    id_cabeza = models.IntegerField(primary_key=True)
    persona_id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_id_persona')
    fecha = models.DateField(blank=True, null=True)
    valor_total = models.CharField(max_length=45, blank=True, null=True)
    forma_pago = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cabeza'


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    descripcion = models.CharField(max_length=120, db_collation='utf8_spanish_ci')
    imagen = models.ImageField(upload_to='categoria', null=True)
    class Meta:
        managed = False
        db_table = 'categoria'


class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    codigo = models.IntegerField()
    departamento_id_departamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='departamento_id_departamento')

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cuerpo(models.Model):
    id_cuerpo = models.IntegerField(primary_key=True)
    cabeza_idcabeza = models.ForeignKey(Cabeza, models.DO_NOTHING, db_column='CABEZA_idCABEZA')  # Field name made lowercase.
    paquetes_id_paquetes = models.ForeignKey('Paquetes', models.DO_NOTHING, db_column='paquetes_id_paquetes')
    tarifa_id_tarifa = models.ForeignKey('Tarifa', models.DO_NOTHING, db_column='tarifa_id_tarifa')
    valor_unitario = models.CharField(max_length=45)
    valor_total = models.CharField(max_length=45)
    descuento = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuerpo'


class Departamento(models.Model):
    id_departamento = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    codigo = models.IntegerField()
    pais_id_pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais_id_pais')

    class Meta:
        managed = False
        db_table = 'departamento'


class DesarrolloSesion(models.Model):
    id_desarrollo_sesion = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=220, db_collation='utf8_spanish_ci')

    class Meta:
        managed = False
        db_table = 'desarrollo_sesion'


class Diagnostico(models.Model):
    id_diagnostico = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=120, db_collation='utf8_spanish_ci')
    nombre = models.CharField(max_length=120, db_collation='utf8_spanish_ci')
    tipo_diagnostico_id_tipo_diagnostico = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'diagnostico'


class Especialidades(models.Model):
    id_especialidades = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'especialidades'


class Evolucion(models.Model):
    id_evolucion = models.AutoField(primary_key=True)
    id_motivo_consulta = models.OneToOneField('MotivoConsulta', models.DO_NOTHING, db_column='id_motivo_consulta')
    diagnostico_id_diagnostico = models.ForeignKey(Diagnostico, models.DO_NOTHING, db_column='diagnostico_id_diagnostico')
    factores_riesgo_id_factores_riesgo = models.ForeignKey('FactoresRiesgo', models.DO_NOTHING, db_column='factores_riesgo_id_factores_riesgo')
    tratamiento_id_tratamiento = models.ForeignKey('Tratamiento', models.DO_NOTHING, db_column='tratamiento_id_tratamiento')
    historia_vida_id_historia_vida = models.ForeignKey('HistoriaVida', models.DO_NOTHING, db_column='historia_vida_id_historia_vida')
    examen_mental_id_examen_mental = models.ForeignKey('ExamenMental', models.DO_NOTHING, db_column='examen_mental_id_examen_mental')
    relacion_familiar_id_relacion_familiar = models.ForeignKey('RelacionFamiliar', models.DO_NOTHING, db_column='relacion_familiar_id_relacion_familiar')
    factores_protectores_id_factores_protectores = models.ForeignKey('FactoresProtectores', models.DO_NOTHING, db_column='factores_protectores_id_factores_protectores')
    remision_id_remision = models.ForeignKey('Remision', models.DO_NOTHING, db_column='remision_id_remision')
    desarrollo_sesion_id_desarrollo_sesion = models.ForeignKey(DesarrolloSesion, models.DO_NOTHING, db_column='desarrollo_sesion_id_desarrollo_sesion')

    class Meta:
        managed = False
        db_table = 'evolucion'


class ExamenMental(models.Model):
    id_examen_mental = models.IntegerField(primary_key=True)
    examen_mental = models.CharField(max_length=300, db_collation='utf8_spanish_ci')

    class Meta:
        managed = False
        db_table = 'examen_mental'


class ExperienciaPsico(models.Model):
    id_experiencia_psico = models.IntegerField(primary_key=True)
    categoria_id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria_id_categoria')
    persona_id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_id_persona')
    recursos_educativos_id_recursos_educativos = models.ForeignKey('RecursosEducativos', models.DO_NOTHING, db_column='recursos_educativos_id_recursos_educativos')

    class Meta:
        managed = False
        db_table = 'experiencia_psico'


class FactoresProtectores(models.Model):
    id_factores_protectores = models.IntegerField(primary_key=True)
    factores_protectores = models.CharField(max_length=120, db_collation='utf8_spanish_ci')

    class Meta:
        managed = False
        db_table = 'factores_protectores'


class FactoresRiesgo(models.Model):
    id_factores_riesgo = models.IntegerField(primary_key=True)
    factores_riesgo = models.CharField(max_length=120, db_collation='utf8_spanish_ci')

    class Meta:
        managed = False
        db_table = 'factores_riesgo'


class HistoriaClinica(models.Model):
    id_historia_clinica = models.IntegerField(primary_key=True)
    persona_id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='persona_id_persona')
    evolucion_id_evolucion = models.ForeignKey(Evolucion, models.DO_NOTHING, db_column='evolucion_id_evolucion')
    antecedentes_idantecedentes = models.ForeignKey(Antecedentes, models.DO_NOTHING, db_column='antecedentes_idantecedentes')
    experiencia_psico_id_experiencia_psico = models.ForeignKey(ExperienciaPsico, models.DO_NOTHING, db_column='experiencia_psico_id_experiencia_psico')

    class Meta:
        managed = False
        db_table = 'historia_clinica'


class HistoriaVida(models.Model):
    id_historia_vida = models.IntegerField(primary_key=True)
    historia_vida = models.CharField(max_length=120, db_collation='utf8_spanish_ci')

    class Meta:
        managed = False
        db_table = 'historia_vida'


class MotivoConsulta(models.Model):
    id_motivo_consulta = models.IntegerField(primary_key=True)
    motivo_consulta = models.CharField(db_column='Motivo_Consulta', max_length=120, db_collation='utf8_spanish_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'motivo_consulta'


class Pais(models.Model):
    id_pais = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    codigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pais'


class Paquetes(models.Model):
    id_paquetes = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    descripcion = models.CharField(max_length=120, db_collation='utf8_spanish_ci')

    class Meta:
        managed = False
        db_table = 'paquetes'


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)  # The composite primary key (id_persona, ciudad_id_ciudad) found, that is not supported. The first column is selected.
    nombre1 = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    nombre2 = models.CharField(max_length=70, db_collation='utf8_spanish_ci', blank=True, null=True)
    apellido1 = models.CharField(max_length=30, db_collation='utf8_spanish_ci')
    apellido2 = models.CharField(max_length=70, db_collation='utf8_spanish_ci', blank=True, null=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=45)
    nombre_responsable = models.CharField(max_length=45, blank=True, null=True)
    eps = models.CharField(max_length=45, blank=True, null=True)
    correo = models.CharField(max_length=45)
    cedula = models.CharField(max_length=45, blank=True, null=True)
    imagen = models.CharField(max_length=45, blank=True, null=True)
    genero = models.CharField(max_length=45, blank=True, null=True)
    estadocivil = models.CharField(db_column='estadoCivil', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipodocumento = models.CharField(db_column='tipoDocumento', max_length=45, blank=True, null=True)  # Field name made lowercase.
    numerodocumento = models.IntegerField(db_column='numeroDocumento', blank=True, null=True)  # Field name made lowercase.
    lugar_nacimiento = models.CharField(db_column='lugar nacimiento', max_length=45)  # Field renamed to remove unsuitable characters.
    ciudad_id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_id_ciudad')
    tipo_persona_id_tipo_usuario = models.ForeignKey('TipoPersona', models.DO_NOTHING, db_column='tipo_persona_id_tipo_usuario')

    class Meta:
        managed = False
        db_table = 'persona'
        unique_together = (('id_persona', 'ciudad_id_ciudad'),)


class Profesion(models.Model):
    id_profesion = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    especialidades_id_especialidades = models.ForeignKey(Especialidades, models.DO_NOTHING, db_column='especialidades_id_especialidades')

    class Meta:
        managed = False
        db_table = 'profesion'


class ProfesionPersona(models.Model):
    id_profesion_persona = models.IntegerField(primary_key=True)
    profesion_id_profesion = models.ForeignKey(Profesion, models.DO_NOTHING, db_column='profesion_id_profesion')
    persona_id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='persona_id_persona')

    class Meta:
        managed = False
        db_table = 'profesion_persona'


class RecursosEducativos(models.Model):
    id_recursos_educativos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    descripcion = models.CharField(max_length=120, db_collation='utf8_spanish_ci')

    class Meta:
        managed = False
        db_table = 'recursos_educativos'


class RelacionFamiliar(models.Model):
    id_relacion_familiar = models.IntegerField(primary_key=True)
    relacion_familiar = models.CharField(max_length=120, db_collation='utf8_spanish_ci')

    class Meta:
        managed = False
        db_table = 'relacion_familiar'


class Remision(models.Model):
    id_remision = models.IntegerField(primary_key=True)
    profesional = models.CharField(max_length=220, db_collation='utf8_spanish_ci')
    descripcion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'remision'


class Tareas(models.Model):
    id_tarea = models.AutoField(primary_key=True)  # The composite primary key (id_tarea, categoria_id_categoria) found, that is not supported. The first column is selected.
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    descripcion = models.CharField(max_length=120, db_collation='utf8_spanish_ci')
    pregunta1 = models.CharField(max_length=120, db_collation='utf8_spanish_ci')
    pregunta2 = models.CharField(max_length=60)
    categoria_id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING, db_column='categoria_id_categoria')
    respuesta1 = models.CharField(max_length=255, blank=True, null=True)
    respuesta2 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tareas'
        unique_together = (('id_tarea', 'categoria_id_categoria'),)


class Tarifa(models.Model):
    id_tarifa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    descripcion = models.CharField(max_length=120, db_collation='utf8_spanish_ci')
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tarifa'


class TipoPersona(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70, db_collation='utf8_spanish_ci')
    descripcion = models.CharField(max_length=120, db_collation='utf8_spanish_ci')

    class Meta:
        managed = False
        db_table = 'tipo_persona'


class Tratamiento(models.Model):
    id_tratamiento = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=220, db_collation='utf8_spanish_ci')
    numero_sesiones = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tratamiento'
        
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    correo = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'usuarios'

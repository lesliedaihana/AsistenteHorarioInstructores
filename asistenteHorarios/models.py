from django.db import models

# Create your models here.

class Catalogo_Perfiles(models.Model):
    id_Perfiles = models.IntegerField()
    Perfil = models.CharField(max_length=30)

class Catalogo_TipoDocumento(models.Model):
    id_TipoDocumento = models.IntegerField()
    TipoDocumento = models.CharField(max_length=30)

class Ambientes(models.Model):
    id_Ambiente = models.IntegerField()
    Descripcion_Infraestructura = models.CharField(max_length=50)
    Capacidad = models.IntegerField()
    TipoDeAmbiente = models.CharField(max_length=50)

class Resultados(models.Model):
    id_Resultado = models.IntegerField()
    Resultado = models.CharField(max_length=50)
    Abordado = models.BooleanField()

class Competencias(models.Model):
    id_Competencia = models.IntegerField()
    Horas = models.IntegerField()
    Competencia = models.CharField(max_length=150)
    id_Resultado = models.ForeignKey(Resultados, on_delete=models.CASCADE)

class Programas_de_Formacion(models.Model):
    id_ProgramaFormacion = models.IntegerField()
    TipoDePrograma = models.CharField(max_length=50)
    FechaInicioEtapaLectiva = models.DateField()
    FechaFinEtapaLectiva = models.DateField()
    CantidadAprendices = models.IntegerField()
    id_Competencia = models.ForeignKey(Competencias, on_delete=models.CASCADE)

class Coordinaciones(models.Model):
    id_Coordinacion = models.IntegerField()
    Coordinacion = models.CharField(max_length=30)
    id_Ambiente = models.ForeignKey(Ambientes, on_delete=models.CASCADE)

class Instructores(models.Model):
    id_Instructor = models.IntegerField()
    NumeroDocumento = models.CharField(max_length=20)
    id_TipoDocumento = models.ForeignKey(Catalogo_TipoDocumento, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    id_Perfiles = models.ForeignKey(Catalogo_Perfiles, on_delete=models.CASCADE)

class Contratacion(models.Model):
    id_Contratacion = models.IntegerField()
    Fecha_Inicio = models.DateField()
    Fecha_Fin = models.DateField()
    Supervisora = models.CharField(max_length=100)
    id_Instructor = models.ForeignKey(Instructores, on_delete=models.CASCADE)
    id_Coordinacion = models.ForeignKey(Coordinaciones, on_delete=models.CASCADE)

class Diseno_Curricular(models.Model):
    id_Diseno_Curricular = models.IntegerField()
    eventoDi = models.CharField(max_length=180)
    id_Instructor = models.ForeignKey(Instructores, on_delete=models.CASCADE)

class Horario_Instructor(models.Model):
    id_Horario_Instructor = models.IntegerField()
    id_Instructor = models.ForeignKey(Instructores, on_delete=models.CASCADE)
    Fecha_Inicio = models.DateField()
    Fecha_Fin = models.DateField()
    Evento = models.CharField(max_length=50)
    LugarFormacion = models.CharField(max_length=40)
from enum import Enum
from django.db import models

# Create your models here.

class Catalogo_Perfiles(models.Model):
    #id_Perfiles = models.IntegerField()
    Perfil = models.CharField(max_length=30)

class Catalogo_TipoDocumento(models.Model):
    #id_TipoDocumento = models.IntegerField()
    TipoDocumento = models.CharField(max_length=30)

""" class Ambientes(models.Model):
    id_Ambiente = models.IntegerField()
    Descripcion_Infraestructura = models.CharField(max_length=50)
    Capacidad = models.IntegerField()
    TipoDeAmbiente = models.CharField(max_length=50)
"""

class ProgramasFormacion(models.Model):
    NombreProgramaFormacion = models.CharField(max_length=150)
    
"""
class jornada(Enum):
    manana = "MAÑANA"
    tarde = "TARDE"
    noche = "NOCHE"
"""

"""
class Coordinaciones(models.Model):
    id_Coordinacion = models.IntegerField()
    Coordinacion = models.CharField(max_length=30)
    id_Ambiente = models.ForeignKey(Ambientes, on_delete=models.CASCADE) """

class Instructores(models.Model):
    #id_Instructor = models.IntegerField()
    NumeroDocumento = models.CharField(max_length=20)
    id_TipoDocumento = models.ForeignKey(Catalogo_TipoDocumento, null=True, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    id_Perfiles = models.ForeignKey(Catalogo_Perfiles, null=True, on_delete=models.CASCADE)

class Contratacion(models.Model):
    #id_Contratacion = models.IntegerField()
    Fecha_Inicio = models.DateField()  # hay que corregir el tipo de dato a "DateField"
    Fecha_Fin = models.DateField() # hay que corregir el tipo de dato a "DateField"
    Supervisora = models.CharField(max_length=100)
    id_Instructor = models.ForeignKey(Instructores, null=True, on_delete=models.CASCADE)
    horasMensualFormacion = models.IntegerField(null=True)
    #id_Coordinacion = models.ForeignKey(Coordinaciones, on_delete=models.CASCADE)

""" class Diseno_Curricular(models.Model):
    id_Diseno_Curricular = models.IntegerField()
    eventoDi = models.CharField(max_length=180)
    id_Instructor = models.ForeignKey(Instructores, on_delete=models.CASCADE)"""

class Horario_Instructor(models.Model):
    #id_Horario_Instructor = models.IntegerField()
    id_Instructor = models.ForeignKey(Instructores, on_delete=models.CASCADE)
    Fecha_Inicio = models.DateTimeField()
    Fecha_Fin = models.DateTimeField()
    Evento = models.TextField(max_length=500, help_text="Ingrese el evento: Competencia + Resultado + activiad de proyecto")
    LugarFormacion = models.CharField(max_length=50)

class Competencias(models.Model):
    competencia = models.TextField(max_length=400)
    codigoCompetencia = models.CharField(max_length=20, null=True)
    Horas = models.IntegerField()
    ProgramasFormaciones = models.ManyToManyField(ProgramasFormacion) 

class Resultados(models.Model):
    Resultado = models.TextField(max_length=300)
    Abordado = models.BooleanField()
    Competencia = models.ForeignKey(Competencias, on_delete=models.CASCADE)

class FichasCaracterizacion(models.Model):
    Ficha = models.CharField(max_length=10)
    FechaInicioEtapaLectiva = models.DateField()
    FechaFinEtapaLectiva = models.DateField()
    CantidadAprendices = models.IntegerField()
    Jornada = models.CharField(max_length=30)
    ProgramasFormacion = models.ForeignKey(ProgramasFormacion, on_delete=models.CASCADE)
    Avance = models.ManyToManyField(Resultados)
    

class OrdenRAP(models.Model):
    OrdenRap = models.IntegerField()
    Resultado = models.ManyToManyField(Resultados)
    Ficha = models.ManyToManyField(FichasCaracterizacion) 

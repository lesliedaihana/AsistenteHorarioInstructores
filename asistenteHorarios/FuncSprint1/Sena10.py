#Obtener la cantidad de horas cargadas de cada instructor y compararla con la cantidad de horas que debería impartir, dependiendo de un periodo determinado de tiempo

# Obtener el objeto (registro del instructor) - consulta con filtro para un instructor determinado
# 1. Consultar la BD y obtener las horas mensuales que debe impartir un instructor, de la tabla Contratación
#2. Constultar la BD y obtener las horas programadas a un instructor a partir de los eventos de la tabla Horario_Instructor. QuerySet
#3. Realizar algoritmo para obtener la sumatoria de la duración de los eventos
#4. Realizar la comparación

from asistenteHorarios.models import Horario_Instructor, Instructores, Contratacion
from datetime import datetime, timedelta

def sena10(instructor, fechaInicio, fechaFin):
    consultaHorarioInstructor = Horario_Instructor.objects.filter(id_Instructor = instructor[0], Fecha_Inicio__gte = fechaInicio).filter(Fecha_Fin__lte = fechaFin)
    dur = timedelta(0)
    for iteracion in consultaHorarioInstructor:
        dur += iteracion.Fecha_Fin - iteracion.Fecha_Inicio
    return dur


#instructor = Instructores.objects.filter(id = 6) 
# consultaHorasMensualFormacion = Contratacion.objects.filter(id_Instructor = instructor[0]) 
# HorasMensualFormacion = consultaHorasMensualFormacion[0].horasMensualFormacion

# PeriodoTiempo = 1             # suponiendo meses el inicio como la fecha de inicio 

#print(sena10(instructor,PeriodoTiempo,HorasMensualFormacion))
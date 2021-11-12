from django.shortcuts import render
from django.http import HttpResponse
from asistenteHorarios.FuncSprint1.Sena10 import sena10
from asistenteHorarios.models import Horario_Instructor, Instructores, Contratacion
from datetime import datetime, timedelta

def prueba(request):
    instructor = Instructores.objects.filter(id = 6) 
    consultaHorasMensualFormacion = Contratacion.objects.filter(id_Instructor = instructor[0]) 
    HorasMensualFormacion = consultaHorasMensualFormacion[0].horasMensualFormacion
    PeriodoTiempo = 1             # suponiendo meses el inicio como la fecha de inicio 
    ctx = {"Mensaje":sena10(instructor)}
    return render(request, 'prueba.html', ctx)

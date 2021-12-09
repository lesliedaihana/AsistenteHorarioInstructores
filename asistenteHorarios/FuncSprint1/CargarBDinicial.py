from django.http import request
from django.shortcuts import render
from asistenteHorarios.models import Instructores, Contratacion
import csv, io
from django.contrib import messages
from datetime import date, datetime

# Esta función maneja la introducción inicial de datos a la BD

def inBD(request):
    template = "CargarBD.html"
    #data = Ambientes.objects.all()
    """prompt = {
        'order': 'Order of the CSV should be name, email, address, phone, profile',
        'profiles': data    
            }"""
    if request.method == "GET":
        return render(request, template)
    ctx = {}
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = Instructores.objects.update_or_create(
        Nombre = column[0],
        Apellido = column[1],
        NumeroDocumento = column[2],
        )
        created1 = Contratacion.objects.update_or_create(
        Fecha_Inicio = column[3],
        Fecha_Fin = column[4],
        Supervisora = column[5]
        )
    
    return render(request, template) 

class cargarBDinicial:

    def __init__(self, file):
        self.file = file

    def tipoFileCsv(self):
        if not self.file.name.endswith('.csv'):
            mensaje = 'THIS IS NOT A CSV FILE'
        else:
            mensaje = 'Este si es un CSV FILE'        
        return mensaje
    
    def InsertInstContr(self):            
        #data_set = self.file.read().decode('UTF-8')
        data_set = self.file.read()
        self.io_string = io.StringIO(data_set)
        next(self.io_string)
        for column in csv.reader(self.io_string, delimiter=',', quotechar="|"):

            RegInstructores = Instructores.objects.create(Nombre = column[0],Apellido = column[1],NumeroDocumento = column[2])

            RegContratacion = Contratacion.objects.create(Fecha_Inicio = datetime.strptime(column[3], '%Y-%m-%d'), Fecha_Fin = datetime.strptime(column[4], '%Y-%m-%d'), Supervisora = column[5], id_Instructor = RegInstructores, horasMensualFormacion = column[6])

        return

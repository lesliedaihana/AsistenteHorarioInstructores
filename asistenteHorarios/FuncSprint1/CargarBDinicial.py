from django.shortcuts import render
from asistenteHorarios.models import Instructores, Contratacion, Ambientes
import csv, io
from django.contrib import messages

# Esta función maneja la introducción inicial de datos a la BD

def inBD(request):
    template = "CargarBD.html"
    data = Ambientes.objects.all()
    prompt = {
        'order': 'Order of the CSV should be name, email, address, phone, profile',
        'profiles': data    
              }
    if request.method == "GET":
        return render(request, template, prompt)
    ctx = {}
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        created = Ambientes.objects.update_or_create(
        id_Ambiente = column[0],
        Descripcion_Infraestructura = column[1],
        Capacidad = column[2],
        TipoDeAmbiente = column[3]
        )
        # created1 = Contratacion.objects.update_or_create(
        # Fecha_Inicio = column[3],
        # Fecha_Fin = column[4],
        # Supervisora = column[5]
        # )
    
    return render(request, template, ctx)

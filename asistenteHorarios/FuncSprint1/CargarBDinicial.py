from django.shortcuts import render
from asistenteHorarios import models

# Esta función maneja la introducción inicial de datos a la BD

def inBD(request):
    #connection = MySQLdb.Connect(host='**', user='**', passwd='**', db='**')
    cursor = connection.cursor()
    query = "LOAD DATA INFILE '/path/to/my/file' INTO TABLE sometable FIELDS TERMINATED BY ';' ENCLOSED BY '\"' ESCAPED BY '\\\\'"
    cursor.execute( query )
    connection.commit()
    return(request,"cargarBD.html")
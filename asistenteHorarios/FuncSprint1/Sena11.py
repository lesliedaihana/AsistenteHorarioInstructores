# 1. Conseguir horario de cada instructor y Conseguir cuantas horas al mes debe impartir el instructor
#   Alternativa 1:Consultando la tabla Horario_Instructor "hasta cuando el instructor se queda sin eventos" y la  
    #eventosOrdenado = sorted(consultaHorario, key=lambda x: x.Fecha_Fin)
#   Alternativa 2: Conseguir el querySet de la consulta  a la tabla Horario_Instructor, con los parametros de el instructor, el periodo de tiempo y horasMensualFormacion, y 
#   se analiza cuando termina cada uno de los RAP
#   "Cada vez que termine un RAP se genera un previsión"
#   Entregar al usuario el cuando (al menos un mes antes) y cuáles son los últiomos RAP's con los que el insructor termina
#   A través de un listado en orden del instructor que menos carga tenga la que mas tenga 
# -Ver cuantas horas utiliza a diario para una competencia
# -Realizar funcion que en base a las horas restantes y las horas utilizadas a diario
# prevea la finalizacion de una competencia
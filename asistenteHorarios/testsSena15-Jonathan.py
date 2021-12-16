from django.test import TestCase
from asistenteHorarios.FuncSprint1.Sena10 import sena10Prueba
from asistenteHorarios.models import FichasCaracterizacion,Horario_Instructor, Instructores, ProgramasFormacion,Competencias,Ambientes,Coordinaciones
import pandas, random
from datetime import date, datetime
from unittest.case import SkipTest, skip

def setUpModule():
    print("pruebaSena15(TestCase)")

def tearDownModule():
    print('tearDownModule()')

class pruebaSena10(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("pruebaSena15(TestCase)")
        for i in range(1,6):
            ficha = random.randint(0, 9999999999)
            cantidad = random.randint(0,50)
            doc=random.randint(0, 9999999999)
            nombre = 'nombre' + str(i)
            apellido = 'apellido' + str(i)
            programa = 'programa' + str(i)
            competencia = 'competencia'+str(i)
            codicomp = random.randint(0, 9999999999)
            horas = random.randint(0, 60)

            CrearFichaCaracterizacion = FichasCaracterizacion.objects.create(Ficha = ficha, FechaInicioEtapaLectiva = date(2021,6,15,tzinfo='UTC'), FechaFinEtapaLectiva = date(2021,6,15,tzinfo='UTC'), CantidadAprendices=cantidad)

            CrearInstructores = Instructores.objects.create(NumeroDocumento = doc, id_TipoDocumento = 'Cedula', Nombre = nombre, Apellido = apellido)

            CrearProgramasFormacion=ProgramasFormacion.objects.create(NombreProgramaFormacion = programa)
            
            CrearCompetencias=Competencias.objects.create(competencia = competencia, codigoCompetencia = codicomp, Horas = horas, ProgramasFormaciones = programa)




    @classmethod
    def tearDownClass(cls) -> None:
        print('\ntearDownClass aplicado')
    
    
    def testA1(self):
        self.assertEqual(Ambientes.id_Ambiente,Coordinaciones.id_Ambiente)
        self.assertEqual(Instructores.Id_intructor,Coordinaciones.id_instructor)


    def testB1(self):
        self.assertLess(Horario_Instructor.Fecha_Fin, FichasCaracterizacion.FechaFinEtapaLectiva)
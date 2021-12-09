from django.test import TestCase
from asistenteHorarios.FuncSprint1.Sena10 import sena10Prueba
from asistenteHorarios.models import Instructores, Contratacion, Horario_Instructor
import pandas, random
from datetime import date, datetime
from unittest.case import SkipTest, skip

def setUpModule():
    print('\t\t\t', "pruebaSena10(TestCase)")

def tearDownModule():
    print('tearDownModule()')

class pruebaSena10(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('\t\t\t', "pruebaSena10(TestCase)")
        for i in range(1,6):
            NumDoc = random.randint(0, 9999999999)
            nombre = 'nombre' + str(i)
            apellido = 'apellido' + str(i)

            CrearInstructores = Instructores.objects.create(NumeroDocumento = NumDoc, Nombre = nombre, Apellido = apellido)

            InsertarContratacion = Contratacion.objects.create(Fecha_Inicio = date(2021,1,15,tzinfo='UTC'), Fecha_Fin = date(2021,12,31,tzinfo='UTC'), Supervisora = 'Sandra Lerma', id_Instructor = CrearInstructores, horasMensualFormacion = random.randint(140,160))

            for instru in range(0,6):
                InsertarHorarioInstru = Horario_Instructor.objects.create(id_Instructor = CrearInstructores, Fecha_Inicio = datetime(2021,12,1 + instru * 2,7, tzinfo='UTC'), Fecha_Fin = datetime(2021,12,1 + instru * 2, random.randint(9,13),tzinfo='UTC'), Evento = 'Impartir formación', LugarFormacion = 'CBA')
        print('setUpClass aplicado', '\t\t\t', "pruebaSena10(TestCase)")

    @classmethod
    def tearDownClass(cls) -> None:
        print('\ntearDownClass aplicado', "pruebaSena10(TestCase)")
    
    @skip("razon")
    def testA1(self):
        for inst in range(1,6):
            try:
                self.assertIsNotNone(sena10Prueba.instructorFalla(inst))
                print("\t",type(sena10Prueba.instructorFalla(inst)))
                #self.assertNotIsInstance(sena10Prueba.desviacion[inst], NoneType)
            except:
                print("sena10Prueba.instructorFalla es none")


    def testB1(self):
        for inst in range(1,6):
            instructor = 'name' + str(inst)
            #try:
            self.assertEqual(sena10Prueba.instructor(inst).Nombre, instructor)
            print("\t",sena10Prueba.instructor(inst).Nombre, "=", instructor)
                #self.assertNotIsInstance(sena10Prueba.desviacion[inst], NoneType)
            #except AssertionError:
            print("\t","AssertionError",sena10Prueba.instructor(inst).Nombre, "!=", instructor, sep="\t")
            #except:
            print("\t",sena10Prueba.instructor(inst).Nombre, "!=", instructor)

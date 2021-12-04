from _typeshed import NoneType
from datetime import date, datetime
from logging import exception
from unittest.case import SkipTest, skip
from django.test import TestCase
import io
from asistenteHorarios.FuncSprint1.CargarBDinicial import cargarBDinicial
from asistenteHorarios.models import Instructores, Contratacion, Horario_Instructor
import pandas, random

class pruebaCargarBDIncial(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        directorio = 'D:/reposClon/AsistenteHorariosInstructores/prueba1.csv'
        cls.archivo = open(directorio,'r')
        cls.objeto = cargarBDinicial(cls.archivo)
        cls.pan_archivo = pandas.read_csv(directorio)
        print('setUpClass aplicado')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.archivo.close()
        print('\ntearDownClass aplicado')

    @skip('razon')
    def testA1(self):
        self.assertIsInstance(self.archivo, io.TextIOWrapper)
        print('testA1 aplicado')

    @skip('razon')
    def testA2(self):
        self.assertEqual(self.objeto.tipoFileCsv(),'Este si es un CSV FILE')
        print('Se ejecuto el testA2')

    def testA3(self):
        self.assertEqual(len(self.pan_archivo.axes[1]), 7)
        print('se ejecuto el testA3')

    @skip('razon')
    def testB1(self):
        insertarInstructoresContratacion = self.objeto.InsertInstContr()
        print('se ejecutó self.objeto.InsertInstContr()')
        self.assertEqual(Instructores.objects.get(id = 1).Nombre, 'Nelson')
        self.assertEqual(Instructores.objects.get(id = 1).Apellido, 'DiaZ')
    
#Obtener la cantidad de horas cargadas de cada instructor y compararla con la cantidad de horas que debería impartir, dependiendo de un periodo determinado de tiempo
# PRUEBAS
# testA1 verificar que la respuesta contenga los atributos / valores de identificación del instructor, desviación de la cantidad de horas normales y el periodo de tiempo
# testA2 verificar que la respuesta contenga todos los registros de instructores válidos
# testB1 verificar que los resultados sean correctos

class pruebaSena10(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        for i in range(1,6):
            NumDoc = random.randint(0, 9999999999)
            nombre = 'nombre' + str(i)
            apellido = 'apellido' + str(i)

            CrearInstructores = Instructores.objects.create(NumeroDocumento = NumDoc, Nombre = nombre, Apellido = apellido)

            InsertarContratacion = Contratacion.objects.create(Fecha_Inicio = date(2021,1,15), Fecha_Fin = date(2021,12,31), Supervisora = 'Sandra Lerma', id_Instructor = CrearInstructores, horasMensualFormacion = random.randint(140,160))

            for instru in range(0,6):
                InsertarHorarioInstru = Horario_Instructor.objects.create(id_Instructor = CrearInstructores, Fecha_Inicio = datetime(2021,12,1 + instru * 2,7), Fecha_Fin = datetime(2021,12,1 + instru * 2, random.randint(9,13)), Evento = 'Impartir formación', LugarFormacion = 'CBA')
        print('setUpClass aplicado')

    @classmethod
    def tearDownClass(cls) -> None:
        print('\ntearDownClass aplicado')
    
    def testA1(self):
        for inst in range(0,5):
            try:
                self.assertNotIsInstance(sena10.instructor()[i], NoneType)
                self.assertNotIsInstance(sena10.desviacion()[i], NoneType)
            except:
                pass

    def testA2(self):
        self.assertEqual(len(sena10(), 5)

    def testB1(self):
        




 










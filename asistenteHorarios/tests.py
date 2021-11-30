from unittest.case import SkipTest, skip
from django.test import TestCase
import io
from asistenteHorarios.FuncSprint1.CargarBDinicial import cargarBDinicial
from asistenteHorarios.models import Instructores, Contratacion
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
# testA1 verificar que la respuesta contenga los atributos / valores de identificación del instructor, cantidad de horas que debería impartir, la cantidad de horas que está impartiendo y el periodo de tiempo
# testA2 verificar que la respuesta contenga todos los registros de instructores válidos
# testB1 verificar que los resultados sean correctos

class pruebaSena10(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NumDoc = random.randint(0, 9999999999)
        nombre = 'nombre'
        apellido = 'apellido'
        CrearInstructores = Instructores.objects.create(NumeroDocumento = NumDoc, Nombre = nombre, Apellido = apellido)
        print('setUpClass aplicado')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.archivo.close()
        print('\ntearDownClass aplicado')




 










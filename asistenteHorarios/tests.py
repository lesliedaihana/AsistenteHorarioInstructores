from django.test import TestCase
import io
from asistenteHorarios.FuncSprint1.CargarBDinicial import cargarBDinicial
from asistenteHorarios.models import Instructores, Contratacion

class pruebaCargarBDIncial(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.archivo = open('D:/reposClon/AsistenteHorariosInstructores/prueba1.csv','r')
        cls.objeto = cargarBDinicial(cls.archivo)
        print('setUpClass aplicado')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.archivo.close()
        print('tearDownClass aplicado')

    def testA1(self):
        self.assertIsInstance(self.archivo, io.TextIOWrapper)
        print('testA1 aplicado')

    def testA2(self):
        self.assertEqual(self.objeto.tipoFileCsv(),'Este si es un CSV FILE')
        print('Se ejecuto el testA2')

    def testB1(self):
        insertarInstructoresContratacion = self.objeto.InsertInstContr()
        print('se ejecutó self.objeto.InsertInstContr()')
        self.assertEqual(Instructores.objects.get(id = 1).Nombre, 'NelsoN')
        self.assertEqual(Instructores.objects.get(id = 1).Apellido, 'Diaz')


 










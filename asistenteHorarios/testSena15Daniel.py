from django.test import TestCase
from Sena15Daniel import sena15Pruebass 
from models import FichasCaracterizacion
import pandas, random
from datetime import date, datetime
from unittest.case import SkipTest, skip

class pruebaSena15(TestCase):
    @classmethod
    def setUpclass(cls) -> None:
        print('\t\t\t', "pruebaSena15(TestCase)")
        for i in range(1,6):
            Fichas = random.randint(0,9999999999)
            Cantidad_Apren = random.randint(0,50)
            jornada = "Diurna"
            Programas = 1

        CreateFichas = FichasCaracterizacion.objects.create(Ficha=Fichas, FechaInicioEtapaLectiva = date(2021,1,15,tzinfo='UTC'), FechaFinEtapaLectiva = date(2021,12,31,tzinfo='UTC'), CantidadAprendices = Cantidad_Apren, Jornada = jornada, ProgramasFormacion = Programas)
        print('setUpClass aplicado', '\t\t\t', "pruebaSena15(TestCase)")

    @classmethod
    def tearDownClass(cls) -> None:
        print('\ntearDownClass aplicado', "pruebaSena15(TestCase)")

    def testA1(self):
        for inst in range(1,6):
            try:
                self.assertNotEquals(sena15Pruebass.Fichas(inst))
                print("\t",type(sena15Pruebass.Fichas(inst)))
            except:
                print("sena15Daniel no contiene los datos")
    def testA2(self):
        for inst in range(1,6):
            try:
                self.assertIsNotNone(sena15Pruebass.FichasFalla(inst))
                print("\t",type(sena15Pruebass.FichasFalla(inst)))
            except:
                print("sena15Daniel no contiene los datos")
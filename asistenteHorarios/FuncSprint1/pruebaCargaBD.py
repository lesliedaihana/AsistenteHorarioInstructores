# A. verificar que el archivo y/o información suministrada por el usuario sea una base de datos -> el archivo sea csv, por una parte revisando el nombre, validar la estructura del archivo
#           1. el archivo ingresado sea de tipo csv
# B. verificar que la función CargarBD gestione el almacenamiento de los siguientes campos:
#   datos básicos del instructor (nombres, apellidos, tipo de documento, número de documento)
#   tipo de instructor (planta / contratista)
#   la cantidad de horas
#   el perfil profesional
#   Programas de formación que puede orientar
#   Competencia que puede impartir
#           1. Revisar que la base de datos tenga registros con los campos descritos anteriormente

import unittest
import csv, io
from datetime import date, datetime
from asistenteHorarios.FuncSprint1.CargarBDinicial import cargarBDinicial

class pruebaCargarBDIncial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.archivo = open('D:/reposClon/AsistenteHorariosInstructores/prueba1.csv','r')
        print('setUpClass ejecutado')
        #self.io_string = inBD(archivo)         # suponiendo que inBD() retorne el archivo originalmente introducido
        #self.CSV = csv() 

    def testA1(self):
        archPrueba = cargarBDinicial(self.archivo)
        self.assertIsInstance(archPrueba, io.TextIOWrapper)
        print('testA1 aplicado')

    # def testB1(self):
    #     self.assertEqual(InstructoresNombre, NombrePrueba)
    #     self.assertEqual(InstructoresApellido, ApellidoPrueba)
    #     self.assertEqual(InstructoresTipoDocumento, TipoDocumentoPrueba)
    #     self.assertEqual(InstructoresNumeroDocumento, NumeroDocumentoPrueba)










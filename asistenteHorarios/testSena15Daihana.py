
from django.test import TestCase
from asistenteHorarios.FuncSprint1.Sena15 import sena15Prueba



#   e) El instructor no debe sobrepasar las 10 horas diarias, ni semanalmente de la cantidad de horas / 4


class sena15(TestCase):
    
    def setUp(self):
        self.Pruebas15ins=4


   def testDA(self):
       self.assertEquals (sena15.horasDiarias,10)
       
    







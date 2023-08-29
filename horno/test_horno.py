from Horno import ControlHorno
from unittest import TestCase, main
from unittest.mock import MagicMock, patch

def validar_horno(control):
    solicitar_mantenimiento = control.check_resistencias()

    return 'Solicitar mantenimiento' if solicitar_mantenimiento else 'Ok'

class HornoTest(TestCase):

   def test_horno_ok(self):
        control = ControlHorno()
        control.sensor_resistencias = MagicMock()
        control.sensor_resistencias.resistencias_activas.return_value = 3
        estado_horno = validar_horno(control)
        self.assertTrue(estado_horno, 'Ok')
        
   def test_horno_error(self):
        control = ControlHorno()
        control.sensor_resistencias = MagicMock()
        control.sensor_resistencias.resistencias_activas.return_value = 2
        estado_horno = validar_horno(control)
        self.assertTrue(estado_horno, 'Ok')

main(__name__)
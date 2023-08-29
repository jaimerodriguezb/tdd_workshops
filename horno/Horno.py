#from sensores import SensorResistencias


class ControlHorno():
   def __init__(self):
       self.sensor_resistencias = None


   def check_resistencias(self):
       resistencias_calentendo = self.sensor_resistencias.resistencias_activas()
       return resistencias_calentendo == 3

import unittest
import numpy as np

def calcular_entrada(x,w):
    return np.dot(x,w)
   

class TestPerceptron(unittest.TestCase):
   
    def test_calcular_entrada(self):
        x = [1,2,3]
        w = [0.1,0.2,0.3]
        y1 = None
       
        y1 = calcular_entrada(x,w)
       
        self.assertEqual(y1,1.4)

    def test_init_perceptron(self):
        inputs = 2

        p = Perceptron(inputs)

        self.assertTrue(type(p) is Perceptron)


unittest.main(__name__)
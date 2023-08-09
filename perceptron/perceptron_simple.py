import unittest
import numpy as np

def calcular_entrada(x,w):
    return np.dot(x,w)

class Perceptron:
    def __init__(self, inputs):
        self.inputs = inputs
        self.x = [0 for i in range(self.inputs)]
        self.w = self.x
        self.b = 0
        self.output = 0
    
    def update(self, x=None, w=None, b=None):
        if x and len(x) == self.inputs:
            self.x = x
        if w and len(w) == self.inputs:
            self.w = w
        if b:
            self.b = b

    def calculate(self):
        return 1 if (np.dot(self.x, self.w) + self.b) > 0.5 else 0

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

    def test_calcular_perceptron(self):
        inputs = 2
        
        p = Perceptron(inputs)
        p.update(x=[1,2,3], w=[0.1,0.2,0.3], b=0)
        output = p.calculate()

        self.assertTrue(type(p) is Perceptron)




unittest.main(__name__)
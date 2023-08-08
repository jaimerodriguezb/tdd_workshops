import unittest

def calcular_entrada(x1,x2,x3,w1,w2,w3):
    return x1*w1 + x2*w2 + x3*w3

class TestPerceptron(unittest.TestCase):
    
    def test_calcular_entrada(self):
        x1 = 1
        x2 = 2
        x3 = 3
        w1 = 0.1
        w2 = 0.2
        w3 = 0.3
        y1 = None
        y1 = calcular_entrada(x1,x2,x3,w1,w2,w3)
        
        self.assertEqual(y1,1.4)


unittest.main(__name__)
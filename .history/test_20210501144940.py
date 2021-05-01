import unittest

from calculadora import (
    Calculadora, 
    CalculadoraCientifica
)

from math import log, sqrt

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        self.values_a = [i for i in range(1, 100)]
        self.values_b = [i for i in range(1, 100)]
        self.calculadoras = []
        
        for a in self.values_a:
            for b in self.values_b:
                self.calculadoras.append(Calculadora(a, b))

    def test_sumar(self):
        for c in self.calculadoras:
            c.sumar()
            self.assertEquals(c.get_suma(), c.a + c.b)
            
    def test_restar(self):
        for c in self.calculadoras:
            c.restar()
            self.assertEquals(c.get_resta(), c.a - c.b)
            
    def test_multiplicar(self):
        for c in self.calculadoras:
            c.multiplicar()
            self.assertEquals(c.get_multiplicacion(), c.a * c.b)
            
    def test_dividir(self):
        for c in self.calculadoras:
            if c.b != 0:
                c.dividir()
                self.assertEquals(c.get_division(), c.a / c.b)
            
    def test_get_a(self):
        for c in self.calculadoras:
            self.assertEquals(c.get_a(), c.a)
            
    def test_get_b(self):
        for c in self.calculadoras:
            self.assertEquals(c.get_b(), c.b)
            
class TestCalculadoraCientifica(unittest.TestCase):
    
    def setUp(self):
        self.values_a = [i for i in range(1, 100)]
        self.values_b = [i for i in range(1, 10)]
        self.calculadoras = []
        
        for a in self.values_a:
            for b in self.values_b:
                self.calculadoras.append(CalculadoraCientifica(a, b))

    def test_calcular_exponencial(self):
        for c in self.calculadoras:
            c.calcular_exponencial()
            self.assertEquals(c.get_exponencial(), c.a ** c.b)
            
    def test_calcular_logaritmo(self):
        for c in self.calculadoras:
            c.calcular_logaritmo()
            self.assertEquals(c.get_logaritmo(), log(c.a, c.b))
            
if __name__ == '__main__':
    unittest.main()
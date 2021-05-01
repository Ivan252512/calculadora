import math

class Calculadora():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.suma = 0
        self.resta = 0
        self.multiplicacion = 0
        self.division = 0
        
    def sumar(self):
        self.suma = self.a + self.b
    
    def restar(self):
        self.resta = self.a - self.b
    
    def multiplicar(self):
        self.multiplicacion = self.a * self.b
    
    def dividir(self):
        self.division = self.a / self.b
    
    def get_a(self):
        print(self.a)
    
    def get_b(self):
        print(self.b)
    
    def get_suma(self):
        return self.suma
    
    def get_resta(self):
        return self.resta
    
    def get_multiplicacion(self):
        return self.multiplicacion
    
    def get_division(self):
        return self.division
    
class CalculadoraCientifica(Calculadora):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.exponencial = 0
        self.logaritmo = 0
        self.raiz_cuadrada = 0
        
    def calcular_exponencial(self):
        self.exponencial = self.a ** self.b
    
    def calcular_logaritmo(self):
        self.logaritmo = math.log(self.b, self.a)

    def get_exponencial(self):
        return self.exponencial
    
    def get_logaritmo(self):
        return self.logaritmo
    

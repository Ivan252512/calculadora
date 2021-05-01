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
        self.resta
    
    def get_multiplicacion(self):
        pass
    
    def get_division(self):
        pass
    
class CalculadoraCientifica(Calculadora):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.exponencial = 0
        self.logaritmo = 0
        self.raiz_cuadrada = 0
        
    def calcular_exponencial(self):
        pass
    
    def calcular_logaritmo(self):
        pass

    def get_exponencial(self):
        pass
    
    def get_logaritmo(self):
        pass
    

import math

#Ponto
class Ponto():
    def __init__(self, x, y):
        self._x = x 
        self._y = y
        
    def __str__(self):
        return f'{self._x}, {self._y}'
    
    def getP(self):
        return self.__str__
    
    def coordenada(self):
        return [self._x, self._y]
    
    def origem(self):
        return math.sqrt(self._x**2 + self._y**2);
    
    def mudar_ponto(self, novoX, novoY):
        self._x = novoX
        self._y = novoY
       
    def ddp(self, p1, p2):
        return math.sqrt((p1.coordenada[0]-p2.coordenada[0])**2 + (p1.coordenada[0]-p2.coordenada[1])**2);

       
#Triangulo
class Triangulo(Ponto):
    def __init__(self, p1, p2, p3):
        self.p1 = Ponto(p1[0], p1[1])
        self.p2 = Ponto(p2[0], p2[1])
        self.p3 = Ponto(p3[0], p3[1])
    
    def lados(self):
        return [self.ddp(self.p1, self.p2), 
                self.ddp(self.p2, self.p3), 
                self.ddp(self.p1, self.p3)]
    
    def __str__(self):
        return f'Ponto 1: ({self.p1.getP()}) | Ponto 2: ({self.p2.getP()}) | Ponto 3: ({self.p3.getP()})'

    def coordenada(self):
        return [self.p1.coordenada, 
                self.p2.coordenada, 
                self.p3.coordenada]

    # Heron
    def area(self):
        lado = self.lados();
        p = (lado[0]+lado[1]+lado[2])/2
        area = math.sqrt(p*(p-lado[0])*(p-lado[1])*(p-lado[2]))
        return area
        

#Quadrado
class Quadrado(Ponto):
    def __init__(self, p1, p2, p3, p4):
        #p1 e p2 = base
        #p1 e p3 = altura
        self.p1 = Ponto(p1[0], p1[1])
        self.p2 = Ponto(p2[0], p2[1])
        self.p3 = Ponto(p3[0], p3[1])
        self.p4 = Ponto(p4[0], p4[1])
        
    def __str__(self):
        return f'Ponto 1: ({self.p1.getP()}) | Ponto 2: ({self.p2.getP()}) | Ponto 3: ({self.p3.getP()} | Ponto 4: ({self.p4.getP()})'
    
    def coordenada(self):
        return [self.p1.coordenada, 
                self.p2.coordenada,
                self.p3.coordenada, 
                self.p4.coordenada]
    
    def lados(self):
        return [self.ddp(self.p1, self.p2), self.ddp(self.p1, self.p3)]
    
    def area(self):
        return self.lados()[0]*self.lados()[1]

#Circulo
class Circulo(Ponto):
    def __init__(self, p, raio):
        self.p = Ponto(p[0], p[1])
        self.raio = raio
        
    def __str__(self):
        return f'Meio: ({self.p.getP()}) | Raio: {self.raio}'
    
    def coordenada(self):
        return [self.p.coordenada, self.raio]
        
    def ponto_esta_no_ciculo(self, local):
        if len(local) > 2:
            for ponto in local:
                ponto_coordenadas = ponto.coordenada()
                if math.sqrt((ponto_coordenadas[0] - self.p.coordenada()[0])**2 + (ponto_coordenadas[1] - self.p.coordenada()[1])**2) < self.raio:
                    return True
        else:
            if math.sqrt((local[0] - self.p.coordenada()[0])**2 + (local[1] - self.p.coordenada()[1])**2) < self.raio:
                    return True
            return False
    
    def area(self):
        return (math.pi**2)*self.raio
# Reta
class Reta(Ponto):
    def __init__(self, p1, p2):
        self.p1 = Ponto(p1[0], p1[1])
        self.p2 = Ponto(p2[0], p2[1])
    
    def __str__(self):
        return f'Ponto 1: ({self.p1.getP()}) | Ponto 2: ({self.p2.getP()})'

    def coordenada(self):
        return [self.p1.coordenada, self.p2.coordenada]
    
    def tamanho(self):
        return self.ddp(self.p1, self.p2);

if __name__ == '__main__':

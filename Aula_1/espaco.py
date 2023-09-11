from math import sqrt
#Ponto
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def coordenadaFormated(self):
        return f'{self.x}, {self.y}'
    
    def coordenada(self):
        return [self.x, self.y]
    
#Triangulo
class Triangulo():
    def __init__(self, p1, p2, p3):
        self.p1 = Ponto(p1[0], p1[1])
        self.p2 = Ponto(p2[0], p2[1])
        self.p3 = Ponto(p3[0], p3[1])
    
    def coordenadaFormated(self):
        return f'Ponto 1: ({self.p1.coordenadaFormated()}) | Ponto 2: ({self.p2.coordenadaFormated()}) | Ponto 3: ({self.p3.coordenadaFormated()})'

    def coordenada(self):
        return [self.p1.coordenada, self.p2.coordenada, self.p3.coordenada]

#Quadrado
class Quadrado():
    def __init__(self, p1, p2, p3, p4):
        self.p1 = Ponto(p1[0], p1[1])
        self.p2 = Ponto(p2[0], p2[1])
        self.p3 = Ponto(p3[0], p3[1])
        self.p4 = Ponto(p4[0], p4[1])
        
    def coordenadaFormated(self):
        return f'Ponto 1: ({self.p1.coordenadaFormated()}) | Ponto 2: ({self.p2.coordenadaFormated()}) | Ponto 3: ({self.p3.coordenadaFormated()} | Ponto 4: ({self.p4.coordenadaFormated()})'
    
    def coordenada(self):
        return [self.p1.coordenada, self.p2.coordenada, self.p3.coordenada, self.p4.coordenada]

#Circulo
class Circulo():
    def __init__(self, p, raio):
        self.p = Ponto(p[0], p[1])
        self.raio = raio
        
    def coordenadaFormated(self):
        return f'Meio: ({self.p.coordenadaFormated()}) | Raio: {self.raio}'
    
    def coordenada(self):
        return [self.p.coordenada, self.raio]
        
    def esta_no_ciculo(self, local):
        if len(local) > 2:
            for ponto in local:
                ponto_coordenadas = ponto.coordenada()
                if sqrt((ponto_coordenadas[0] - self.p.coordenada()[0])**2 + (ponto_coordenadas[1] - self.p.coordenada()[1])**2) < self.raio:
                    return True
        else:
            if sqrt((local[0] - self.p.coordenada()[0])**2 + (local[1] - self.p.coordenada()[1])**2) < self.raio:
                    return True
            return False
    
# Reta
class Reta():
    def __init__(self, p1, p2):
        self.p1 = Ponto(p1[0], p1[1])
        self.p2 = Ponto(p2[0], p2[1])
    
    def coordenadaFormated(self):
        return f'Ponto 1: ({self.p1.coordenadaFormated()}) | Ponto 2: ({self.p2.coordenadaFormated()})'

    def coordenada(self):
        return [self.p1.coordenada, self.p2.coordenada]
    

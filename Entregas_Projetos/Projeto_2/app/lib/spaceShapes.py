import math
import random
import string

def generateKey():
    characters = string.ascii_letters + string.digits
    random_key = ''.join(random.choice(characters) for _ in range(8))
    return random_key


#Ponto
class Ponto():
    def __init__(self, x, y) -> None:
        self._x = x 
        self._y = y
        self.__key = generateKey()
        
    def __str__(self) -> str:
        return f'{self._x}, {self._y}'
    
    def getKey(self) -> str:
        return f'{self.__key}'
    
    def getP(self) -> str:
        return self.__str__
    
    def getType(self) -> str:
        return 'Ponto'
    
    def getPosition(self) -> str:
        return f'({self._x}, {self._y})'
    
    def coordenada(self) -> list:
        return [self._x, self._y]
    
    # Distancia da origem ate o ponto
    def origem(self) -> float:
        return math.sqrt((self._x)**2 + (self._y)**2)
    
    def update(self, **kwargs):
        self._x = kwargs["x"]
        self._y = kwargs["y"]
    
    # Distancia entre dois pontos - ddp
    def ddp(self, p1, p2) -> float:
        return math.sqrt((p1.coordenada()[0]-p2.coordenada()[0])**2 + (p1.coordenada()[1]-p2.coordenada()[1])**2);
    

       
#Triangulo
class Triangulo(Ponto):
    def __init__(self, p1, p2, p3):
        self.p1 = Ponto(p1[0], p1[1])
        self.p2 = Ponto(p2[0], p2[1])
        self.p3 = Ponto(p3[0], p3[1])
        self.__key = generateKey()

    def getKey(self) -> str:
        return f'{self.__key}'
    
    def lados(self):
        return [
            self.ddp(self.p1, self.p2), 
            self.ddp(self.p1, self.p3),
            self.ddp(self.p2, self.p3)
        ]
    
    def getType(self) -> str:
        return 'Triangulo'
    
    def getPosition(self) -> str:
        return f'({self.p1.getP()()}),({self.p2.getP()()}),({self.p3.getP()()})'
    
    def __str__(self):
        return f'Ponto 1: ({self.p1.getP()()}) | Ponto 2: ({self.p2.getP()()}) | Ponto 3: ({self.p3.getP()()})'

    def coordenada(self):
        return [self.p1.coordenada(), 
                self.p2.coordenada(), 
                self.p3.coordenada()]

    # Heron
    def area(self):
        lado = self.lados();
        p = (lado[0]+lado[1]+lado[2])/2
        area = math.sqrt(p*(p-lado[0])*(p-lado[1])*(p-lado[2]))
        return area
    
    def update(self, **kwargs):
        self.p1.update(x=kwargs["p1"][0], y=kwargs["p1"][1])
        self.p2.update(x=kwargs["p2"][0], y=kwargs["p2"][1])
        self.p3.update(x=kwargs["p3"][0], y=kwargs["p3"][1])
        

#Quadrado
class Quadrado(Ponto):
    def __init__(self, p1, tamanho):
        # p1 = canto inferior direito
        # O quadrado expande para a direita e para cima do ponto p1 com lados tamanho 'tamanho'
        self.p1 = Ponto(p1[0], p1[1])
        self.p2 = Ponto(p1[0]+tamanho, p1[1])
        self.p3 = Ponto(p1[0], p1[1]+tamanho)
        self.p4 = Ponto(p1[0]+tamanho, p1[1]+tamanho)
        self.__key = generateKey()

    def getKey(self) -> str:
        return f'{self.__key}'
        
    def __str__(self):
        return f'Ponto 1: ({self.p1.getP()()}) | Ponto 2: ({self.p2.getP()()}) | Ponto 3: ({self.p3.getP()()} | Ponto 4: ({self.p4.getP()()})'
    
    def getType(self) -> str:
        return 'Quadrado'
    
    def getPosition(self) -> str:
        return f'({self.p1.getP()()}),({self.p2.getP()()}),({self.p3.getP()()}),({self.p4.getP()()})'

    def coordenada(self):
        return [self.p1.coordenada(), 
                self.p2.coordenada(),
                self.p3.coordenada(), 
                self.p4.coordenada()]
    
    def lados(self):
        return [self.ddp(self.p1, self.p2), self.ddp(self.p1, self.p3)]
    
    def area(self):
        return self.lados()[0]*self.lados()[1]
    
    def update(self, **kwargs):
        self.p1.update(x=kwargs["p"][0],                   
                       y=kwargs["p"][1]
        )
        self.p2.update(x=kwargs["p"][0]+kwargs["tamanho"], 
                       y=kwargs["p"][1]
        )
        self.p3.update(x=kwargs["p"][0],                   
                       y=kwargs["p"][1]+kwargs["tamanho"]
        )
        self.p4.update(x=kwargs["p"][0]+kwargs["tamanho"], 
                       y=kwargs["p"][1]+kwargs["tamanho"]
        )
        

#Circulo
class Circulo(Ponto):
    def __init__(self, p, raio):
        self.p = Ponto(p[0], p[1])
        self.raio = raio
        self.__key = generateKey()

    def getKey(self) -> str:
        return f'{self.__key}'
        
    def __str__(self):
        return f'Meio: ({self.p.getP()()}) | Raio: {self.raio}'
    
    def getType(self) -> str:
        return 'Circulo'
    
    def getPosition(self) -> str:
        return f'({self.p.getP()()})'

    def coordenada(self):
        return [self.p.coordenada, self.raio]
        
    # Ponto esta no circulo
    def pec(self, local):
        if len(local) > 2:
            for ponto in local:
                if math.sqrt((ponto[0] - self.p.coordenada()[0])**2 + (ponto[1] - self.p.coordenada()[1])**2) < self.raio:
                    return True
                return False
        else:
            if math.sqrt((local[0] - self.p.coordenada()[0])**2 + (local[1] - self.p.coordenada()[1])**2) < self.raio:
                    return True
            return False
    
    def area(self):
        return (math.pi**2)*self.raio
    
    def update(self, **kwargs):
        self.p.update(x=kwargs["p"][0], y=kwargs["p"][1])
        self.raio = kwargs["raio"]

# Reta
class Reta(Ponto):
    def __init__(self, p1, p2):
        self.p1 = Ponto(p1[0], p1[1])
        self.p2 = Ponto(p2[0], p2[1])
        self.__key = generateKey()

    def getKey(self) -> str:
        return f'{self.__key}'
    
    def __str__(self):
        return f'Ponto 1: ({self.p1.getP()()}) | Ponto 2: ({self.p2.getP()()})'

    def getType(self) -> str:
        return 'Reta'
    
    def getPosition(self) -> str:
        return f'({self.p1.getP()()}),({self.p1.getP()()})'

    def coordenada(self):
        return [self.p1.coordenada(), self.p2.coordenada()]
    
    def tamanho(self):
        return self.ddp(self.p1, self.p2)
    
    def update(self, **kwargs):
        self.p1.update(x=kwargs["p1"][0], y=kwargs["p1"][1])
        self.p2.update(x=kwargs["p2"][0], y=kwargs["p2"][1])

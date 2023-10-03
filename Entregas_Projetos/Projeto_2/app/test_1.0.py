from lib.spaceShapes import *
from lib.cartesianBoard import *

def workspace():
    p1 = Ponto(0, 0)
    print(p1.getKey())
    
    t1 = Triangulo([1, 7], [9,2],[5,5])
    print(t1)

    c1 = Circulo([2, 0], 10)
    print('key circulo: ' + c1.getKey())

    espaco = CartesianBoard()
    print('Adicionando ponto ao meu espaco')
    espaco.addShape(p1)
    print('Adicionando triangulo ao meu espaco')
    espaco.addShape(t1)
    print('Adicionando circulo ao meu espaco')
    espaco.addShape(c1)

    espaco.getShapesCLI()

    print('Removendo triangulo')
    espaco.delShape(t1.getKey())

    espaco.getShapesCLI()

    print(espaco.getShape(p1))
    
    espaco.updateShape(p1.getKey(), x=1, y=2)
    
    print(espaco.getShape(p1))





if __name__ == "__main__":
    workspace()
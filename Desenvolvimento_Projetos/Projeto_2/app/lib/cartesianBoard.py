from lib.spaceShapes import *

class CartesianBoard():
    def __init__(self) -> None:
        self.shapes = {}

    def addShape(self, newShape) -> None:
        if newShape.getType() != 'Circulo':
            self.shapes[newShape.getKey()] = {"type" : newShape.getType(), "cord" : newShape.getPosition()}
        else:
            self.shapes[newShape.getKey()] = {"type" : newShape.getType(), "cord" : newShape.getPosition(), "raio": newShape.raio}

    def delShape(self, shape_key : str) -> None:
        self.shapes.pop(shape_key)

    def getShape(self, shape) -> str:
        return {shape.getKey() : {"type" : shape.getType(), "cord" : shape.getPosition()}}
    
    def getShapesCLI(self):
        print("\n=-=-=-=-=-Shapes-=-=-=-=-=")
        print("Tipo - Chave : Cordenadas\n")
        for key, value in self.shapes.items():
            print(f'{key} : {value}')

    def getShapes(self):
        return [{key: value} for key, value in self.shapes.items()]

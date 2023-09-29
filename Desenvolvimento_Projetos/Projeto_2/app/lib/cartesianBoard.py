from lib.spaceShapes import *

class CartesianBoard():
    def __init__(self) -> None:
        self.shapes = {}

    def addShape(self, newShape) -> None:
        self.shapes[newShape.getKey()] = {"type" : newShape.getType(), "cord" : newShape.getPosition()}

    def delShape(self, shape) -> None:
        self.shapes.pop(shape.getKey())

    def getShape(self, shape) -> str:
        return {shape.getKey() : {"type" : shape.getType(), "cord" : shape.getPosition()}}
    
    def getShapesCLI(self):
        print("\n=-=-=-=-=-Shapes-=-=-=-=-=")
        print("Tipo - Chave : Cordenadas\n")
        for key, value in self.shapes.items():
            print(f'{key} : {value}')

    def getShapes(self):
        return {{key: value} for key, value in self.shapes.items()}

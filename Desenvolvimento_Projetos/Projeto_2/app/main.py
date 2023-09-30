from fastapi import FastAPI, HTTPException
from typing import Dict
from lib.spaceShapes import *
from lib.cartesianBoard import CartesianBoard

app =  FastAPI()

space = CartesianBoard()

# Start some shapes
p1 = Ponto(102, 78)
p2 = Ponto(90, 66)
t = Triangulo([26, 0],[53, 53], [26, 10])
c = Circulo([0,0], 150)
space.addShape(p1)
space.addShape(p2)
space.addShape(t)
space.addShape(c)


@app.get('/')
def root():
    return {'Projeto 2' : 'API Quadro Cartesiano'}

# CREATE
@app.post('/shapes/add/{shape_type}')
async def add_shape(shape_type : str, shape_data: Dict):
    if shape_type == 'Ponto':
        shape = Ponto(
            shape_data['x'], shape_data['y']
        )
    elif shape_type == 'Triangulo':
        shape = Triangulo(
            shape_data['p1'], shape_data['p2'], shape_data['p3']
        )
    elif shape_type == 'Quadrado':
        shape = Quadrado(
            shape_data['p1'], shape_data['tamanho']
        )
    elif shape_type == 'Circulo':
        shape = Circulo(
            shape_data['p'], shape_data['raio']
        )
    elif shape_type == 'Reta':
        shape = Reta(
            shape_data['p1'], shape_data['p2']
        )
    else:
        raise HTTPException(
            status_code=400, 
            detail="Tipo de forma desconhecido"
        )
    
    space.addShape(shape)

    return space.getShape(shape)

# READ
@app.get('/shapes/')
async def get_all():
    return space.getShapes()
# UPDATE

# DELETE
@app.delete('/shapes/del/{shape_key}')
async def del_shape(shape_key : str):
    space.delShape(shape_key)
    if not (shape_key in space.getShapes()):
        return {"Shape removido"}
    return {"Erro ao remover o shape"}

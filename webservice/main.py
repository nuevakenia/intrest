import json
from uuid import uuid4
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas import CreateRecetaRequest
import requests

app = FastAPI()

recetas = []
farmacos = [{"paracetamol600": 5},{"ketoprofeno300": 5},{"ibuprofeno600": 0}]

#recibir recetas y guardarlas.
@app.post("/receta/recibir/")
async def recibir_receta(receta: CreateRecetaRequest):
    recetas.append(receta.dict())
    print(recetas.farmacos)
    stock = consultar_stock(receta.farmacos)
    jsonizado = jsonable_encoder(receta)

    return jsonizado

async def consultar_stock(farmacos: CreateRecetaRequest):
    for farmaco in farmacos:
        for nombre, stock in farmaco:
            print("farmaco: " ,"")
    return

@app.post("/receta/recibir/")
async def recibir_receta(receta: CreateRecetaRequest):
    recetas.append(receta.dict())
    print(recetas)
    jsonizado = jsonable_encoder(receta)

    return jsonizado
    #Conexion
    #get_test_url = f"http://127.0.0.1:8001/receta/post/{id}/"
    #post = await requests.post(get_test_url,json=jsonizado)
    
    return json(JSONResponse(content=jsonizado))



# GET api solicitar remedios centros -> farmacia.

# POST api solicitar remedios centros <- farmacia.

#

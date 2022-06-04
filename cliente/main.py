from datetime import datetime
from uuid import uuid4
from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from typing import List
from requests import Session
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import requests

from schemas import CreateRecetaRequest, CreatePacienteRequest, CreateCarnetRequest


app = FastAPI()

pacientes = []
carnets = []




# GET api solicitar remedios centros -> farmacia.

# POST api solicitar remedios centros <- farmacia.
@app.post("/receta/post/")
async def enviar_receta(receta: CreateRecetaRequest):
    receta.id = str(uuid4())
    receta.carnet = str(uuid4())
    #receta.fecha = datetime.now()
    """ receta.medico = str
    receta.nombre_paciente = str
    receta.telefono_paciente = str
    receta.fecha = datetime.utcnow()
    receta.preescripcion = str
    receta.farmacos = List[str] """
    jsonizado = jsonable_encoder(receta)
    #Conexion
    get_test_url = f"http://127.0.0.1:8001/receta/recibir/"
    post = requests.post(get_test_url,json=jsonizado)
    print("type: ",type(post))
    print("POST: ",post)
    return post.json()
#

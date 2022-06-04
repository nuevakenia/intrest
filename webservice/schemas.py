from ast import List
from uuid import uuid4
from pydantic import BaseModel
from datetime import datetime

class CreateFarmacoRequest(BaseModel):
    nombre_farmaco: str
    stock: int

class CreatePacienteRequest(BaseModel):
    id: str
    rut: str
    nombre_completo: str
    Doctor: str

class CreateCarnetRequest(BaseModel):
    id: str
    rut_paciente: str
    receta: str
    fecha: str
    estado: bool

class CreateRecetaRequest(BaseModel):
    id: str
    carnet: str
    medico : str
    nombre_paciente: str
    telefono_paciente: str
    fecha: str
    prescripcion: str
    farmacos: list[dict[str,int]]



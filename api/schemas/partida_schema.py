from pydantic import BaseModel
from typing import Optional, List
from model.partida import Partida
import json
import numpy as np


class PartidaSchema(BaseModel):
    """Define como uma nova partida a ser simulada deve ser representada
    """
    sigla_casa: str
    sigla_fora: str


class PartidaViewSchema(BaseModel):
    """Define como uma partida será retornada
    """
    id: int
    nome_time_casa: str
    nome_time_fora: str
    cgc: int
    cgf: int
    ec: int
    ef: int
    vencedor: int


class PartidaBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca por uma partida.
    A busca é feita com base nas siglas dos times.
    """
    sigla_casa: str
    sigla_fora: str


class ListaPartidasSchema(BaseModel):
    """Define como uma lista de partidas será representada
    """
    partidas: List[PartidaViewSchema]

# Apresenta apenas os dados de um paciente    
def apresenta_partida(partida: Partida):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": partida.id,
        "sigla_casa": partida.nome_time_casa,
        "sigla_fora": partida.nome_time_fora,
        "cgc": partida.cgc,
        "cgf": partida.cgf,
        "ec": partida.ec,
        "ef": partida.ef,
        "vencedor": partida.vencedor,
    }
    
# # Apresenta uma lista de pacientes
# def apresenta_pacientes(pacientes: List[Paciente]):
#     """ Retorna uma representação do paciente seguindo o schema definido em
#         PacienteViewSchema.
#     """
#     result = []
#     for paciente in pacientes:
#         result.append({
#             "id": paciente.id,
#             "name": paciente.name,
#             "preg": paciente.preg,
#             "plas": paciente.plas,
#             "pres": paciente.pres,    
#             "skin": paciente.skin,
#             "test": paciente.test,
#             "mass": paciente.mass,
#             "pedi": paciente.pedi,
#             "age": paciente.age,
#             "outcome": paciente.outcome
#         })

#     return {"pacientes": result}


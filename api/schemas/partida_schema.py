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

# Apresenta apenas os dados de um partida    
def apresenta_partida(partida: Partida):
    """ Retorna uma representação do partida seguindo o schema definido em
        PartidaViewSchema.
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



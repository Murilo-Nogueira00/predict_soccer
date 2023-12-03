from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base

class Partida(Base):
    __tablename__ = 'partida'

    id = Column(Integer, primary_key=True)
    nome_time_casa = Column("CASA", String(50))
    cod_time_casa = Column("TIME_CASA", Integer)
    nome_time_fora = Column("FORA", String(50))
    cod_time_fora = Column("TIME_FORA", Integer)
    cgc = Column("CHUTES_NO_GOL_TIME_CASA", Integer)
    cgf = Column("CHUTES_NO_GOL_TIME_FORA", Integer)
    ec = Column("JOGADORES_EXPULSOS_TIME_CASA", Integer)
    ef = Column("JOGADORES_EXPULSOS_TIME_FORA", Integer)
    vencedor = Column("VENCEDOR", Integer)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome_time_casa: str, cod_time_casa: int, nome_time_fora: str,
                 cod_time_fora: int, cgc: int, cgf: int, ec: int,
                 ef: int, vencedor: int,
                 data_insercao: Union[DateTime, None] = None):
        """
        Cria uma partida

        Arguments:
            nome_time_casa: nome do time da casa
            cod_time_casa: código do time da casa
            nome_time_fora: nome do time visitante
            cod_time_fora: código do time visitante
            cgc: chutes no gol feitos pelo time da casa
            cgf: chutes no gol feitos pelo time visitante
            ec: jogadores expulsos do time da casa
            ef: jogadores expulsos do time visitante
            vencedor: time vencedor da partida
            data_insercao: data de quando o paciente foi inserido à base
        """
        self.nome_time_casa = nome_time_casa
        self.cod_time_casa = cod_time_casa
        self.nome_time_fora = nome_time_fora
        self.cod_time_fora = cod_time_fora
        self.cgc = cgc
        self.cgf = cgf
        self.ec = ec
        self.ef = ef
        self.vencedor = vencedor

        # se não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

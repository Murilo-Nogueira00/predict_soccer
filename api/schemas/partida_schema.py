from pydantic import BaseModel


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

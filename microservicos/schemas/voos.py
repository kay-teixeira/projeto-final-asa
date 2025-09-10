from pydantic import BaseModel
from datetime import date, time
from decimal import Decimal 


class VooSchema(BaseModel):
    id: int
    aeroporto_origem_id: int
    aeroporto_destino_id: int
    data_partida: date
    hora_partida: time
    data_chegada: date
    hora_chegada: time
    companhia_aerea: str
    preco: Decimal
    assentos_disponíveis: int

    class Config:
        from_attributes = True

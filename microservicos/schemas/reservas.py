from pydantic import BaseModel
from datetime import datetime

class ReservaCreate(BaseModel):
    voo_id: int
    numero_passageiros: int

class ReservaOut(BaseModel):
    usuario_id: int
    voo_id: int
    numero_passageiros: int
    data_reserva: datetime
    localizador: str
    numero_etickets: str
    preco_total: float

    class Config:
        from_attributes = True
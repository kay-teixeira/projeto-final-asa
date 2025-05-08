from pydantic import BaseModel
from datetime import datetime

class ReservaCreate(BaseModel):
    usuario_id: int
    voo_id: int
    numero_passageiros: int

class ReservaOut(ReservaCreate):
    id: int
    data_reserva: datetime
    localizador: str
    numero_etickets: str
    preco_total: float

    class Config:
        orm_mode = True
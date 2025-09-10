from pydantic import BaseModel


class AeroportoSchema(BaseModel):
    id: int
    codigo: str
    nome: str
    cidade: str
    pais: str

    class Config:
        from_attributes = True
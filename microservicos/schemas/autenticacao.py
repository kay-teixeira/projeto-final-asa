from pydantic import BaseModel
from datetime import datetime

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str

class LoginRequest(BaseModel):
    email: str
    senha: str

class SessaoResponse(BaseModel):
    chave_sessao: str
    data_expiracao: datetime

class UsuarioOut(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True
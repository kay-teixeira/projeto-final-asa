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
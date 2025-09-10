from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from microservicos.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)

class Sessao(Base):
    __tablename__ = "sessoes"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    chave_sessao = Column(String(255), unique=True, nullable=False)
    data_expiracao = Column(TIMESTAMP, nullable=False)
    ip_address = Column(String(50))
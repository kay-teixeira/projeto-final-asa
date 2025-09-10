from sqlalchemy import Column, Integer, String
from microservicos.database import Base

class Aeroporto(Base):
    __tablename__ = "aeroportos"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(3), nullable=False)
    nome = Column(String(100), nullable=False)
    cidade = Column(String(50), nullable=False)
    pais = Column(String(50), nullable=False)

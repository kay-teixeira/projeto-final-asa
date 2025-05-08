from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from microservicos.database import Base
from datetime import datetime

class Reserva(Base):
    __tablename__ = "reservas"
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    voo_id = Column(Integer, ForeignKey("voos.id"), nullable=False)
    data_reserva = Column(DateTime, default=datetime.utcnow)
    localizador = Column(String(255), unique=True, nullable=False)
    numero_etickets = Column(String(255), nullable=False)
    preco_total = Column(Numeric(10, 2), nullable=False)
    numero_passageiros = Column(Integer, nullable=False)
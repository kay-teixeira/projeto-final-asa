from sqlalchemy import Column, Integer, String, ForeignKey, Time, Numeric, Date
from microservicos.database import Base

class Voo(Base):
    __tablename__ = "voos"
    id = Column(Integer, primary_key=True, index=True)
    aeroporto_origem_id = Column(Integer, ForeignKey("aeroportos.id"))
    aeroporto_destino_id = Column(Integer, ForeignKey("aeroportos.id"))
    data_partida = Column(Date)
    hora_partida = Column(Time)
    data_chegada = Column(Date)
    hora_chegada = Column(Time)
    companhia_aerea = Column(String(100))
    preco = Column(Numeric(10, 2))
    assentos_disponíveis = Column(Integer)


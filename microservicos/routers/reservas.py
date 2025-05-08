from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from microservicos.schemas.reservas import ReservaCreate, ReservaOut
from microservicos.models.voos import Voo as VooModel
from microservicos.database import get_db
from microservicos.models.reservas import Reserva as ReservaModel
from datetime import datetime
import logging
import colorlog
import uuid
from sqlalchemy import select

router = APIRouter(prefix = "/Reservas", tags=["Reservas"])


def gerar_localizador():
    return str(uuid.uuid4())[:8].upper()

def gerar_eticket():
    return "ET-" + str(uuid.uuid4())[:10].replace("-", "").upper()

# Logger configurado
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter("%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger = colorlog.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

@router.post("/", response_model=ReservaOut)
def criar_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    logger.info("Criando reserva para o usuário ID: %s", reserva.usuario_id)
    voo = db.execute(
        select(VooModel).where(VooModel.id == reserva.voo_id)
    ).scalar_one_or_none()

    if not voo:
        logger.info("Voo não encontrado.")
        raise HTTPException(status_code=404, detail="Voo não encontrado")

    if voo.assentos_disponíveis < reserva.numero_passageiros:
        logger.info("Assentos insuficientes.")
        raise HTTPException(status_code=400, detail="Assentos insuficientes")

    preco_total = float(voo.preco) * reserva.numero_passageiros

    nova_reserva = ReservaModel(
        usuario_id=reserva.usuario_id,
        voo_id=reserva.voo_id,
        data_reserva=datetime.utcnow(),
        localizador=gerar_localizador(),
        numero_etickets=gerar_eticket(),
        preco_total=preco_total,
        numero_passageiros=reserva.numero_passageiros
    )

# Atualiza os assentos disponíveis
    voo.assentos_disponíveis -= reserva.numero_passageiros

    logger.info("Reserva criada com sucesso. Localizador: %s", nova_reserva.localizador)
    db.add(nova_reserva)
    db.commit()
    db.refresh(nova_reserva)

    return nova_reserva

@router.get("/", response_model=list[ReservaOut])
def listar_reservas_usuario(usuario_id: int, db: Session = Depends(get_db)):
    logger.info("Listando reservas para o usuário ID: %s", usuario_id)
    return db.query(ReservaModel).filter_by(usuario_id=usuario_id).all()


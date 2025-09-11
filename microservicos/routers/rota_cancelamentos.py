from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from microservicos.database import get_db
from microservicos.models.reservas import Reserva as ReservaModel
import logging
import colorlog

router = APIRouter(prefix = "/cancelamentos",tags=["Cancelamentos"])

# Logger configurado
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter("%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger = colorlog.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

@router.delete("/")
def cancelar_reserva(localizador: str, db: Session = Depends(get_db)):
    logger.info("Cancelando reserva com localizador: %s", localizador)
    reserva = db.query(ReservaModel).filter_by(localizador=localizador).first()
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")

    db.delete(reserva)
    db.commit()
    return {"mensagem": "Reserva cancelada com sucesso"}
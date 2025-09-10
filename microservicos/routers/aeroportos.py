from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from microservicos.schemas.aeroportos import AeroportoSchema
from microservicos.database import get_db
from microservicos.models.aeroportos import Aeroporto as AeroportoModel
import logging
import colorlog

router = APIRouter(prefix="/Aeroportos", tags=["Aeroportos"])


# Logger configurado
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter("%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger = colorlog.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)


@router.get("/listar aeroporto", response_model=list[AeroportoSchema])
def listar_aeroportos(db: Session = Depends(get_db)):
    logger.info("Listando todos os aeroportos.")
    return db.query(AeroportoModel).all()

@router.get("/ buscar por código", response_model=AeroportoSchema)
def buscar_por_codigo(codigo: str, db: Session = Depends(get_db)):
    logger.info("Buscando aeroporto pelo código: %s", codigo)
    aeroporto = db.query(AeroportoModel).filter_by(codigo=codigo.upper()).first()
    if not aeroporto:
        raise HTTPException(status_code=404, detail="Aeroporto não encontrado.")
        logger.info("Aeroporto não encontrado.")
    return aeroporto
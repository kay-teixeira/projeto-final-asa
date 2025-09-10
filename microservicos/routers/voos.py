from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date
from microservicos.schemas.voos import VooSchema
from microservicos.database import get_db
from microservicos.models.voos import Voo 
import logging
import colorlog

router = APIRouter()
router = APIRouter(prefix = "/Voos", tags=["Voos"])

handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"
))
logger = colorlog.getLogger(__name__)
logger.setLevel(logging.DEBUG)
if not logger.hasHandlers():
    logger.addHandler(handler)

@router.get("/", response_model=list[VooSchema])
def listar_voos(
    origem: int = Query(None),
    destino: int = Query(None),
    data: date = Query(None),
    db: Session = Depends(get_db)
):
    logger.info("Consultando voos com filtros: origem=%s, destino=%s, data=%s", origem, destino, data)
    query = db.query(Voo)
    if origem:
        query = query.filter(Voo.aeroporto_origem_id == origem)
    if destino:
        query = query.filter(Voo.aeroporto_destino_id == destino)
    if data:
        query = query.filter(Voo.data_partida == data)
    resultados = query.all()
    logger.debug("Voos encontrados: %d", len(resultados))
    return resultados
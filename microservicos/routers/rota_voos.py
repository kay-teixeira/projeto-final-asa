from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date
from microservicos.schemas.voos import VooSchema
from microservicos.database import get_db
from microservicos.models.voos import Voo 
import logging
import colorlog
from microservicos.models.voos import Voo as VooModel
from microservicos.models.aeroportos import Aeroporto as AeroportoModel 

router = APIRouter()
router = APIRouter(prefix = "/voos", tags=["Voos"])

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
    db: Session = Depends(get_db),
    origem: str | None = None, 
    destino: str | None = None,
    data_partida: date | None = None
):
    logger.info(f"Buscando voos com origem: {origem}, destino: {destino}")

    query = db.query(VooModel)

    if origem:
        aeroporto_origem_obj = db.query(AeroportoModel).filter(AeroportoModel.codigo == origem.upper()).first()
        if aeroporto_origem_obj:
            query = query.filter(VooModel.aeroporto_origem_id == aeroporto_origem_obj.id)
        else:
            return []

    if destino:
        aeroporto_destino_obj = db.query(AeroportoModel).filter(AeroportoModel.codigo == destino.upper()).first()
        if aeroporto_destino_obj:
            query = query.filter(VooModel.aeroporto_destino_id == aeroporto_destino_obj.id)
        else:
            return []
    
    if data_partida:
        query = query.filter(VooModel.data_partida == data_partida)

    voos_encontrados = query.all()
    logger.info(f"Encontrados {len(voos_encontrados)} voos.")
    return voos_encontrados
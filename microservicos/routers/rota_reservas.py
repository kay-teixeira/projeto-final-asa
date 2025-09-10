from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from microservicos.schemas.reservas import ReservaCreate, ReservaOut
from microservicos.models.voos import Voo as VooModel
from microservicos.models.reservas import Reserva as ReservaModel
from microservicos.models.autenticacao import Usuario as UsuarioModel, Sessao as SessaoModel # Importar modelos de autenticação
from microservicos.database import get_db
from datetime import datetime
import uuid
import logging
import colorlog

router = APIRouter(prefix="/reservas", tags=["Reservas"])
security = HTTPBearer()

# Função de dependência para obter o usuário atual a partir do token
def get_current_user(token: HTTPAuthorizationCredentials = Security(security), db: Session = Depends(get_db)):
    chave_sessao = token.credentials
    sessao = db.query(SessaoModel).filter_by(chave_sessao=chave_sessao).first()
    if not sessao or sessao.data_expiracao < datetime.utcnow():
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    
    usuario = db.query(UsuarioModel).filter_by(id=sessao.usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return usuario

# Funções para gerar localizador e eticket 
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
def criar_reserva(reserva: ReservaCreate, db: Session = Depends(get_db), current_user: UsuarioModel = Depends(get_current_user)):
    logger.info("Criando reserva para o usuário ID: %s", current_user.id)
    
    voo = db.query(VooModel).filter(VooModel.id == reserva.voo_id).first()

    if not voo:
        raise HTTPException(status_code=404, detail="Voo não encontrado")

    if voo.assentos_disponíveis < reserva.numero_passageiros:
        raise HTTPException(status_code=400, detail="Assentos insuficientes")

    preco_total = float(voo.preco) * reserva.numero_passageiros

    nova_reserva = ReservaModel(
        usuario_id=current_user.id,
        voo_id=reserva.voo_id,
        data_reserva=datetime.utcnow(),
        localizador=gerar_localizador(),
        numero_etickets=gerar_eticket(),
        preco_total=preco_total,
        numero_passageiros=reserva.numero_passageiros
    )

    voo.assentos_disponíveis -= reserva.numero_passageiros
    
    db.add(nova_reserva)
    db.commit()
    db.refresh(nova_reserva)
    
    logger.info("Reserva criada com sucesso. Localizador: %s", nova_reserva.localizador)
    return nova_reserva

@router.get("/", response_model=list[ReservaOut])
def listar_reservas_usuario(db: Session = Depends(get_db), current_user: UsuarioModel = Depends(get_current_user)):
    logger.info("Listando reservas para o usuário ID: %s", current_user.id)
    return db.query(ReservaModel).filter_by(usuario_id=current_user.id).all()
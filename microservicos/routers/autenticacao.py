from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from microservicos.schemas.autenticacao import UsuarioCreate, LoginRequest, SessaoResponse
from microservicos.models.autenticacao import Usuario as UsuarioModel, Sessao as SessaoModel
from microservicos.database import get_db
from passlib.context import CryptContext
from uuid import uuid4
from datetime import datetime, timedelta
import logging
import colorlog

router = APIRouter(prefix="/Autenticacao", tags=["Autenticação"])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Logger configurado
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter("%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logger = colorlog.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

@router.post("/registrar")
def registrar(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    if db.query(UsuarioModel).filter_by(email=usuario.email).first():
        raise HTTPException(status_code=400, detail="Email já registrado.")
    if db.query(UsuarioModel).filter_by(nome=usuario.nome).first():
        raise HTTPException(status_code=400, detail="Nome de usuário já existe.")
    hashed = pwd_context.hash(usuario.senha)
    novo_usuario = UsuarioModel(nome=usuario.nome, email=usuario.email, senha=hashed)
    logger.info(f"Novo usuário registrado: {usuario.email}")
    db.add(novo_usuario)
    db.commit()
    return {"mensagem": "Usuário registrado com sucesso."}


@router.post("/login", response_model=SessaoResponse)
def login(req: LoginRequest, request: Request, db: Session = Depends(get_db)):
    user = db.query(UsuarioModel).filter_by(email=req.email).first()
    if not user or not pwd_context.verify(req.senha, user.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")
    chave = str(uuid4())
    expira = datetime.utcnow() + timedelta(hours=1)
    nova_sessao = SessaoModel(usuario_id=user.id, chave_sessao=chave, data_expiracao=expira, ip_address=request.client.host)
    logger.info(f"Usuário {user.email} logado com sucesso.")
    db.add(nova_sessao)
    db.commit()
    return SessaoResponse(chave_sessao=chave, data_expiracao=expira)

@router.post("/logout")
def logout(chave_sessao: str, db: Session = Depends(get_db)):
    sessao = db.query(SessaoModel).filter_by(chave_sessao=chave_sessao).first()
    if sessao:
        logger.info(f"Usuário com chave de sessão {chave_sessao} deslogado.")
        db.delete(sessao)
        db.commit()
    return {"mensagem": "Logout realizado com sucesso."}

@router.get("/verificar")
def verificar(chave_sessao: str, db: Session = Depends(get_db)):
    logger.info("Verificando sessão.")
    sessao = db.query(SessaoModel).filter_by(chave_sessao=chave_sessao).first()
    if not sessao or sessao.data_expiracao < datetime.utcnow():
        logger.info("Sessão inválida ou expirada.")
        raise HTTPException(status_code=401, detail="Sessão inválida ou expirada.")
    return {"status": "sessão válida"}
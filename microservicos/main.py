from fastapi import FastAPI
from microservicos.routers import autenticacao, cancelamentos, reservas, voos, aeroportos
from microservicos.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(autenticacao.router)
app.include_router(cancelamentos.router)
app.include_router(reservas.router)
app.include_router(voos.router)
app.include_router(aeroportos.router)



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from microservicos.routers import rota_aeroportos, rota_autenticacao, rota_cancelamentos, rota_reservas, rota_voos
from microservicos.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost:5173", 
     "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       
    allow_credentials=True,      
    allow_methods=["*"],         
    allow_headers=["*"],         
)

app.include_router(rota_autenticacao.router)
app.include_router(rota_cancelamentos.router)
app.include_router(rota_reservas.router)
app.include_router(rota_voos.router)
app.include_router(rota_aeroportos.router)



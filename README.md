# Sistema de Vendas de Passagens Aéreas

Este é um sistema completo de venda de passagens aéreas desenvolvido utilizando a linguagem Python com **FastAPI**, banco de dados **PostgreSQL**, **Docker** e orquestração com **Kubernetes (Minikube)**.

## Tecnologias Utilizadas:

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker + Docker Compose
- Kubernetes (Minikube)
- PgAdmin 4
- Uvicorn
- Pydantic v2

## Estrutura dos Microserviços:

projeto-final-asa/
|---- Dockerfile
|---- docker-compose.yaml
|---- microservicos/
| |---- main.py
| |---- models/
| |---- routers/
| | |---- aeroportos.py
| | |---- autenticacao.py
| | |---- cancelamentos.py
| | |---- reservas.py
| | |---- voos.py
| |---- schemas/
| |---- database.py
|---- k8s/
| |---- app-deployment.yaml
| |---- app-service.yaml
| |---- postgres-deployment.yaml
| |---- postgres-service.yaml
|---|---- pgadmin.yaml

## Funcionalidades:

- **Autenticação**: login, logout e sessão
- **Cadastro e consulta de voos**
- **Compra de passagens** com geração de: localizador e E-ticket;
- **Cancelamento de Passagens**
- **Filtros de voos por origem, destino e data**

## Como executar com Docker Compose:

docker-compose up --build

=> Acesse a documentação da API: http://localhost:5000/docs

## Como executar com Minikube:

1. Inicie o Minikube:

minikube start --driver=docker

eval $(minikube docker-env)

2. Construa a imagem:

docker build -t minikube_projeto_final_app:latest .

3. Aplique os manifestos Kubernetes:

kubectl apply -f k8s/

4. Verifique se os pods estão rodando:

kubectl get pods

5. Quando todos estiverem como **Running**, acesse a API:

minikube service fastapi-service

## Requisitos:

- Docker e Docker Compose
- Minikube e Kubectl
- Python 3.13

## Autoria:

Desenvolvido por Kaylane Raquel como parte do projeto final da disciplina de Arquitetura de Software Aplicada - Universidade Federal de Uberlândia (UFU).

FROM python

RUN apt-get update && apt-get install python3-pip -y
WORKDIR /projeto_final
COPY microservicos/ ./microservicos/
RUN pip install --no-cache-dir -r microservicos/requirements.txt 
EXPOSE 5000
ENV PYTHONPATH=/projeto_final
CMD ["uvicorn", "microservicos.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload", "--app-dir", "/projeto_final"]




## dockerdile usando version de python alpine 
FROM python:3.9-alpine as builder
WORKDIR /app
# Instalacion de requerimientos actualmente vacios
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt
COPY . .
# multistaging
FROM python:3.9-alpine
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
# comando inicial al correr el contenedor
CMD ["python","microservice.py"]

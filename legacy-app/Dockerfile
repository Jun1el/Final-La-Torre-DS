## usamos version slim para reducir el tamaño de la imagen como pidio en el problema
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt
COPY . .
## multistaging
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
## comando inicial al correr el contenedor
CMD ["python", "legacy-app.py"]
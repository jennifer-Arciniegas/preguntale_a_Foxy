# Usa una imagen base con Python
FROM python:3.9-slim

# Configura el entorno
WORKDIR /app
COPY . .

# Instala dependencias
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    reflex init

# Expone el puerto 3000 (default de Reflex)
EXPOSE 3000

# Comando para producción
CMD reflex run --env prod --host 0.0.0.0

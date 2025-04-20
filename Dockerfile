FROM python:3.9-slim  

# 1. Instala Node.js 16.x (requerido para reflex 0.6)
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs=16.20.2-1nodesource1 gcc python3-dev

# 2. Configura el entorno
WORKDIR /app
COPY . .

# 3. Instala dependencias (sin actualizar npm a propósito)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 4. Puerto y comando de inicio
EXPOSE 3000
CMD ["sh", "-c", "reflex init && reflex run --env prod --host 0.0.0.0"]
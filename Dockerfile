FROM python:3.10-slim

# 1. Instala Node.js y dependencias del sistema
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs gcc python3-dev

# 2. Configura el entorno
WORKDIR /app
COPY . .

# 3. Instala dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    npm install -g npm@latest

# 4. Inicializa Reflex (esto se ejecutará al iniciar el contenedor)
EXPOSE 3000
CMD ["sh", "-c", "reflex init && reflex run --env prod --host 0.0.0.0"]
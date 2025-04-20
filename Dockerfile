FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs=16.20.2-1nodesource1 gcc python3-dev

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir --upgrade "pip<22.0" && \
    pip install --no-cache-dir --use-deprecated=legacy-resolver -r requirements.txt

EXPOSE 3000
CMD ["sh", "-c", "reflex init && reflex run --env prod --host 0.0.0.0"]
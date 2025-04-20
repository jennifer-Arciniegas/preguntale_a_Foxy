FROM python:3.11-slim  

RUN apt-get update && \
    apt-get install -y \
    curl \
    gcc \
    python3-dev \
    unzip \
    && rm -rf /var/lib/apt/lists/*


RUN curl -fsSL https://bun.sh/install | bash
ENV PATH="/root/.bun/bin:${PATH}"


WORKDIR /app
COPY . .


RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


EXPOSE 3000
CMD ["sh", "-c", "reflex init && reflex run --env prod --backend-host 0.0.0.0"]
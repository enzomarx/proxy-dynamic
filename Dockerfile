# Imagem base
FROM python:3.9-slim

# dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Cria um diretório para o app
WORKDIR /app

# Copia os arquivos necessários para o diretório 
COPY requirements.txt requirements.txt
COPY proxy_server.py proxy_server.py
COPY web_interface.py web_interface.py
COPY config.json config.json

RUN pip install --no-cache-dir -r requirements.txt

# portas para a comunicação
EXPOSE 8000
EXPOSE 5000

# Comando para iniciar 
CMD ["sh", "-c", "python proxy_server.py & python web_interface.py"]

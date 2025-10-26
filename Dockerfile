# Dockerfile para OpenVoice Server
FROM python:3.12-slim

# Configurar variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório de trabalho
WORKDIR /app

# Copiar arquivos de requirements
COPY requirements.txt .
COPY requirements_server.txt .

# Instalar dependências Python (servidor)
RUN pip install --upgrade pip && \
    pip install -r requirements_server.txt

# Copiar código do servidor
COPY openvoice_server ./openvoice_server
COPY openvoice ./openvoice

# Criar diretórios necessários
RUN mkdir -p outputs processed checkpoints logs

# Expor porta
EXPOSE 8000

# Comando padrão
CMD ["python", "-m", "uvicorn", "openvoice_server.main:app", "--host", "0.0.0.0", "--port", "8000"]


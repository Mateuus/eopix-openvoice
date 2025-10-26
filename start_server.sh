#!/bin/bash
# Script para iniciar o servidor OpenVoice

echo "🚀 Iniciando OpenVoice Server..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado!"
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"

# Criar diretórios necessários
mkdir -p outputs processed logs

# Verificar se os modelos existem
if [ ! -d "checkpoints" ]; then
    echo "⚠️  Diretório 'checkpoints' não encontrado"
    echo "📥 Os modelos serão baixados automaticamente na primeira execução"
fi

# Verificar se o venv existe
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
fi

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências
echo "📚 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements_server.txt

# Iniciar servidor
echo "🎯 Iniciando servidor na porta 8000..."
echo "📖 Documentação disponível em: http://localhost:8000/docs"
echo ""

python -m uvicorn openvoice_server.main:app --host 0.0.0.0 --port 8000 --reload


# eopix-openvoice

Repositório de clonagem de voz usando OpenVoice para o projeto eopix.

## 📦 Repositório

[GitHub: Mateuus/eopix-openvoice](https://github.com/Mateuus/eopix-openvoice)

## 🚀 Quick Start

```bash
# Clone o repositório
git clone https://github.com/Mateuus/eopix-openvoice.git
cd eopix-openvoice/openvoice-server

# Configure o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/WSL

# Instale as dependências
pip install -r requirements_server.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite .env e adicione OPENAI_API_KEY=sua_chave

# Execute os notebooks
jupyter notebook
```

## 📚 Documentação

- [README_SERVER_PT.md](README_SERVER_PT.md) - Documentação completa em português
- [README.md](README.md) - Documentação original do OpenVoice
- [docs/USAGE.md](docs/USAGE.md) - Guia de uso
- [docs/QA.md](docs/QA.md) - Perguntas frequentes

## 🎮 Notebooks Disponíveis

1. **demo_part1.ipynb** - Clonagem de voz com controle de estilo
2. **demo_part2.ipynb** - Clonagem cross-lingual com OpenAI TTS
3. **demo_part3.ipynb** - Demos adicionais

## ⚙️ Configuração

### Arquivos Ignorados pelo Git

- `checkpoints/` - Modelos treinados (arquivos grandes)
- `outputs/` - Arquivos de saída
- `processed/` - Arquivos processados
- `venv/` - Ambiente virtual
- `.env` - Configurações sensíveis
- `logs/` - Logs do sistema

### Checkpoints

Os checkpoints devem ser baixados separadamente e colocados em `checkpoints/`:
- `checkpoints/base_speakers/EN/` - Speaker em inglês
- `checkpoints/base_speakers/ZH/` - Speaker em chinês
- `checkpoints/converter/` - Conversor de tom

## 🐳 Docker

```bash
# Build
docker build -t openvoice-server .

# Run
docker run -p 8000:8000 openvoice-server
```

## 📝 Licença

MIT License - Baseado no OpenVoice da MyShell


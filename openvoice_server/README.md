# OpenVoice Server

Servidor REST API para clonagem de voz instantânea usando OpenVoice, atualizado para Python 3.12+.

## 🚀 Características

- ✅ Clonagem de voz instantânea
- ✅ Suporte multi-idioma (Inglês, Chinês, Japonês, Espanhol, Francês, Coreano)
- ✅ Processamento em lote
- ✅ API REST moderna com FastAPI
- ✅ Documentação automática com Swagger
- ✅ CORS habilitado
- ✅ Python 3.12+

## 📋 Pré-requisitos

- Python 3.12 ou superior
- CUDA (opcional, para GPU)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/myshell-ai/OpenVoice.git openvoice-server
cd openvoice-server
```

2. Crie um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements_server.txt
```

4. Baixe os modelos do OpenVoice (se necessário):
```bash
# O OpenVoice baixará os modelos automaticamente na primeira execução
```

## 🎯 Uso

### Iniciar o servidor

```bash
python -m openvoice_server.main
```

Ou usando uvicorn diretamente:

```bash
uvicorn openvoice_server.main:app --host 0.0.0.0 --port 8000
```

### Documentação da API

Acesse a documentação interativa do Swagger em:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📡 Endpoints da API

### `GET /`
Endpoint raiz - informações básicas do servidor

### `GET /health`
Verificar status do servidor e modelo

### `GET /languages`
Listar idiomas suportados

### `GET /models`
Informações sobre os modelos carregados

### `POST /clone`
Clonar voz a partir de um arquivo de áudio e texto

**Parâmetros (form-data):**
- `audio_file`: Arquivo de áudio de referência (WAV)
- `text`: Texto a ser sintetizado
- `language`: Idioma (auto, en, zh, ja, es, fr, ko)
- `speed`: Velocidade de fala (padrão: 1.0)

**Resposta:**
Arquivo WAV com áudio sintetizado

### `POST /batch_clone`
Clonar voz para múltiplos textos

**Parâmetros (form-data):**
- `audio_file`: Arquivo de áudio de referência (WAV)
- `texts`: Lista de textos (JSON)
- `language`: Idioma
- `speed`: Velocidade de fala

**Resposta:**
Arquivo ZIP com os áudios sintetizados

## 📝 Exemplos

### Clone de voz simples (curl)

```bash
curl -X POST "http://localhost:8000/clone" \
  -F "audio_file=@reference.wav" \
  -F "text=Hello, this is a test" \
  -F "language=en" \
  -F "speed=1.0" \
  -o output.wav
```

### Clone em lote (Python)

```python
import requests

files = {
    'audio_file': open('reference.wav', 'rb')
}

data = {
    'texts': ['Text 1', 'Text 2', 'Text 3'],
    'language': 'en',
    'speed': 1.0
}

response = requests.post('http://localhost:8000/batch_clone', files=files, data=data)
with open('batch_output.zip', 'wb') as f:
    f.write(response.content)
```

## 🛠️ Desenvolvimento

Para modo desenvolvimento com reload automático:

```bash
uvicorn openvoice_server.main:app --reload --host 0.0.0.0 --port 8000
```

## 📄 Licença

MIT License - livre para uso comercial e de pesquisa

## 🙏 Agradecimentos

- [OpenVoice](https://github.com/myshell-ai/OpenVoice) - MyShell e MIT
- [ValyrianTech](https://github.com/ValyrianTech/) - Inspiração para este servidor


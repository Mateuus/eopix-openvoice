# OpenVoice Server - eopix

Servidor OpenVoice customizado para o projeto eopix.

## 📋 Descrição

Este é um servidor OpenVoice configurado para clonagem de voz com suporte a múltiplos idiomas e estilos de voz.

## 🚀 Instalação

### Requisitos
- Python 3.12+
- CUDA (para GPU)
- Docker (opcional)

### Setup

1. Clone o repositório:
```bash
git clone https://github.com/Mateuus/eopix-openvoice.git
cd eopix-openvoice/openvoice-server
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/WSL
# ou
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements_server.txt
```

4. Configure o arquivo `.env`:
```bash
cp .env.example .env
# Edite o .env e adicione sua chave da OpenAI
OPENAI_API_KEY=sua_chave_aqui
```

5. Baixe os checkpoints (consulte a documentação oficial):
- Os checkpoints devem ser colocados nas pastas `checkpoints/`
- São arquivos grandes e não são versionados no Git

## 🎮 Uso

### Executando os Notebooks

1. Abra o Jupyter:
```bash
jupyter notebook
# ou
jupyter lab
```

2. Execute os notebooks na seguinte ordem:
- `demo_part1.ipynb` - Clonagem de voz com controle de estilo
- `demo_part2.ipynb` - Clonagem cross-lingual com OpenAI TTS
- `demo_part3.ipynb` - Demos adicionais

### Executando o Servidor

```bash
./start_server.sh
```

O servidor estará disponível em `http://localhost:8000`

## 📁 Estrutura do Projeto

```
openvoice-server/
├── openvoice/           # Código fonte do OpenVoice
├── openvoice_server/    # Código do servidor
├── checkpoints/         # Modelos (não versionado)
├── outputs/             # Arquivos de saída (não versionado)
├── processed/           # Arquivos processados (não versionado)
├── resources/           # Recursos de exemplo
├── demo_part*.ipynb    # Notebooks de demonstração
├── requirements_server.txt  # Dependências
└── .env                # Configurações (não versionado)
```

## ⚙️ Configuração

### Configurações do Kernel Jupyter

O kernel "OpenVoice Server" está configurado para usar o ambiente virtual correto e o diretório de trabalho apropriado.

### Variáveis de Ambiente

- `OPENAI_API_KEY`: Chave da API da OpenAI (necessária para o demo_part2)

## 📚 Arquivos Excluídos do Git

Os seguintes arquivos/diretórios são ignorados pelo Git:
- `venv/` - Ambiente virtual
- `checkpoints/` - Modelos treinados
- `outputs/` - Arquivos de saída
- `processed/` - Arquivos processados
- `logs/` - Logs do sistema
- `.env` - Configurações sensíveis
- Arquivos de áudio (`.wav`, `.mp3`)
- Arquivos temporários

## 🐛 Troubleshooting

### Problema: "Please install onnxruntime"
```bash
pip install onnxruntime
```

### Problema: "No module named 'torch'"
```bash
pip install torch torchaudio
```

### Problema: Não gera arquivos em outputs/
- Verifique se o diretório de trabalho está correto
- Verifique se está usando o kernel "OpenVoice Server"

## 📝 Licença

Este projeto é baseado no OpenVoice da MyShell, licenciado sob MIT License.

## 🤝 Contribuição

Este repositório é mantido para o projeto eopix.

## 📧 Contato

Para questões sobre o projeto eopix, consulte o repositório principal.


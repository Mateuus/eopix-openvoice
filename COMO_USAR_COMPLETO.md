# 🎯 Guia Completo: Como Usar o OpenVoice

## 📋 O que você tem agora

### ✅ Arquivos Prontos:
- `demo_part1.ipynb` - Clonagem com V1 (EN/ZH)
- `demo_part2.ipynb` - Clonagem com OpenAI TTS (múltiplos idiomas)
- `demo_part3.ipynb` - Demo com MeloTTS (múltiplos idiomas incluindo PT)
- `demo_portugues.ipynb` - Demo específica para português
- Checkpoints instalados em `checkpoints/` e `checkpoints_v2/`
- Embeddings de PT-BR em `checkpoints_v2/base_speakers/ses/en-br.pth`

### ❌ O que está faltando:
- OpenAI API sem cota (precisa adicionar créditos)
- MeloTTS não instalado (precisa sudo)

## 🚀 Opção 1: Usar OpenAI TTS (MAIS FÁCIL - só precisa adicionar créditos)

### Passos:

1. **Adicionar créditos na OpenAI:**
   - Acesse: https://platform.openai.com/account/billing
   - Adicione método de pagamento
   - Configure limite ($5 é suficiente para testes)

2. **Usar o notebook demo_portugues.ipynb:**
```bash
cd /home/mateuus/projects/eopix/openvoice-server
jupyter lab
# Abra demo_portugues.ipynb
# Execute as células em ordem
```

3. **Resultados serão salvos em:**
   - `outputs/output_pt_0.wav`
   - `outputs/output_pt_1.wav`
   - `outputs/output_pt_2.wav`

## 🔧 Opção 2: Instalar MeloTTS (LOCAL E GRATUITO)

### Instalação Completa:

```bash
# 1. Instalar dependências do sistema
sudo apt-get update
sudo apt-get install -y libssl-dev pkg-config build-essential libffi-dev

# 2. Ativar ambiente virtual
cd /home/mateuus/projects/eopix/openvoice-server
source venv/bin/activate

# 3. Instalar tokenizers com wheel pré-compilado
pip install tokenizers==0.13.3

# 4. Instalar MeloTTS (vai baixar e compilar automaticamente)
pip install git+https://github.com/myshell-ai/MeloTTS.git

# 5. Verificar instalação
python -c "from melo.api import TTS; print('✓ MeloTTS instalado com sucesso!')"
```

### Usar o MeloTTS:

Abra `demo_part3.ipynb` e execute as células. O notebook já está configurado para usar MeloTTS e suporta:
- ✅ Português Brasileiro (PT-BR)
- ✅ Inglês (EN)
- ✅ Espanhol (ES)
- ✅ Francês (FR)
- ✅ Chinês (ZH)
- ✅ Japonês (JP)
- ✅ Coreano (KR)

## 📂 Estrutura dos Arquivos

### Para usar sua própria voz de referência:

1. **Coloque seu arquivo de áudio em `resources/`:**
```bash
cp /caminho/do/seu/audio.mp3 resources/minha_voz.mp3
```

2. **Edite o notebook e troque a linha:**
```python
# No demo_portugues.ipynb, linha ~254:
reference_speaker = 'resources/minha_voz.mp3'  # Troque aqui
```

### Embeddings processados ficam em:
```
processed/
  ├── base_pt_v1_XXXXX/      ← Base speaker em PT
  │   └── se.pth              (embeddings)
  └── example_reference_v1_YYYYY/  ← Sua voz de referência
      └── se.pth               (embeddings)
```

### Resultados finais em:
```
outputs/
  ├── output_pt_0.wav         ← Clonagem 1
  ├── output_pt_1.wav         ← Clonagem 2
  └── output_pt_2.wav         ← Clonagem 3
```

## 🔍 Troubleshooting

### Problema: "Audio too short"
**Solução:** Use áudios de 3-10 segundos

### Problema: "RateLimitError 429"
**Solução:** Adicione créditos na OpenAI ou use MeloTTS

### Problema: "AssertionError: input audio is too short"
**Solução:** Os try/except já tratam isso automaticamente

### Problema: MeloTTS não instala
**Solução:** Execute `sudo apt-get install -y libssl-dev` primeiro

## 📊 Comparação Rápida

| Método | Custo | Qualidade | Setup |
|--------|-------|-----------|-------|
| OpenAI TTS | $ | ⭐⭐⭐⭐⭐ | Fácil |
| MeloTTS | Gratuito | ⭐⭐⭐⭐ | Complexo |

## 🎯 Recomendação

**Para começar AGORA:**
- Adicione $5 de créditos na OpenAI
- Use `demo_portugues.ipynb`

**Para futuro:**
- Instale o MeloTTS quando tiver tempo
- Use sem limites

## 📝 Checklist Final

- [ ] Adicionar créditos OpenAI OU instalar MeloTTS
- [ ] Abrir `demo_portugues.ipynb` ou `demo_part3.ipynb`
- [ ] Executar todas as células
- [ ] Verificar arquivos gerados em `outputs/`
- [ ] Testar com sua própria voz de referência

## 🎉 Você está pronto!

Tudo está configurado. Só precisa escolher:
1. Adicionar créditos OpenAI (mais rápido)
2. Instalar MeloTTS (mais trabalho, mas gratuito)


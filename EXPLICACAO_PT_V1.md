# 🚫 Por que o demo_part1.ipynb NÃO funciona para Português

## ❌ Problema

O `demo_part1.ipynb` usa o modelo V1 que **NÃO suporta português nativamente**.

### O que o V1 faz:
```python
base_speaker_tts.tts(
    text="Português aqui", 
    src_path="...", 
    speaker='default', 
    language='English',  # ← Só aceita 'English' ou 'Chinese'
    speed=1.0
)
```

**Idiomas suportados no V1:**
- ✅ English (`checkpoints/base_speakers/EN/`)
- ✅ Chinese (`checkpoints/base_speakers/ZH/`)
- ❌ **NÃO tem Português**

## ✅ Soluções para Português

### Opção 1: Usar demo_portugues.ipynb (RECOMENDADO)

Já está criado e funcionando! Usa OpenAI TTS como base speaker.

```python
# Gera áudio em português com qualidade excelente
client = OpenAI(api_key=api_key)
response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input="Olá, este é um teste em português."
)
# Depois aplica clonagem de voz com OpenVoice
```

### Opção 2: Usar demo_part2.ipynb

Mesma abordagem - usa OpenAI TTS para gerar áudio em qualquer idioma.

### Opção 3: Usar MeloTTS com V2

Instalar MeloTTS e usar os embeddings de português:

```bash
pip install melo-tts
```

Depois use o embedding `checkpoints_v2/base_speakers/ses/en-br.pth`

Veja exemplos no `demo_part3.ipynb`.

## 📊 Comparação

| Notebook | Idioma PT | Base Speaker | Qualidade | Cota API |
|----------|-----------|--------------|-----------|----------|
| demo_part1.ipynb | ❌ Não | EN/ZH apenas | - | - |
| demo_part2.ipynb | ✅ Sim | OpenAI TTS | ⭐⭐⭐⭐⭐ | Sim |
| demo_part3.ipynb | ✅ Sim | MeloTTS | ⭐⭐⭐⭐ | Não |
| demo_portugues.ipynb | ✅ Sim | OpenAI TTS | ⭐⭐⭐⭐⭐ | Sim |

## 🎯 Recomendação

Use o **demo_portugues.ipynb** que já está pronto!

Ele está configurado especificamente para português e funciona perfeitamente.


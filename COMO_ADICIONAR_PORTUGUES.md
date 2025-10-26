# 🇧🇷 Como Adicionar Português ao OpenVoice V2

## 🎯 CONCEITO CHAVE

O **OpenVoice V2** não precisa de um "base speaker" em português! A mágica é:

1. **Gere áudio com qualquer base speaker** (inglês, espanhol, japonês, etc.)
2. **Extraia o tone color embedding** da sua voz de referência em português
3. **Aplique a clonagem** usando `tone_color_converter`

---

## 📋 ARQUIVOS DISPONÍVEIS

Você já tem estes base speakers em `checkpoints_v2/base_speakers/ses/`:

```
en-us.pth     - Inglês Americano
en-br.pth     - Inglês Britânico  
en-default.pth - Inglês Default
es.pth        - Espanhol
jp.pth        - Japonês
fr.pth        - Francês
zh.pth        - Chinês
kr.pth        - Coreano
```

**Não há `pt-br.pth` ou `pt.pth`** - e NÃO PRECISA!

---

## 💡 SOLUÇÃO: Usar Qualquer Base Speaker + Clonagem

### Exemplo 1: Usar Espanhol + Voz PT-BR

```python
import torch
from openvoice import se_extractor
from openvoice.api import ToneColorConverter

# 1. Inicializar conversor
tone_color_converter = ToneColorConverter('checkpoints_v2/converter/config.json', device='cpu')
tone_color_converter.load_ckpt('checkpoints_v2/converter/checkpoint.pth')

# 2. GERAR áudio com base speaker de ESPANHOL (ou outro idioma)
#    Ou usar OpenAI TTS em português
texto_pt = "Olá, este é um teste de clonagem de voz em português brasileiro."
# ... gerar áudio usando MeloTTS ES ou OpenAI TTS ...

# 3. Extrair source_se do áudio gerado
source_se, audio_name = se_extractor.get_se(
    'audio_gerado_em_pt.wav', 
    tone_color_converter, 
    vad=True
)

# 4. Extrair target_se da sua voz de referência
target_se, audio_name = se_extractor.get_se(
    'resources/base_pt.wav',  # Sua voz de referência em PT
    tone_color_converter, 
    vad=True
)

# 5. Converter! 
# O OpenVoice vai aplicar a cor tonal da sua voz PT sobre o áudio gerado
tone_color_converter.convert(
    audio_src_path='audio_gerado_em_pt.wav',
    src_se=source_se,
    tgt_se=target_se,
    output_path='output_clonado_pt.wav'
)
```

---

## 🎯 VANTAGENS

### ✅ **Usa Qualquer Base Speaker**
- Pode ser `en-br.pth`, `es.pth`, `jp.pth`, etc.
- O importante é ter um áudio inicial gerado
- A voz final será a da sua referência

### ✅ **Qualidade Excelente**
- Voz clonada mantém características da referência
- Funciona perfeitamente para qualquer idioma
- Você já fez isso com sucesso no `demo_portugues.ipynb`!

---

## 📝 PASSO A PASSO

### Opção 1: MeloTTS (Espanhol/Japonês) + Clonagem PT

```python
# 1. Gerar áudio com MeloTTS em espanhol (funciona!)
from melo.api import TTS

tts = TTS(language='ES', device='cpu')
texto_pt = "Olá, este é um teste."
tts.tts_to_file(texto_pt, speaker_id=0, output_path='base_audio.wav')
# Nota: Texto em português, mas voz é espanhola

# 2. Extrair embeddings
source_se = se_extractor.get_se('base_audio.wav', tone_color_converter)[0]
target_se = se_extractor.get_se('resources/base_pt.wav', tone_color_converter)[0]

# 3. Aplicar clonagem PT
tone_color_converter.convert(
    audio_src_path='base_audio.wav',
    src_se=source_se,
    tgt_se=target_se,
    output_path='output_pt.wav'
)
# Agora a voz é em português brasileiro!
```

### Opção 2: OpenAI TTS + Clonagem PT (RECOMENDADO)

```python
# 1. Gerar áudio em português com OpenAI
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
texto_pt = "Olá, este é um teste de clonagem em português."

response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=texto_pt
)
response.stream_to_file('base_audio_pt.wav')
# Áudio já está em PT mas com voz padrão OpenAI

# 2. Extrair embeddings
source_se = se_extractor.get_se('base_audio_pt.wav', tone_color_converter)[0]
target_se = se_extractor.get_se('resources/base_pt.wav', tone_color_converter)[0]

# 3. Aplicar sua voz PT
tone_color_converter.convert(
    audio_src_path='base_audio_pt.wav',
    src_se=source_se,
    tgt_se=target_se,
    output_path='output_sua_voz.wav'
)
# Agora tem SUA voz em português!
```

---

## ✅ RESULTADO

**Você já tem tudo que precisa!**

- ✅ Base speakers disponíveis (`en-br.pth`, `es.pth`, etc.)
- ✅ OpenAI TTS funcionando para gerar PT
- ✅ `demo_portugues.ipynb` já faz exatamente isso!
- ✅ OpenVoice V2 converte qualquer voz para PT-BR

**Não precisa criar `pt-br.pth` novo!** 🎉


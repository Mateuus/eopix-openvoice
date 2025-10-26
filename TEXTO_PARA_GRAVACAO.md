# 📝 Texto para Gravação de Voz de Referência

## 🎤 Texto Completo (25-30 segundos)

```
Olá, este é um teste de clonagem de voz em português brasileiro. 
Meu nome é [digite seu nome aqui]. Estou gravando esta mensagem para 
usar como voz de referência no sistema OpenVoice. Esta tecnologia permite 
replicar a cor tonal de qualquer voz de forma muito realista. Espero que 
funcione perfeitamente com este áudio de teste.
```

---

## 🎤 Versão Curta (15-20 segundos)

```
Olá, este é um teste de clonagem de voz em português. Meu nome é 
[seu nome]. Estou gravando esta mensagem para usar como voz de referência 
no sistema OpenVoice. Esta tecnologia permite replicar vozes de forma 
realista. Espero que funcione perfeitamente.
```

---

## 🎤 Versão Longa (30-40 segundos)

```
Olá, este é um teste de clonagem de voz em português brasileiro para 
o sistema OpenVoice. Meu nome é [seu nome]. Estou gravando esta mensagem 
com o objetivo de criar uma voz de referência que será usada em testes 
de clonagem vocal. Esta tecnologia permite replicar a cor tonal de qualquer 
voz de forma muito realista e precisa. Espero que esta gravação sirva 
como uma boa base para os experimentos de clonagem de voz.
```

---

## 📋 Instruções para Gravar

### ⚠️ IMPORTANTE:

1. **Fale naturalmente** - não leia como robô
2. **Voz clara** - articule bem as palavras
3. **Ritmo normal** - não fale muito rápido ou devagar
4. **Tom natural** - use sua voz normal do dia a dia
5. **Ambiente silencioso** - evite ruídos de fundo
6. **Duração** - 15-30 segundos é ideal

### ✅ Exemplo de Como Falar:

- Faça pausas naturais nos pontos
- Respire normalmente
- Pronuncie todas as palavras completamente
- Mantenha um tom consistente

### ❌ Evite:

- ❌ Sussurrar ou gritar
- ❌ Falar muito rápido
- ❌ Ambiente com barulho
- ❌ Voz muito baixa ou distorcida
- ❌ Música ou efeitos de fundo

---

## 🎯 Script Recomendado (use este!)

**Versão otimizada de 20-25 segundos:**

```
Olá, este é um teste de clonagem de voz em português brasileiro.
Meu nome é [digite seu nome]. Estou gravando esta voz de referência
para o projeto de clonagem de voz com OpenVoice. Esta tecnologia
permite replicar a cor tonal de qualquer voz de forma muito realista
e precisa. Espero que esta gravação funcione bem para os testes.
```

---

## 📱 Como Gravar

### No Celular:

1. Abra o app "Gravador" ou "Gravação de Voz"
2. Toque em "Gravar"
3. Leia o texto acima
4. Toque em "Parar"
5. Salve como **WAV** ou **MP3**

### No Computador:

**Windows:**
- App "Gravador de Som" (built-in)
- Ou use Audacity (gratuito)

**Mac:**
- QuickTime Player
- Ou GarageBand

**Linux:**
```bash
# Usando Audacity
sudo apt install audacity
# Ou via terminal:
arecord -d 30 -f cd -t wav minha_voz.wav
```

---

## 📤 Depois de Gravar

```bash
# Copiar para o projeto
cp /caminho/do/arquivo.wav \
   /home/mateuus/projects/eopix/openvoice-server/resources/minha_voz.wav

# Verificar
ls -lh /home/mateuus/projects/eopix/openvoice-server/resources/minha_voz.wav

# Editar o script
nano /home/mateuus/projects/eopix/openvoice-server/test_portugues.py
# Mude a linha 52 para:
# reference_speaker = 'resources/minha_voz.wav'

# Executar teste
cd /home/mateuus/projects/eopix/openvoice-server
source venv/bin/activate
python test_portugues.py
```

---

## ✅ Exemplo Final de Gravação

```
[PAUSA 1 segundo]

Olá, este é um teste de clonagem de voz em português brasileiro.
[PAUSA]
Meu nome é João Silva. Estou gravando esta voz de referência
para o projeto de clonagem de voz com OpenVoice.
[PAUSA]
Esta tecnologia permite replicar a cor tonal de qualquer voz
de forma muito realista e precisa.
[PAUSA]
Espero que esta gravação funcione bem para os testes.

[PAUSA 1 segundo]
```

**Total:** ~25 segundos

---

## 💡 Dicas Extras

### Para Melhor Qualidade:

1. **Microfone**: Use fones de ouvido com microfone ou microfone externo
2. **Distância**: Fique a 15-20cm do microfone
3. **Teste**: Grave 2-3 versões e escolha a melhor
4. **Revisão**: Ouça antes de usar para verificar qualidade
5. **Volume**: Mantenha o volume médio (nem muito alto nem muito baixo)

### Formato Recomendado:

- **Formato**: WAV (melhor qualidade)
- **Taxa de amostragem**: 16 kHz ou 44.1 kHz
- **Bit depth**: 16-bit
- **Canais**: Mono (1 canal) ou Stereo

---

Boa sorte com a gravação! 🎤

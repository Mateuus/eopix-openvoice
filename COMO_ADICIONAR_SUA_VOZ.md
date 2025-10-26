# 🎤 Como Adicionar Sua Voz de Referência

## 📝 Passo a Passo

### 1️⃣ **Gravar Sua Voz**

Você precisa gravar um áudio de voz para usar como referência.

**Como gravar:**
- Use seu celular ou computador
- Grave em **WAV** ou **MP3**
- **Duração:** 10-60 segundos (quanto mais longo, melhor!)
- **Qualidade:** Quanto mais clara a gravação, melhor será a clonagem
- **Conteúdo:** Fale naturalmente sobre qualquer assunto

**Exemplo:**
```
"Olá, meu nome é [seu nome]. Estou testando o OpenVoice para clonagem de voz. 
Esta é minha voz de referência. Espero que funcione bem com a tecnologia de clonagem."
```

### 2️⃣ **Colocar o Arquivo no Projeto**

Copie o arquivo de áudio para a pasta `resources/`:

```bash
# Exemplo:
cp /caminho/do/seu/audio.wav /home/mateuus/projects/eopix/openvoice-server/resources/minha_voz.wav
```

**Arquivos suportados:**
- `.wav` (recomendado)
- `.mp3`
- `.m4a`
- `.flac`

### 3️⃣ **Usar no Código**

#### Opção A: Modificar o Script `test_portugues.py`

Edite o arquivo e mude esta linha:

```python
# Linha 52 - TROCAR DE:
reference_speaker = 'resources/base_pt.wav'

# PARA:
reference_speaker = 'resources/minha_voz.wav'
```

#### Opção B: Usar no Notebbok

No Jupyter, modifique a célula que define `reference_speaker`:

```python
reference_speaker = 'resources/minha_voz.wav'  # SUA VOZ
```

---

## 🎯 Teste Rápido

Depois de colocar seu arquivo, execute:

```bash
cd /home/mateuus/projects/eopix/openvoice-server
source venv/bin/activate
python test_portugues.py
```

O script vai:
1. ✅ Extrair o tone color embedding da SUA voz
2. ✅ Gerar áudio com o texto
3. ✅ Aplicar clonagem usando SUA voz
4. ✅ Salvar em `outputs/`

---

## 💡 Dicas para Melhor Qualidade

### ✅ **Faça:**
- Fale pausadamente e claramente
- Grave em ambiente silencioso
- Use microfone de boa qualidade
- Grave 15-30 segundos mínimo
- Fale de forma natural (não exagerada)

### ❌ **Evite:**
- Ruídos de fundo
- Áudio muito curto (< 5 segundos)
- Voz muito baixa ou alta
- Trechos de música ou outros sons
- Sussurros ou gritos

---

## 📁 Estrutura de Arquivos

```
openvoice-server/
├── resources/
│   ├── base_pt.wav        ← Voz padrão (atual)
│   ├── minha_voz.wav      ← SUA voz
│   └── demo_speaker0.mp3  ← Outros exemplos
│
├── test_portugues.py      ← Script para testar
└── outputs/               ← Áudios gerados aqui
    ├── test_final_clonado.wav
    └── ...
```

---

## 🔧 Teste com Múltiplas Vozes

Você pode ter várias vozes de referência:

```bash
resources/
├── minha_voz.wav
├── voz_amigo.wav
├── voz_narrador.wav
└── base_pt.wav
```

E testar cada uma:

```python
# Em test_portugues.py
opcoes_voz = [
    'resources/minha_voz.wav',
    'resources/voz_amigo.wav',
    'resources/voz_narrador.wav'
]

# Testar todas
for voz in opcoes_voz:
    print(f"\n🎤 Testando com: {voz}")
    reference_speaker = voz
    # ... resto do código
```

---

## ✅ Exemplo Prático

```bash
# 1. Copiar seu áudio
cp /tmp/minha_gravacao.wav /home/mateuus/projects/eopix/openvoice-server/resources/

# 2. Editar o script
nano test_portugues.py
# Mude: reference_speaker = 'resources/minha_gravacao.wav'

# 3. Executar
python test_portugues.py

# 4. Ouça o resultado
ls -lh outputs/
play outputs/test_final_clonado.wav
```

---

## 🎉 Resultado

Quando executar, o áudio final terá **SUA VOZ** falando em português! 🎤

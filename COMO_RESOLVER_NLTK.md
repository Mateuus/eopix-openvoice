# 🔧 Como Resolver o Problema do NLTK

## ❌ O PROBLEMA

O MeloTTS precisa do NLTK para o g2p_en (pronúncia em inglês), mas o download está bloqueado por rate limit (HTTP 429).

## ✅ SOLUÇÕES

### OPÇÃO 1: Baixar Manualmente (MAIS RÁPIDO)

```bash
# 1. Baixar manualmente do GitHub
cd /tmp
wget https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/taggers/averaged_perceptron_tagger_eng.zip

# 2. Criar diretório
mkdir -p /tmp/nltk/taggers
cd /tmp/nltk/taggers

# 3. Extrair
unzip /tmp/averaged_perceptron_tagger_eng.zip

# 4. Renomear para o nome correto
mv averaged_perceptron_tagger_eng/* ./
rmdir averaged_perceptron_tagger_eng

# 5. Testar
cd /home/mateuus/projects/eopix/openvoice-server
source venv/bin/activate
export NLTK_DATA=/tmp/nltk
python -c "from melo.api import TTS; tts = TTS(language='EN', device='cpu'); tts.tts_to_file('Hello world', 0, 'test.wav', quiet=True)"
```

### OPÇÃO 2: Aguardar Rate Limit (1-2 horas)

O rate limit do NLTK costuma durar 1-2 horas. Aguarde e tente novamente:

```bash
cd /home/mateuus/projects/eopix/openvoice-server
source venv/bin/activate
python -c "import nltk; nltk.download('averaged_perceptron_tagger_eng', download_dir='/tmp/nltk')"
```

### OPÇÃO 3: Usar OpenAI TTS (RECOMENDADO)

O `demo_portugues.ipynb` já funciona perfeitamente com OpenAI TTS e **SUPORTA PORTUGUÊS**.

**Vantagens:**
- ✅ Funciona imediatamente
- ✅ Suporta português nativo
- ✅ Qualidade excelente
- ✅ Sem dependências complexas

**Custo:** ~$5/mês para testes

---

## 📝 SITUAÇÃO ATUAL

✅ **Funcionando:**
- MeloTTS instalado
- Transformers 4.57.1 funcionando
- Tokenizers pré-compilado funcionando
- TTS inicializa corretamente

❌ **Bloqueado:**
- NLTK rate limit (HTTP 429)
- Impossível baixar `averaged_perceptron_tagger_eng`

---

## 🎯 RECOMENDAÇÃO

**Use o `demo_portugues.ipynb` com OpenAI TTS!**

Ele já está funcionando e suporta português. MeloTTS é útil apenas para idiomas não suportados pelo OpenVoice V1 (JP, KR, etc.).

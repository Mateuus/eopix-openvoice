# 📦 Como Instalar o MeloTTS - Guia Completo

## ⚠️ ATENÇÃO

O MeloTTS requer compilação Rust e várias dependências do sistema. 

## 🔧 Opção 1: MeloTTS (Mais Completo, Requer sudo)

### Passos:

1. **Instalar dependências do sistema:**
```bash
sudo apt-get update
sudo apt-get install -y libssl-dev pkg-config build-essential
```

2. **Rust já está instalado ✅** (feito anteriormente)

3. **Instalar tokenizers:**
```bash
cd /home/mateuus/projects/eopix/openvoice-server
source venv/bin/activate
pip install tokenizers==0.13.3
```

4. **Instalar MeloTTS:**
```bash
pip install git+https://github.com/myshell-ai/MeloTTS.git
```

5. **Verificar instalação:**
```bash
python -c "import melo; print('MeloTTS instalado!')"
```

## 🎯 Opção 2: Usar o que já temos (RECOMENDADO)

Você NÃO precisa do MeloTTS agora! Use o que já temos:

### ✅ **demo_portugues.ipynb** - Já funciona
- Usa OpenAI TTS
- Basta adicionar créditos na API
- Muito mais simples

### Como funciona agora:
1. Abra `demo_portugues.ipynb`
2. Execute as células
3. Ou adicione créditos na OpenAI API

## 💰 Comparação

| Opção | Custo | Complexidade | Status |
|-------|-------|--------------|--------|
| **demo_portugues.ipynb** | Precisa créditos OpenAI | ⭐ Fácil | ✅ Funciona |
| **MeloTTS** | Gratuito | ⭐⭐⭐⭐⭐ Complexo | ❌ Requer sudo + build |

## 🎯 Recomendação Final

**Não instale o MeloTTS agora!**

Você já tem:
- ✅ Notebook funcionando (`demo_portugues.ipynb`)
- ✅ Embeddings de PT-BR prontos
- ✅ Tudo configurado

**Apenas aguarde adicionar créditos na OpenAI** ou use o que já está funcionando.


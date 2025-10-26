# 📁 Onde Colocar o Arquivo de Referência

## Caminho Atual (Padrão)
```python
reference_speaker = 'resources/example_reference.mp3'
```

## Opções Disponíveis

### 1. Usar arquivos existentes em `resources/`
Você tem 4 arquivos já disponíveis:
- `resources/example_reference.mp3` (939 KB)
- `resources/demo_speaker0.mp3` (302 KB)
- `resources/demo_speaker1.mp3` (713 KB)
- `resources/demo_speaker2.mp3` (461 KB)

### 2. Colocar seu próprio arquivo
Coloque seu áudio na pasta `resources/`:
```bash
cp /caminho/do/seu/audio.mp3 resources/minha_voz.mp3
```

Depois altere no notebook:
```python
reference_speaker = 'resources/minha_voz.mp3'
```

### 3. Usar caminho absoluto
```python
reference_speaker = '/caminho/completo/para/seu/audio.mp3'
```

## Requisitos do Áudio de Referência

- ✅ **Duração**: 3-10 segundos (ideal)
- ✅ **Qualidade**: Fala clara e limpa
- ✅ **Formato**: MP3, WAV, ou qualquer formato de áudio
- ✅ **Conteúdo**: Uma pessoa falando (sem ruído de fundo se possível)

## Exemplo de Uso no Notebook

Na célula onde você extrai o embedding da referência, edite a linha:

```python
reference_speaker = 'resources/example_reference.mp3'  # Troque aqui!
```

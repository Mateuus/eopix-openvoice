"""
OpenVoice Server - Servidor principal FastAPI
Servidor REST API moderno para clonagem de voz usando OpenVoice
"""
import os
import torch
from fastapi import FastAPI, HTTPException, UploadFile, File, BackgroundTasks
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import tempfile
from typing import Optional
from datetime import datetime
import soundfile as sf

from openvoice import se_extractor
from openvoice.api import BaseSpeakerTTS, ToneColorConverter
from openvoice_server.config import settings

app = FastAPI(
    title="OpenVoice Server",
    description="API REST para clonagem de voz instantânea usando OpenVoice",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos globais
base_speaker_tts_en = None
base_speaker_tts_zh = None
tone_color_converter = None
source_se_en = None
source_se_zh = None

def load_models():
    """Carregar todos os modelos do OpenVoice"""
    global base_speaker_tts_en, base_speaker_tts_zh
    global tone_color_converter, source_se_en, source_se_zh
    
    device = settings.DEVICE
    
    print("Carregando modelos OpenVoice...")
    
    # Verificar se checkpoints existem
    if not os.path.exists('checkpoints'):
        print("⚠️  Diretório 'checkpoints' não encontrado!")
        print("📝 Consulte SETUP_CHECKPOINTS.md para instruções de download")
        return
    
    # Modelos base
    try:
        ckpt_base_en = 'checkpoints/base_speakers/EN'
        if os.path.exists(ckpt_base_en):
            base_speaker_tts_en = BaseSpeakerTTS(f'{ckpt_base_en}/config.json', device=device)
            base_speaker_tts_en.load_ckpt(f'{ckpt_base_en}/checkpoint.pth')
            print("Modelo inglês carregado!")
            
            source_se_en = torch.load(f'{ckpt_base_en}/en_default_se.pth').to(device)
    except Exception as e:
        print(f"Erro ao carregar modelo inglês: {e}")
    
    try:
        ckpt_base_zh = 'checkpoints/base_speakers/ZH'
        if os.path.exists(ckpt_base_zh):
            base_speaker_tts_zh = BaseSpeakerTTS(f'{ckpt_base_zh}/config.json', device=device)
            base_speaker_tts_zh.load_ckpt(f'{ckpt_base_zh}/checkpoint.pth')
            print("Modelo chinês carregado!")
            
            source_se_zh = torch.load(f'{ckpt_base_zh}/zh_default_se.pth').to(device)
    except Exception as e:
        print(f"Erro ao carregar modelo chinês: {e}")
    
    # Conversor de tom
    try:
        ckpt_converter = 'checkpoints/converter'
        if os.path.exists(ckpt_converter):
            tone_color_converter = ToneColorConverter(
                f'{ckpt_converter}/config.json', 
                device=device,
                enable_watermark=True
            )
            tone_color_converter.load_ckpt(f'{ckpt_converter}/checkpoint.pth')
            print("Conversor de tom carregado!")
    except Exception as e:
        print(f"Erro ao carregar conversor: {e}")
    
    print("Modelos carregados com sucesso!")

@app.on_event("startup")
async def startup_event():
    """Inicializar modelos na inicialização do servidor"""
    load_models()

@app.get("/")
async def root():
    """Endpoint raiz"""
    return {
        "message": "OpenVoice Server API",
        "version": "1.0.0",
        "status": "online",
        "device": settings.DEVICE
    }

@app.get("/health")
async def health_check():
    """Verificar status do servidor"""
    models_loaded = {
        "english": base_speaker_tts_en is not None,
        "chinese": base_speaker_tts_zh is not None,
        "converter": tone_color_converter is not None
    }
    
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "device": settings.DEVICE,
        "models": models_loaded
    }

@app.post("/clone")
async def clone_voice(
    background_tasks: BackgroundTasks,
    audio_file: UploadFile = File(...),
    text: str = None,
    language: str = "en",
    speaker: str = "default",
    speed: float = 1.0
):
    """
    Clonar voz a partir de um arquivo de áudio e texto
    
    Args:
        audio_file: Arquivo de áudio de referência (WAV, MP3, etc.)
        text: Texto a ser sintetizado
        language: Idioma (en, zh)
        speaker: Estilo da voz (default, friendly, excited, etc.)
        speed: Velocidade de fala (padrão: 1.0)
    
    Returns:
        Arquivo de áudio WAV sintetizado
    """
    if not text:
        raise HTTPException(status_code=400, detail="Parâmetro 'text' é obrigatório")
    
    if language == "en" and base_speaker_tts_en is None:
        raise HTTPException(status_code=503, detail="Modelo inglês não carregado")
    if language == "zh" and base_speaker_tts_zh is None:
        raise HTTPException(status_code=503, detail="Modelo chinês não carregado")
    if not tone_color_converter:
        raise HTTPException(status_code=503, detail="Conversor não carregado")
    
    try:
        # Salvar arquivo de referência temporariamente
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_ref:
            content = await audio_file.read()
            temp_ref.write(content)
            temp_ref_path = temp_ref.name
        
        # Selecionar modelo base conforme idioma
        if language == "zh":
            base_tts = base_speaker_tts_zh
            source_se = source_se_zh
        else:
            base_tts = base_speaker_tts_en
            source_se = source_se_en
        
        # Extrair embedding da voz de referência
        target_se, audio_name = se_extractor.get_se(
            temp_ref_path, 
            tone_color_converter, 
            target_dir='processed', 
            vad=True
        )
        
        # Criar arquivos temporários para processamento
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_src:
            temp_src_path = temp_src.name
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_out:
            temp_out_path = temp_out.name
        
        # Sintetizar voz com o modelo base
        base_tts.tts(
            text=text,
            output_path=temp_src_path,
            speaker=speaker,
            language='English' if language == 'en' else 'Chinese',
            speed=speed
        )
        
        # Converter cor de tom
        encode_message = "@MyShell"
        tone_color_converter.convert(
            audio_src_path=temp_src_path,
            src_se=source_se,
            tgt_se=target_se,
            output_path=temp_out_path,
            tau=0.3,
            message=encode_message
        )
        
        # Limpar arquivos temporários
        background_tasks.add_task(os.unlink, temp_ref_path)
        background_tasks.add_task(os.unlink, temp_src_path)
        background_tasks.add_task(os.unlink, temp_out_path)
        
        return FileResponse(
            temp_out_path,
            media_type="audio/wav",
            filename="output.wav"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/languages")
async def get_languages():
    """Obter lista de idiomas suportados"""
    return {
        "supported_languages": ["en", "zh"],
        "language_names": {
            "en": "English",
            "zh": "Chinese"
        }
    }

@app.get("/speakers")
async def get_speakers():
    """Obter lista de estilos de voz disponíveis"""
    return {
        "speakers": [
            "default",
            "friendly",
            "cheerful",
            "excited",
            "sad",
            "angry",
            "terrified",
            "shouting",
            "whispering"
        ],
        "description": "Estilos de voz disponíveis para síntese"
    }

@app.get("/models")
async def get_models():
    """Obter informações sobre os modelos carregados"""
    return {
        "openvoice": {
            "version": "V1",
            "device": settings.DEVICE
        },
        "models_loaded": {
            "english": base_speaker_tts_en is not None,
            "chinese": base_speaker_tts_zh is not None,
            "converter": tone_color_converter is not None
        }
    }

if __name__ == "__main__":
    uvicorn.run(
        "openvoice_server.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD
    )

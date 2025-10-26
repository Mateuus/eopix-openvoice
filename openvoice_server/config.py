"""
Configurações do OpenVoice Server
"""
import os
from typing import Optional

class Settings:
    """Configurações do servidor"""
    
    # Servidor
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    RELOAD: bool = DEBUG
    
    # OpenVoice
    SAMPLE_RATE: int = 24000
    DEVICE: str = "cuda" if os.getenv("USE_GPU", "true").lower() == "true" else "cpu"
    
    # Modelos
    BASE_MODEL_PATH: Optional[str] = os.getenv("BASE_MODEL_PATH", None)
    SE_MODEL_PATH: Optional[str] = os.getenv("SE_MODEL_PATH", None)
    
    # Detecção de idioma
    DEFAULT_LANGUAGE: str = "auto"
    SUPPORTED_LANGUAGES: list = [
        "auto", "en", "zh", "ja", "es", "fr", "ko"
    ]
    
    # Audio
    MAX_AUDIO_DURATION: int = 60  # segundos
    MAX_TEXT_LENGTH: int = 500
    
    # Batch processing
    MAX_BATCH_SIZE: int = 10
    
    # Performance
    NUM_WORKERS: int = int(os.getenv("NUM_WORKERS", "1"))
    
    @classmethod
    def to_dict(cls) -> dict:
        """Converter configurações para dicionário"""
        return {
            "host": cls.HOST,
            "port": cls.PORT,
            "debug": cls.DEBUG,
            "device": cls.DEVICE,
            "sample_rate": cls.SAMPLE_RATE,
            "default_language": cls.DEFAULT_LANGUAGE,
            "supported_languages": cls.SUPPORTED_LANGUAGES,
            "max_batch_size": cls.MAX_BATCH_SIZE
        }

settings = Settings()


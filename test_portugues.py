#!/usr/bin/env python3
"""
Teste de clonagem de voz em português com OpenVoice V2
"""

import os
import sys
import torch
import warnings
warnings.filterwarnings('ignore')

# Configurar diretório de trabalho
os.chdir('/home/mateuus/projects/eopix/openvoice-server')

print("=" * 60)
print("🎤 TESTE DE CLONAGEM DE VOZ EM PORTUGUÊS")
print("=" * 60)

# Importar bibliotecas
try:
    from openvoice import se_extractor
    from openvoice.api import ToneColorConverter
    print("✅ OpenVoice importado")
except Exception as e:
    print(f"❌ Erro ao importar OpenVoice: {e}")
    sys.exit(1)

# Configurações
ckpt_converter = 'checkpoints_v2/converter'
device = "cuda:0" if torch.cuda.is_available() else "cpu"
output_dir = 'outputs'

os.makedirs(output_dir, exist_ok=True)

print(f"\n📁 Device: {device}")
print(f"📁 Output directory: {output_dir}")

# Carregar conversor
print("\n⏳ Carregando ToneColorConverter...")
try:
    tone_color_converter = ToneColorConverter(
        f'{ckpt_converter}/config.json', 
        device=device
    )
    tone_color_converter.load_ckpt(f'{ckpt_converter}/checkpoint.pth')
    print("✅ ToneColorConverter carregado")
except Exception as e:
    print(f"❌ Erro ao carregar conversor: {e}")
    sys.exit(1)

# Caminhos dos arquivos
reference_speaker = 'resources/base_pt.wav'

# Texto longo para garantir que o áudio seja suficiente (> 10 segundos)
textos_pt = [
    "Olá, este é um teste de clonagem de voz em português brasileiro. " * 3 +
    "O OpenVoice é capaz de replicar a cor tonal de qualquer voz. " * 3 +
    "Essa tecnologia permite clonar vozes de forma muito realista. " * 3
]

print(f"\n📝 Textos de teste:")
for i, texto in enumerate(textos_pt, 1):
    print(f"   {i}. {texto[:60]}...")

# Extrair embedding da voz de referência
print(f"\n⏳ Extraindo tone color embedding da referência...")
print(f"   Arquivo: {reference_speaker}")

try:
    target_se, audio_name = se_extractor.get_se(
        reference_speaker, 
        tone_color_converter, 
        vad=True
    )
    print(f"✅ Embedding extraído: {audio_name}")
except AssertionError as e:
    print(f"⚠️ Áudio muito curto para VAD. Tentando sem VAD...")
    target_se, audio_name = se_extractor.get_se(
        reference_speaker, 
        tone_color_converter, 
        vad=False
    )
    print(f"✅ Embedding extraído (sem VAD): {audio_name}")
except Exception as e:
    print(f"❌ Erro ao extrair embedding: {e}")
    sys.exit(1)

# Gerar áudio base com OpenAI TTS (opção 1)
print("\n" + "=" * 60)
print("OPÇÃO 1: Gerar áudio base com OpenAI TTS")
print("=" * 60)

try:
    from openai import OpenAI
    from dotenv import load_dotenv
    
    load_dotenv()
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if api_key:
        print("✅ API Key encontrada")
        client = OpenAI(api_key=api_key)
        
        # Testar com um texto
        texto_teste = textos_pt[0]
        print(f"\n📝 Gerando áudio: {texto_teste}")
        
        try:
            response = client.audio.speech.create(
                model="tts-1",
                voice="nova",
                input=texto_teste
            )
            
            base_speaker_path = f'{output_dir}/openai_base_pt.wav'
            response.stream_to_file(base_speaker_path)
            
            # Verificar tamanho do arquivo
            size_kb = os.path.getsize(base_speaker_path) / 1024
            print(f"✅ Áudio gerado: {base_speaker_path} ({size_kb:.1f} KB)")
            
            # Extrair embedding do áudio gerado
            print("\n⏳ Extraindo embedding do áudio gerado...")
            source_se, audio_name = se_extractor.get_se(
                base_speaker_path, 
                tone_color_converter, 
                vad=False
            )
            print(f"✅ Embedding extraído: {audio_name}")
            
            # Aplicar clonagem
            output_path = f'{output_dir}/output_openai_pt_clonado.wav'
            print(f"\n⏳ Aplicando clonagem de voz...")
            print(f"   Input: {base_speaker_path}")
            print(f"   Output: {output_path}")
            
            tone_color_converter.convert(
                audio_src_path=base_speaker_path,
                src_se=source_se,
                tgt_se=target_se,
                output_path=output_path,
                message="@MyShell"
            )
            
            size_kb = os.path.getsize(output_path) / 1024
            print(f"✅ Áudio clonado gerado: {output_path} ({size_kb:.1f} KB)")
            print("\n🎉 SUCESSO! Clonagem de voz em português concluída!")
            
        except Exception as e:
            print(f"❌ Erro ao gerar áudio com OpenAI: {e}")
            if "429" in str(e) or "quota" in str(e).lower():
                print("\n💡 SOLUÇÃO: Adicione créditos na OpenAI")
                print("   https://platform.openai.com/account/billing")
    else:
        print("⚠️ OPENAI_API_KEY não configurada no .env")
        print("   Pulando geração com OpenAI TTS...")
        
except ImportError:
    print("⚠️ OpenAI não instalado ou não importado")
    print("   Pulando geração com OpenAI TTS...")

# OPÇÃO 2: Usar MeloTTS (Espanhol/Japonês)
print("\n" + "=" * 60)
print("OPÇÃO 2: Gerar áudio base com MeloTTS (Espanhol)")
print("=" * 60)

try:
    from melo.api import TTS
    
    print("✅ MeloTTS disponível")
    
    # Configurar NLTK_DATA
    os.environ['NLTK_DATA'] = '/tmp/nltk'
    
    # Testar com espanhol (funciona!)
    print("\n📝 Gerando áudio com MeloTTS (ES)...")
    tts = TTS(language='ES', device='cpu')
    
    texto_teste = textos_pt[0]
    print(f"   Texto: {texto_teste}")
    
    melo_base_path = f'{output_dir}/melo_base_es.wav'
    tts.tts_to_file(texto_teste, speaker_id=0, output_path=melo_base_path, quiet=True)
    
    size_kb = os.path.getsize(melo_base_path) / 1024
    print(f"✅ Áudio gerado: {melo_base_path} ({size_kb:.1f} KB)")
    
    # Extrair embedding
    print("\n⏳ Extraindo embedding...")
    source_se, audio_name = se_extractor.get_se(
        melo_base_path, 
        tone_color_converter, 
        vad=False
    )
    print(f"✅ Embedding extraído: {audio_name}")
    
    # Aplicar clonagem
    output_path = f'{output_dir}/output_melo_pt_clonado.wav'
    print(f"\n⏳ Aplicando clonagem de voz...")
    
    tone_color_converter.convert(
        audio_src_path=melo_base_path,
        src_se=source_se,
        tgt_se=target_se,
        output_path=output_path,
        message="@MyShell"
    )
    
    size_kb = os.path.getsize(output_path) / 1024
    print(f"✅ Áudio clonado gerado: {output_path} ({size_kb:.1f} KB)")
    print("\n🎉 SUCESSO! Clonagem com MeloTTS concluída!")
    
except ImportError:
    print("⚠️ MeloTTS não instalado")
except Exception as e:
    print(f"⚠️ Erro com MeloTTS: {e}")

# RESUMO
print("\n" + "=" * 60)
print("📊 RESUMO")
print("=" * 60)

print("\n✅ ToneColorConverter carregado")
print(f"✅ Embedding de referência extraído de: {reference_speaker}")
print(f"✅ Arquivos gerados em: {output_dir}/")

print("\n💡 Próximos passos:")
print("   1. Ouça os arquivos em outputs/")
print("   2. Para usar OpenAI: adicione créditos e execute novamente")
print("   3. Para usar MeloTTS: funciona agora com ES/JP")

print("\n🎉 Teste concluído!")

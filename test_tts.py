import os
from dotenv import load_dotenv
from openai import OpenAI
import sys

print("=" * 50)
print("TESTE DE TTS DA OPENAI")
print("=" * 50)

# 1. Carregar variáveis
os.chdir('/home/mateuus/projects/eopix/openvoice-server')
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# 2. Inicializar cliente
client = OpenAI(api_key=api_key)
print("✓ Cliente inicializado")

# 3. Testar TTS com texto muito curto
print("\nTestando geração de áudio TTS...")
try:
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input="Teste"  # Texto extremamente curto
    )
    print("✓ TTS funcionou!")
    print(f"Tipo de resposta: {type(response)}")
    
except Exception as e:
    print(f"\n✗ ERRO no TTS:")
    print(f"Tipo: {type(e).__name__}")
    print(f"Mensagem: {str(e)}")
    
    # Analisar erro específico
    if "429" in str(e) or "quota" in str(e).lower():
        print("\n⚠️  ERRO DE COTA:")
        print("- Você excedeu a cota da API OpenAI")
        print("- Verifique: https://platform.openai.com/account/usage")
        print("- Adicione créditos ou atualize o plano")
    elif "401" in str(e):
        print("\n⚠️  ERRO DE AUTENTICAÇÃO:")
        print("- Chave da API inválida")
        print("- Verifique se a chave está correta no .env")
    elif "403" in str(e):
        print("\n⚠️  ERRO DE PERMISSÃO:")
        print("- Você não tem permissão para usar este endpoint")
        print("- Verifique seu plano na OpenAI")
    else:
        print(f"\nDetalhes completos do erro:")
        if hasattr(e, 'status_code'):
            print(f"Status: {e.status_code}")
        if hasattr(e, 'body'):
            print(f"Body: {e.body}")
        if hasattr(e, 'response'):
            print(f"Response: {e.response}")

print("\n" + "=" * 50)


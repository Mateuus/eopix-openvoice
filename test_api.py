import os
from dotenv import load_dotenv
from openai import OpenAI
import sys

print("=" * 50)
print("TESTE DE CONEXÃO COM A API DA OPENAI")
print("=" * 50)

# 1. Verificar e mudar para o diretório correto
expected_dir = '/home/mateuus/projects/eopix/openvoice-server'
if os.getcwd() != expected_dir:
    print(f"Mudando diretório de {os.getcwd()} para {expected_dir}")
    os.chdir(expected_dir)
print(f"✓ Diretório atual: {os.getcwd()}")

# 2. Carregar variáveis de ambiente
print("\nCarregando variáveis de ambiente...")
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print("✗ ERRO: OPENAI_API_KEY não encontrada no arquivo .env.")
    print("Certifique-se de que o arquivo .env existe e contém 'OPENAI_API_KEY=sua_chave_aqui'.")
    sys.exit(1)
else:
    print(f"✓ OPENAI_API_KEY carregada (início: {api_key[:20]}...{api_key[-10:]})")

# 3. Inicializar cliente OpenAI
print("\nInicializando cliente OpenAI...")
try:
    client = OpenAI(api_key=api_key)
    print("✓ Cliente OpenAI inicializado com sucesso.")
except Exception as e:
    print(f"✗ ERRO ao inicializar OpenAI: {e}")
    sys.exit(1)

# 4. Fazer uma requisição de teste (ex: listar modelos)
print("\nFazendo uma requisição de teste (listando modelos)...")
try:
    models = client.models.list()
    print("✓ Requisição de teste bem-sucedida!")
    print(f"Número de modelos disponíveis: {len(models.data)}")
    print(f"Primeiros 3 modelos: {[m.id for m in models.data[:3]]}")
    print("\n✓ A API da OpenAI está configurada e funcionando corretamente.")
except Exception as e:
    print(f"✗ ERRO ao fazer requisição de teste: {e}")
    print(f"Tipo de erro: {type(e).__name__}")
    if hasattr(e, 'response'):
        print(f"Status: {e.response.status_code if hasattr(e.response, 'status_code') else 'N/A'}")
    if hasattr(e, 'body'):
        print(f"Detalhes: {e.body}")
    print("\nVerifique sua chave da API e sua conexão com a internet.")
    sys.exit(1)

print("\n" + "=" * 50)


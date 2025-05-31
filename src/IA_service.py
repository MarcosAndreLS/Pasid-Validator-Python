import time
from ollama import ChatResponse, Client
from requests.exceptions import RequestException

class IAService:
    def __init__(self):
        self.models = {
            "llama3.2": "llama3.2",
            "deep-seek": "DeepSeek-R1"
        }
        self.model = self.models["llama3.2"]
        self.client = None

        max_retries = 30
        retry_delay = 2  # segundos

        for attempt in range(max_retries):
            try:
                self.client = Client(host="http://ollama:11434")
                # Testa uma requisição leve para garantir conexão
                self.client.list()  # Verifica se Ollama está respondendo
                print(f"[IAService] Conectado ao Ollama com sucesso na tentativa {attempt+1}")
                break
            except Exception as e:
                print(f"[IAService] Tentativa {attempt+1}/{max_retries} falhou: {e}")
                time.sleep(retry_delay)
        else:
            raise RuntimeError("Não foi possível conectar ao Ollama após várias tentativas.")

    def ask(self, prompt: str) -> str:
        ia_response: ChatResponse = self.client.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return ia_response.message.content

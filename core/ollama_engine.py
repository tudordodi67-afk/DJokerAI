import requests
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"


class OllamaEngine:

    def __init__(self):

        try:
            prompt_path = Path("core/prompts/system.txt")

            self.system_prompt = prompt_path.read_text(
                encoding="utf-8"
            )

        except Exception:

            self.system_prompt = (
                "You are DJoker AI."
            )

    def ask(self, prompt: str):

        payload = {
            "model": MODEL,
            "prompt": prompt,
            "system": self.system_prompt,
            "stream": False,
            "options": {
                "temperature": 0.4,
                "num_predict": 300
            }
        }

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data["response"].strip()
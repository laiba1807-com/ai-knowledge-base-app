import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Settings:
	ollama_base_url: str = os.getenv("OLLAMA_BASE_URL=http://localhost:11434")
	embedding_model: str = os.getenv("EMBEDDING_MODEL=nomic-embed-text")
	llm_model: str = os.getenv("LLM_MODEL=llama3.2:1b")

def get_settings() -> Settings:
	return Settings()
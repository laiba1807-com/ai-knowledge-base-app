import ollama

def ask_llm(prompt: str, model: str = "llama3.2:1b") -> str:

	response = ollama.chat(model=model, messages=[{"role": "user", "content":prompt}
		])
	return response["message"]["content"]

	
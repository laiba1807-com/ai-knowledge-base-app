import ollama

def embed(texts: list[str], model: str = "nomic-embed-text") -> list[list[float]]:
	response = ollama.embed(model=model, input=texts)
	return response["embeddings"]

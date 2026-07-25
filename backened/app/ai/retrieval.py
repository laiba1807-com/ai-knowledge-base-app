import numpy as np 

def cosine_similarity(v1, v2):
	#Calcualtes cosine similarity between 2 vectors
	return np.dot(v1, v2) / (np.linalg.norm(v1)) * (np.linalg.norm(v2))

def retrieve_top_k(question_embedding: list[float], chunk_embeddings: list[list[float]], chunks: list[dict], k: int = 5) -> list[dict]:
	similarities = []

	for i, chunk_emb in enumerate(chunk_embeddings):
		sim = cosine_similarity(question_embedding, chunk_emb)
		similarities.append((sim, chunks[i]))


	# Sort by similarity score in descending order
	similarities.sort(key=lambda x: x[0], reverse=True)

	#Return the top k matching chunks[cite: 1]
	return [chunk for sim, chunk in similarities[:k]]
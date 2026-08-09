def build_prompt(question: str, retrieved_chunks: list[dict]) -> str:

	context_lines = []

	for i, chunk in enumerate(retrieved_chunks):
		line = f"[{i+1}] ({chunk['filename']} p.{chunk['page']}) {chunk['text']}"
		context_lines.append(line)


	context_lines = "\n".join(context_lines)

	prompt = f"""System: You answer strictly from the provided context. If the answer is not in the context, say you don't know. Cite sources as [filename p.N].
	Context: {context_lines}
	Question: {question}"""

	return prompt

from pypdf import PdfReader
import tiktoken
import os


def extract_pages(path: str) -> list[tuple[int, str]]:
	reader= PdfReader(path)
	return [(i+1, page.extract_text() or "") for i, page in enumerate(reader.pages)]


def chunk_text(pages: list[tuple[int, str]], filename: str, chunk_size: int = 500, overlap: int = 75) -> list[dict]:
	enc = tiktoken.get_encoding("cl100k_base")
	chunks = []


	for page_num, text in pages:
		tokens = enc.encode(text)
		i = 0
		while i < len(tokens):
			chunk_tokens = tokens[i:i + chunk_size]
			chunk_text = enc.decode(chunk_tokens)

			chunks.append({
				"filename": os.path.basename(filename),
				"page": page_num,
				"text": chunk_text
				})

			i = i + (chunk_size - overlap)

	return chunks
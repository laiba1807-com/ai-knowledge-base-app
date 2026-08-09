import sys
import os
import time


PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)
sys.path.insert(0, PROJECT_ROOT)


#import time
from app.ai.chunking import extract_pages, chunk_text
from app.ai.embeddings import embed
from app.ai.retrieval import retrieve_top_k
from app.ai.prompts import build_prompt
from app.ai.llm import ask_llm

def main():
    if len(sys.argv) < 2:
        print("Usage: python ask.py 'Your question here'")
        sys.exit(1)
        
    question = sys.argv[1]
    data_dir = "data"
    
    print("1. Reading and chunking PDFs...")
    all_chunks = []
    
    # Only process PDF files
    for filename in os.listdir(data_dir):
        if filename.endswith(".pdf"):
            filepath = os.path.join(data_dir, filename)
            pages = extract_pages(filepath)
            chunks = chunk_text(pages, filename, chunk_size=500, overlap=75)
            all_chunks.extend(chunks)
            
    print(f"   Created {len(all_chunks)} chunks total.")

    print("2. Embedding document chunks...")
    chunk_texts = [chunk["text"] for chunk in all_chunks]
    chunk_embeddings = embed(chunk_texts)
    
    print(f"3. Embedding user question: '{question}'...")
    question_vector = embed([question])[0]
    
    print("4. Retrieving relevant context...")
    top_chunks = retrieve_top_k(question_vector, chunk_embeddings, all_chunks, k=5)
    
    print("5. Generating answer...")
    start_time = time.time()
    prompt = build_prompt(question, top_chunks)
    answer = ask_llm(prompt)
    end_time = time.time()
    
    print("\n" + "="*50)
    print("ANSWER:")
    print("="*50)
    print(answer)
    print("="*50)
    print(f"Generation took: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()

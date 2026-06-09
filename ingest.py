import os
from sentence_transformers import SentenceTransformer
import chromadb

DOCUMENTS_DIR = "documents"
CHUNK_SIZE = 500
OVERLAP = 50

def load_documents():
    docs = []
    for filename in os.listdir(DOCUMENTS_DIR):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCUMENTS_DIR, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            docs.append({"filename": filename, "text": text})
    return docs

def clean_text(text):
    lines = text.splitlines()
    cleaned = []
    for line in lines:
        line = line.strip()
        if line:
            cleaned.append(line)
    return "\n".join(cleaned)

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def main():
    print("Loading documents...")
    docs = load_documents()
    print(f"Loaded {len(docs)} documents")

    model = SentenceTransformer("all-MiniLM-L6-v2")
    client = chromadb.PersistentClient(path="./chroma_db")
    
    try:
        client.delete_collection("professor_reviews")
    except:
        pass
    collection = client.create_collection("professor_reviews")

    all_chunks = []
    all_ids = []
    all_metadata = []

    for doc in docs:
        clean = clean_text(doc["text"])
        chunks = chunk_text(clean)
        for i, chunk in enumerate(chunks):
            if len(chunk.strip()) > 0:
                all_chunks.append(chunk)
                all_ids.append(f"{doc['filename']}_{i}")
                all_metadata.append({"source": doc["filename"]})

    print(f"Total chunks: {len(all_chunks)}")
    print("\n--- 5 SAMPLE CHUNKS ---")
    for i in range(min(5, len(all_chunks))):
        print(f"\nChunk {i} (source: {all_metadata[i]['source']}):")
        print(all_chunks[i])
        print("-" * 40)

    print("\nEmbedding and storing chunks...")
    embeddings = model.encode(all_chunks).tolist()
    collection.add(
        documents=all_chunks,
        embeddings=embeddings,
        ids=all_ids,
        metadatas=all_metadata
    )
    print("Done! All chunks stored in ChromaDB.")

if __name__ == "__main__":
    main()
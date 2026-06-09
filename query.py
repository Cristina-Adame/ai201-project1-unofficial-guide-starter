from sentence_transformers import SentenceTransformer
import chromadb
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("professor_reviews")
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def retrieve(query, k=6):
    query_embedding = model.encode([query]).tolist()[0]
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=["documents", "metadatas", "distances"]
    )
    chunks = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]
    return chunks, metadatas, distances

def ask(question):
    chunks, metadatas, distances = retrieve(question)
    
    context = ""
    for i, (chunk, meta) in enumerate(zip(chunks, metadatas)):
        professor = meta["source"].replace(".txt", "").replace("_", " ").title()
        context += f"[Source: {meta['source']} - {professor}]\n{chunk}\n\n"
    
    prompt = f"""You are a helpful assistant that answers questions about UT Austin CS professors based only on student reviews.

Answer the question using ONLY the information provided in the documents below.
If the documents do not contain enough information to answer the question, say "I don't have enough information on that."
Always cite which document(s) your answer comes from.

Documents:
{context}

Question: {question}

Answer:"""

    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    
    answer = response.choices[0].message.content
    sources = list(set(meta["source"] for meta in metadatas))
    
    return {"answer": answer, "sources": sources}

if __name__ == "__main__":
    test_questions = [
        "What do students say about Professor Gheith's lectures?",
        "Is Professor Young good for beginners?",
        "What do students say about Professor Ravishankar?"
    ]
    
    for q in test_questions:
        print(f"\nQuestion: {q}")
        result = ask(q)
        print(f"Answer: {result['answer']}")
        print(f"Sources: {result['sources']}")
        print("=" * 60)
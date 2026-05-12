"""
10. Build a chatbot for the Indian Penal Code. We'll start by downloading the official 
Indian Penal Code document, and then we'll create a chatbot that can interact with it. 
Users will be able to ask questions about the Indian Penal Code and have a conversation 
with it.

"""
from pypdf import PdfReader 
from sentence_transformers import SentenceTransformer 
import faiss 
import numpy as np 
from transformers import pipeline 
reader = PdfReader("IPCFile.pdf") 
text = "" 
for page in reader.pages: 
    text += page.extract_text() 
print("Text loaded successfully!") 
def split_text(text, chunk_size=500, overlap=50): 
    chunks = [] 
    start = 0 
    while start < len(text): 
        end = start + chunk_size 
        chunks.append(text[start:end]) 
        start += chunk_size - overlap 
    return chunks 
chunks = split_text(text) 
print("Total chunks:", len(chunks)) 
model = SentenceTransformer('all-MiniLM-L6-v2') 
embeddings = model.encode(chunks) 
dimension = embeddings.shape[1] 
index = faiss.IndexFlatL2(dimension) 
index.add(np.array(embeddings)) 
print("Faiss index created!") 
generator = pipeline("text2text-generation", model="google/flan-t5-base") 
def search(query, k=1): 
    query_vec = model.encode([query]) 
    distances, indices = index.search(np.array(query_vec), k) 
    results = [chunks[i] for i in indices[0]] 
    return "".join(results) 
def chatbot(query): 
    context = search(query) 
    prompt = f"""
Answer the question based on the context below:
Context:
{context}
Question:
{query}
""" 
    result = generator(prompt, max_length=300) 
    return result[0]['generated_text'] 
while True: 
    query = input("\nAsk your IPC question (type 'exit' to stop): ") 
    if query.lower() == "exit": 
        break 
    answer = chatbot(query) 
    print("\nAnswer:", answer)
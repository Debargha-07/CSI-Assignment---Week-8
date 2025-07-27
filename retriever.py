# retriever.py
import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

with open("docs/embedded_docs.pkl", "rb") as f:
    data = pickle.load(f)
    documents = data["docs"]
    embeddings = data["embeddings"]
    

embedding_dim = len(embeddings[0])
index = faiss.IndexFlatL2(embedding_dim)
index.add(np.array(embeddings))

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_top_docs(query, k=5):
    query_emb = model.encode([query])[0]
    D, I = index.search(np.array([query_emb]), k)
    top_docs = [documents[i] for i in I[0]]
    return top_docs, None

# prepare_docs.py
import pandas as pd
import pickle
import os
from utils import load_data, dataframe_to_docs
from sentence_transformers import SentenceTransformer

def save_data(docs, embeddings, df, output_path="docs/embedded_docs.pkl"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as f:
        pickle.dump({"docs": docs, "embeddings": embeddings, "df": df}, f)
    print(f"Saved {len(docs)} documents and DataFrame to {output_path}")

if __name__ == "__main__":
    df = load_data("data/training.csv")
    docs = dataframe_to_docs(df)

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(docs)

    save_data(docs, embeddings, df)

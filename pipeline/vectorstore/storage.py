import os
import json
from .config import collection, client
from .tokenizer import train_sentencepiece_from_embeddings
from .embedder import get_embedding

def add_embedding_to_chroma(embedding_file, float_id):
    """
    Read embedding JSON, tokenize, vectorize, and store in Chroma
    """
    sp = train_sentencepiece_from_embeddings(os.path.dirname(embedding_file))

    with open(embedding_file) as f:
        data = json.load(f)

    text = data["profile_summary"] + " " + str(data["variable_stats"])
    tokens = sp.encode(text, out_type=str)
    tokenized_text = " ".join(tokens)

    vector = get_embedding(tokenized_text)

    collection.add(
        ids=[str(float_id)],
        metadatas=[{"float_id": float_id}],
        documents=[tokenized_text],
        embeddings=[vector.tolist()]
    )
    client.persist()

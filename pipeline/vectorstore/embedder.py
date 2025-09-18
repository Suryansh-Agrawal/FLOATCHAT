from sentence_transformers import SentenceTransformer

# Load model once
MODEL = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    """
    Generate vector embedding for tokenized text
    """
    return MODEL.encode(text)

import os
import chromadb

OUTPUT_DIR = "data/output"
CHROMA_DIR = os.path.join(OUTPUT_DIR, "chroma")
SP_MODEL_PATH = os.path.join(OUTPUT_DIR, "spm.model")
SP_CORPUS_FILE = os.path.join(OUTPUT_DIR, "spm_corpus.txt")

# Ensure directories exist
os.makedirs(CHROMA_DIR, exist_ok=True)

# Initialize PersistentClient for Chroma
client = chromadb.PersistentClient(path=CHROMA_DIR)

# Create or get collection
collection = client.get_or_create_collection(name="argo_profiles")

import os
import sentencepiece as spm
from .config import SP_MODEL_PATH, SP_CORPUS_FILE, OUTPUT_DIR
import json

def train_sentencepiece_from_embeddings(embedding_dir):
    """
    Create a corpus from all embedding JSONs and train SentencePiece model
    """
    if os.path.exists(SP_MODEL_PATH):
        sp = spm.SentencePieceProcessor(model_file=SP_MODEL_PATH)
        return sp

    # Create corpus
    with open(SP_CORPUS_FILE, "w", encoding="utf-8") as f:
        for file in os.listdir(embedding_dir):
            if file.endswith(".json"):
                data = json.load(open(os.path.join(embedding_dir, file)))
                text = data["profile_summary"] + " " + str(data["variable_stats"])
                f.write(text + "\n")

    spm.SentencePieceTrainer.Train(
        f"--input={SP_CORPUS_FILE} --model_prefix={os.path.join(OUTPUT_DIR,'spm')} --vocab_size=8000"
    )
    sp = spm.SentencePieceProcessor(model_file=SP_MODEL_PATH)
    return sp

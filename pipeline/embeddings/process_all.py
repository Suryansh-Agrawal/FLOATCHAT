import os
import json
from .content import create_embedding_content

def create_embedding_for_ds(ds, float_id, output_dir="output/embeddings"):
    """
    Create embedding JSON for a single Dataset.
    """
    os.makedirs(output_dir, exist_ok=True)
    content = create_embedding_content(ds)
    out_file = os.path.join(output_dir, f"{float_id}_embedding.json")
    with open(out_file, "w") as f:
        json.dump(content, f, indent=2)
    print(f"[INFO] Saved embedding for float {float_id} -> {out_file}")
    return out_file

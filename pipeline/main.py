from fetcher import load_netcdf
from qc import apply_qc
from transform import flatten, compute_derived
from save import save_parquet, save_metadata_sqlite
from embeddings.process_all import create_embedding_for_ds
from vectorstore.storage import add_embedding_to_chroma
import pandas as pd
import os

# Define output directories directly
OUTPUT_DIR = "data/output"
PROCESSED_DIR = os.path.join(OUTPUT_DIR, "processed")
EMBEDDING_DIR = os.path.join(OUTPUT_DIR, "embeddings")

def main():
    # 1. Load raw NetCDF
    filepath = "data/raw/edata.nc"
    ds = load_netcdf(filepath)
    print(ds)

    # 2. Apply QC
    ds = apply_qc(ds, var_name='sea_level_1', qc_var_name='sea_level_quality_flag_1')
    print("Quality control applied")

    # 3. Flatten to tidy table
    df = flatten(ds, 'sea_level_1_clean')

    # 4. Compute derived fields
    df = compute_derived(df)

    # 5. Save partitioned Parquet
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    save_parquet(df, PROCESSED_DIR, partition_cols=['latitude','longitude'])

    # 6. Extract metadata (example: float info, lat/lon, QC summary)
    float_id = getattr(ds, "PLATFORM_NUMBER", 1)  # Use actual float ID if available
    df_metadata = pd.DataFrame({
        'float_id': [float_id],
        'latitude': [float(ds.latitude.values[0])],
        'longitude': [float(ds.longitude.values[0])],
        'qc_summary': [df['sea_level_1_clean'].isna().sum()]
    })

    # 7. Save metadata to SQLite
    save_metadata_sqlite(df_metadata)

    # 8. Generate embedding content
    os.makedirs(EMBEDDING_DIR, exist_ok=True)
    embedding_file = create_embedding_for_ds(ds, float_id=float_id, output_dir=EMBEDDING_DIR)
    print(f"[INFO] Embedding saved for float {float_id}")

    # --- Add embedding to Chroma ---
    add_embedding_to_chroma(embedding_file, float_id)
    print(f"[INFO] Embedding stored in Chroma for float {float_id}")

if __name__ == "__main__":
    main()

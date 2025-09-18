import os

def save_parquet(df, output_dir, partition_cols=None):
    """
    Save DataFrame as partitioned Parquet files.
    """
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "sea_level.parquet")
    df.to_parquet(path, partition_cols=partition_cols, index=False)
    print(f"Saved partitioned Parquet at {path}")

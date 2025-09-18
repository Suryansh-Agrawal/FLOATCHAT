import os
import pandas as pd
import sqlite3

def save_parquet(df, output_dir, partition_cols=None):
    """
    Save DataFrame as partitioned Parquet files.
    """
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "sea_level.parquet")
    df.to_parquet(path, partition_cols=partition_cols, index=False)
    print(f"Saved partitioned Parquet at {path}")

def save_metadata_sqlite(df_metadata, db_path="data/processed/argo_metadata.db", table_name="floats"):
    """
    Save float metadata to SQLite database.
    """
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    df_metadata.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Metadata saved in SQLite DB at {db_path}, table: {table_name}")

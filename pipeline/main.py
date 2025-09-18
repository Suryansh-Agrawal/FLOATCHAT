from fetcher import load_netcdf
from qc import apply_qc
from transform import flatten, compute_derived
from save import save_parquet

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
    save_parquet(df, "data/processed", partition_cols=['latitude','longitude'])

if __name__ == "__main__":
    main()

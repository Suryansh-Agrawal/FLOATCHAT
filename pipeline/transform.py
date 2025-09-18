import pandas as pd

def flatten(ds, var_name):
    """Flatten 3D xarray variable into tidy DataFrame."""
    df = ds[var_name].to_dataframe().reset_index()
    return df

def compute_derived(df):
    """
    Compute derived fields if needed.
    Example: sea level anomaly from mean, or simple rolling averages.
    """
    df['sea_level_anomaly'] = df['sea_level_1_clean'] - df['sea_level_1_clean'].mean()
    return df

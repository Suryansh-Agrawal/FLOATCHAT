import numpy as np

def apply_qc(ds, var_name, qc_var_name, bad_flags=None, interpolate=True):
    """
    Apply QC to a variable and optionally interpolate missing values.
    
    Args:
        ds: xarray.Dataset
        var_name: variable to QC (e.g., 'sea_level_1')
        qc_var_name: QC variable (e.g., 'sea_level_quality_flag_1')
        bad_flags: list of flags to treat as bad
        interpolate: whether to interpolate missing values
    Returns:
        ds: xarray.Dataset with cleaned variable
    """
    if bad_flags is None:
        bad_flags = ['R','S','T','U','W','X']
    
    qc_flags = ds[qc_var_name].astype(str)
    good_mask = ~np.isin(qc_flags, bad_flags)
    var_clean = ds[var_name].where(good_mask)
    
    if interpolate:
        var_clean = var_clean.interpolate_na(dim='time', method='linear')
    
    clean_name = f"{var_name}_clean"
    ds[clean_name] = var_clean
    return ds

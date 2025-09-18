import xarray as xr

def load_netcdf(filepath: str):
    """Load local NetCDF file into xarray."""
    ds = xr.open_dataset(filepath)
    return ds

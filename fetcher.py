import xarray as xr

def load_netcdf_xarray(filepath: str):
    """Load a local NetCDF file into an xarray Dataset."""
    ds = xr.open_dataset(filepath)
    return ds
from fetcher import load_netcdf_xarray

def main():

    filepath = "data/raw/edata.nc" 
    print("Loading local NetCDF file with xarray...")
    ds = load_netcdf_xarray(filepath)
    print(ds)


if __name__ == "__main__":
    main()
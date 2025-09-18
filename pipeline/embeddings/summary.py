def create_profile_summary(ds):
    """
    Create a short 1-3 sentence summary of a float/profile dataset.
    Works with any available variables; does not assume LAT/LON.
    """
    if ds is None:
        return ""

    float_id = getattr(ds, "PLATFORM_NUMBER", "unknown")
    
    # Pick first numeric variable as latitude/longitude proxy if exists
    lat, lon = 0.0, 0.0
    numeric_vars = [v for v in ds.data_vars if ds[v].dtype.kind in "fi"]
    if len(numeric_vars) >= 2:
        try:
            lat = float(ds[numeric_vars[0]].values[0])
            lon = float(ds[numeric_vars[1]].values[0])
        except Exception:
            pass

    n_profiles = ds.dims.get("N_PROF", ds.dims.get("profile", 0))

    # Detect BGC sensors if present
    bgc_sensors = [var for var in ds.data_vars if var.upper() in ["DOXY", "NITRATE", "CHLA", "BBP"]]

    summary = f"Float {float_id} near {lat:.2f}°N {lon:.2f}°E, {n_profiles} profiles; "
    summary += f"BGC sensors present: {', '.join(bgc_sensors)}." if bgc_sensors else "No BGC sensors reported."

    return summary

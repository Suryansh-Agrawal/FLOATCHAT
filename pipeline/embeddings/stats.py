import pandas as pd
import numpy as np

def compute_variable_stats(ds):
    """
    Compute min, max, mean, std, and flagged anomalies per numeric variable.
    Non-numeric variables are skipped.
    """
    stats = {}
    if ds is None:
        return stats

    for var in ds.data_vars:
        # Only numeric types
        if ds[var].dtype.kind not in "fiu":  # float, int, unsigned int
            continue

        data = ds[var].values.flatten()
        data = data[~pd.isnull(data)]  # remove NaNs

        if len(data) == 0:
            continue

        stats[var] = {
            "min": float(np.min(data)),
            "max": float(np.max(data)),
            "mean": float(np.mean(data)),
            "std": float(np.std(data)),
            "flagged_anomalies": int(np.sum((data < data.mean() - 3*data.std()) |
                                            (data > data.mean() + 3*data.std())))
        }

    return stats

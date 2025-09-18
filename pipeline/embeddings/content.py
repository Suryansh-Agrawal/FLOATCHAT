from .summary import create_profile_summary
from .stats import compute_variable_stats

def create_embedding_content(ds):
    """
    Combine profile summary and variable statistics into a single dictionary.
    """
    return {
        "profile_summary": create_profile_summary(ds),
        "variable_stats": compute_variable_stats(ds)
    }

from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x = np.asarray(x, dtype=float)
    counts = Counter(x.tolist())
    max_c = max(counts.values())
    mode = min(value for value, count in counts.items() if count == max_c)
    return {'mean': float(np.mean(x)), 
            'median': float(np.median(x)),
            'mode': float(mode)
           }
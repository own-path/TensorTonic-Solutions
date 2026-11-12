import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    X = np.asarray(x)
    Y = np.asarray(y)

    return float(np.sum(np.abs(X-Y)))
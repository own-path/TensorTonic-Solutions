import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    X = np.asarray(x)
    Y = np.asarray(y)

    return float(np.sqrt(np.sum((X - Y)**2)))
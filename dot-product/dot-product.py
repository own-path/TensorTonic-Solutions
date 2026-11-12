import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    X = np.asarray(x)
    Y = np.asarray(y)
    return float(X @ Y)
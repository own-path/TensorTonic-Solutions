import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    A = np.asarray(a, dtype=float)
    B = np.asarray(b, dtype=float)

    L_a_norm = np.sqrt(np.sum(A**2))
    L_b_norm = np.sqrt(np.sum(B**2))

    if L_a_norm == 0 or L_b_norm == 0:
        return float(0)
    else:
        return float(( A @ B ) / (L_a_norm * L_b_norm ))
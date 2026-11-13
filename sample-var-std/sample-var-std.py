import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x = np.asarray(x, dtype=float)
    x_bar = np.mean(x)

    std = (1/(len(x)-1))* np.sum((x-x_bar)**2)
    return {'variance': float(std), 
            'standard_deviation': float(np.sqrt(std))
    }
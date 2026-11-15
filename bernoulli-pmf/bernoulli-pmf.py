import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    x = np.asarray(x, dtype=float)
    pmf =np.asarray([ 1 - p  if i==0 else p for i in x  ])

    return {'pmf': pmf,
            'mean': float(p),
            'variance': float(p*(1-p))
    }
    
    
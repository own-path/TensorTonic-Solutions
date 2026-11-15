import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """

    rng = np.random.default_rng(seed)
    
    samples = rng.choice(x, size=(n_bootstrap, len(x)), replace=True)
    means = samples.mean(axis=1)
    
    alpha = 1 - ci
    lower, upper = np.percentile(
        means,
        [100 * alpha / 2, 100 * (1 - alpha / 2)]
    )
    
    result = {
        "bootstrap_mean": float(means.mean()),
        "lower": float(lower),
        "upper": float(upper)
    }

    return result
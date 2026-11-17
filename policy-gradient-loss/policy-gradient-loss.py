import numpy as np
def policy_gradient_loss(log_probs: list, rewards: list, gamma: float) -> float:
    """
    Returns the REINFORCE loss with a mean-return baseline.
    """

    log_probs = np.asarray(log_probs, dtype=float)
    rewards   = np.asarray(rewards, dtype=float)

    T = len(rewards)
    G = np.asarray([0.0] * T)

    G[T-1] = rewards[T-1]

    for t in range(T-2, -1,-1):
        G[t] = rewards[t] + gamma * G[t+1]
        
    meanG = G.mean()
    adv = [g - meanG for g in G]

    return -sum(lp * ad for lp, ad in zip(log_probs,adv)) / T
    
    
import numpy as np
from numpy.typing import ArrayLike

def payoff_forward(ST,K):
    '''
    Forward terminal payoff.
    
    Parameters
    --------------------
    ST : array-like
        Terminal underlying price(s).
    K : float
        Delivery price.
    
    Returns
    --------------------
    np.ndarray:
        Payoff values : ST - K.
    '''
    ST = np.array(ST, dtype=float)
    payoff = ST - K
    return payoff

def payoff_call(ST, K):
    '''
    European call terminal payoff.
    
    Parameters
    --------------------
    ST : array-like
        Terminal underlying price(s).
    K : float
        Strike price.
    
    Returns
    --------------------
    np.ndarray:
        Payoff values : max(ST - K,0).    
    '''
    ST = np.array(ST, dtype=float)
    payoff = np.maximum(ST - K, 0.0)
    return payoff

def payoff_put(ST, K):
    '''
    European put terminal payoff.

    Parameters
    --------------------
    ST : array-like
        Terminal underlying price(s).
    K : float
        Strike price.

    Returns
    --------------------
    np.ndarray:
        Payoff values: max(K - ST,0).
    '''
    ST = np.array(ST, dtype=float)
    payoff = np.maximum(K - ST, 0.0)
    return payoff
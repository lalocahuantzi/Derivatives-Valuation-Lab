import numpy as np

def discount_factor(r, T):
    '''
    Computes the discout factor under continuous compounding.

    Parameters
    --------------------
    r: float
        Continuously compounded risk-free rate.
    T: float
        Time to maturity in years.

    Returns
    --------------------
    float:
        Discount factor exp(-r*T)
    '''
    if T < 0:
        raise ValueError("T must be non-negative.")
    
    discf = np.exp(-r*T)
    return float(discf)
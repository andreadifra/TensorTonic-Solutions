import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x, p = np.array(x), np.array(p)

    if not (x.shape == p.shape):
        raise ValueError("Shapes of s and o must match")
    
    if not np.isclose(np.sum(p), 1, rtol=1e-06):
        raise ValueError("Expected value doesn't equal 1")
    
    return np.sum(x*p)

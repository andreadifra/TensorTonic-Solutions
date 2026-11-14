import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    x = np.asarray(x, float)
    y = np.asarray(y, float)

    return float(x.dot(y))
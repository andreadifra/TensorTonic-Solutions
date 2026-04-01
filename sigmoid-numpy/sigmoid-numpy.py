import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    vec = np.vectorize( lambda x: 1/(1+np.exp(-1*x)))
    return vec(x)
    
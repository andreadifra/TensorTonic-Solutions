import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    # Set initial values to 0
    ## Need to fix shape of W
    W = np.zeros(X.shape[1])
    b = 0

    for i in range(steps):
        # Linear predictor
        z = X@W + b 
        # wrap in sigmoid - calculate probability
        p = _sigmoid(z)
        
        # Calculate the loss
        L = -1/len(y) * (y*np.log(p) + (1-y)*np.log(1-p))
        
        # Derivatives 
        dLdw = X.T@(p - y)*(1/len(y))
        dLdb = np.mean(p-y)
        
        # Update gradients 
        W -= lr*dLdw
        b -= lr*dLdb
    
    return W, b
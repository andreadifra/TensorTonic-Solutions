import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    X, y = np.array(X), np.array(y)
    # Initialise weights & bias at zero 
    W = np.zeros(X.shape[1])
    b = 0 

    for i in range(steps):
        # Sigmoid activation
        p = _sigmoid(X@W.T + b)
        
        # Calculate gradients
        dW = (X.T@(p - y))/len(y)
        db = np.mean(p - y)
    
        # Gradient descent
        W = W - lr*dW
        b = b - lr*db
    
    return W, b
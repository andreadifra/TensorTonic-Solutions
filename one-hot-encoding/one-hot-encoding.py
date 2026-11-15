import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    if num_classes is None:
        # Infer class size
        num_classes = max(y) + 1

    # Initialise array
    X = np.zeros((len(y),num_classes))

    for i, j in enumerate(y):
        X[i, j] = 1

    return X
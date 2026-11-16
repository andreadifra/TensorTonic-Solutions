import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a, b = np.array(a), np.array(b)
    anorm = np.sqrt(a@a)
    bnorm = np.sqrt(b@b)

    if anorm == 0.0 or bnorm == 0.0:
        return 0.0
    else:
        return float(np.dot(a, b) / (anorm * bnorm))
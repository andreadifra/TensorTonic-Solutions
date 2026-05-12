import numpy as np

def matrix_transpose(A):
    """
    Returns: ndarray, the transpose of A.
    """
    A = np.array(A)
    n, m = A.shape
    T = np.zeros((m, n), dtype = A.dtype)

    for i in range(n):
        for j in range(m):
            T[j, i] = A[i, j]
    
    return T
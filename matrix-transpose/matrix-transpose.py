import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    A_t = np.zeros(np.shape(A)[::-1])
    
    for i, row in enumerate(A):
        for j, value in enumerate(row):
            A_t[j, i] = value 

    return A_t

import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    unique, counts = np.unique(y, return_counts=True)
    props = counts / counts.sum()
    entropy = - (props * np.log2(props)).sum()
    return entropy
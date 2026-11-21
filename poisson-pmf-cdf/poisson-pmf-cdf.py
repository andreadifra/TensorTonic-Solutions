import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    pmf = math.exp(-lam)
    cdf = pmf

    for i in range(1, k+1):
        pmf *= lam/i
        cdf += pmf
        
    return {
        "pmf": float(pmf),
        "cdf": float(cdf)
    }
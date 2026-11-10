import numpy as np

def exponential_distribution(x: list, lam: float) -> dict:
    """
    Compute exponential distribution properties.
    
    Args:
        x: Points at which to evaluate PDF and CDF
        lam: Rate parameter (lambda) of the distribution
        
    Returns:
        Dictionary with 'pdf', 'cdf', 'mean', and 'variance' keys
    """
    # Your code here
    if lam <= 0:
        return dict.fromkeys(
            ["pdf", "cdf", "mean", "variance"],
            None
        )
    X = np.asarray(x)
    result = {'pdf':np.where(X>= 0, np.round(lam*np.exp(-lam* X),4), 0).tolist(), 
                'cdf': np.where(X>= 0,np.round(1 - np.exp(-lam*X),4), 0).tolist(),
                'mean': np.round(1/lam,4),
                'variance': np.round(1/(lam**2),4)
                }
    return result
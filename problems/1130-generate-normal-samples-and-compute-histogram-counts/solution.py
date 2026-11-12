import numpy as np

def fn(seed, mean, std, n, bins):
    # return (counts, edges) as plain Python lists
    np.random.seed(seed)
    s =np.random.normal(loc=mean, scale=std, size=n)
    return np.histogram(s, bins=bins)

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    pass
    freq = {}
    n = len(samples)
    for num in samples:
        freq[num] = freq.get(num, 0) + 1
    
    result = [(key, val/n) for key, val in freq.items()]
    return result


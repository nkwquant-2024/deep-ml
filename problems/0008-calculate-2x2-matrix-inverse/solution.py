def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    #entries = [i for j in matrix for i in j]
    #a,b,c,d = entries[0], entries[1] , entries[2] ,entries[3]
    [[a, b], [c, d]] = matrix
    det = a*d - c*b 
    if det == 0:
        return None
    else:
        k = 1/det
        flipped_mat = [[d,-b],[-c,a]]
        return [[i * k for i in row] for row in flipped_mat]
    

    
    pass
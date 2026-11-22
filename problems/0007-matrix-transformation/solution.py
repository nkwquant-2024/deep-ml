import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    try:
        inverseT = np.linalg.inv(T)
        inverseS = np.linalg.inv(S)
    except np.linalg.LinAlgError:
        return -1
    transformed_matrix = np.dot(np.dot(inverseT, A), S)
    return transformed_matrix
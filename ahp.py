import numpy as np

def ahp_weights(matrix):
    matrix = np.array(matrix)
    col_sum = matrix.sum(axis=0)
    norm_matrix = matrix / col_sum
    weights = norm_matrix.mean(axis=1)
    return weights

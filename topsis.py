import numpy as np

def topsis(data, weights, impacts):
    data = np.array(data, dtype=float)
    norm = data / np.sqrt((data**2).sum(axis=0))
    weighted = norm * weights

    ideal_pos = np.max(weighted, axis=0)
    ideal_neg = np.min(weighted, axis=0)

    for i in range(len(impacts)):
        if impacts[i] == 'cost':
            ideal_pos[i], ideal_neg[i] = ideal_neg[i], ideal_pos[i]

    d_pos = np.sqrt(((weighted - ideal_pos)**2).sum(axis=1))
    d_neg = np.sqrt(((weighted - ideal_neg)**2).sum(axis=1))

    score = d_neg / (d_pos + d_neg)
    return score

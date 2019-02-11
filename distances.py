"""distances.py

An utility modules about distances
"""

import numpy as np


def distance(x, y):
    assert len(x) == len(y)
    assert len(x) > 0 and len(y) > 0
    return np.sqrt(np.sum((np.array(x)-np.array(y)) ** 2))

def get_distances(x, X):
    return [distance(np.array(x), _) for _ in X]

def get_k_closest(lst, K=1):
    return np.argsort(np.array(lst))[:K]
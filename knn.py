"""
An implementation of K-Nearest Neighbors
"""

from .distances import get_k_closest, get_distances, distance
from collections import Counter

class KNN:
    """Class KNN
    """
    def __init__(self, K=1):
        self.K = K

    def fit(self, X, y):
        """Fit function
        """
        self.X = X
        self.y = y

    def _predict_for_x(self, x):
        """predict_for_x function
        """
        lst_distances = get_distances(x, self.X)
        lst_knn = get_k_closest(lst_distances, self.K)
        predict = [self.y[i] for i in lst_knn]
        prediction = max(predict, key=Counter(predict).get)
        return prediction
        

    def predict(self, X):
        """predict function
        """
        predict_lst = [self._predict_for_x(e) for e in X]
        return predict_lst

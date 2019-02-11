from .knn import KNN
from .metrics import accuracy_score

from vivadata.datasets import load_iris


X, y = load_iris(version='petal')

print(X.shape, y.shape)

# y_test = y
# knn = KNN()
# knn.fit(X, y)
# y_pred = knn.predict(y_test, K=1)
# acc = accuracy_score(y, y_test)
# print(acc)
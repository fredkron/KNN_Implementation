# KNN_implementation

In pattern recognition, the k-nearest neighbors algorithm (k-NN) is a non-parametric method used for classification and regression. In both cases, the input consists of the k closest training examples in the feature space. The output depends on whether k-NN is used for classification or regression:

        In k-NN classification, the output is a class membership. An object is classified by a plurality vote of its neighbors, with the object being assigned to the class most common among its k nearest neighbors (k is a positive integer, typically small). If k = 1, then the object is simply assigned to the class of that single nearest neighbor.

        In k-NN regression, the output is the property value for the object. This value is the average of the values of its k nearest neighbors.

More informations here: https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm

### `distance`
This function compute the [euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) between 2 points.
It takes 2 positional arguments, `x` and `y` and return the euclidean distance between them.
`x` and `y` are vector-like/sequence-like and the function should return a float.

### `get_distances`
This function takes a 2 positional arguments, `x` and `X`.
`x` should be vector like while `X` should be an array of vectors with same dimensions as `x`.
The function should return the list of distances between `x` and each vector of `X`.

### `get_k_closest`
This function takes a list of distances (for example, the return value of `get_distances`) as positional parameter, and a keyword argument `K`.
It should return the indices of the K closest distances within the list.


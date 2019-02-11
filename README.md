# KNN_implementation

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


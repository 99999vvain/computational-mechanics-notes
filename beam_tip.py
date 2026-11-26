"""Exact endpoint observations for equal-length Euler--Bernoulli segments."""
from fractions import Fraction as Q
from itertools import permutations

import numpy as np


def observation(n):
    """Integrate (1-x)^p on each segment, in clamp-to-tip order."""
    edges = [Q(i, n) for i in range(n + 1)]
    return np.array([
        [((1-left)**(p+1) - (1-right)**(p+1)) / (p+1)
         for left, right in zip(edges, edges[1:])]
        for p in (2, 1, 0)
    ], dtype=object)


def det3(matrix):
    total = 0
    for i, j, k in permutations(range(3)):
        inversions = int(i > j) + int(i > k) + int(j > k)
        total += (-1)**inversions * matrix[0, i] * matrix[1, j] * matrix[2, k]
    return total


def show(vector):
    return ", ".join(map(str, vector))


def main():
    a3 = observation(3)
    det = det3(a3)
    flex = np.array([1, 2, 3], dtype=object)
    data = a3 @ flex
    recovered = []
    for col in range(3):
        augmented = a3.copy()
        augmented[:, col] = data
        recovered.append(det3(augmented) / det)
    assert det == Q(2, 729) and recovered == list(flex)
    print("3 segments: det =", det, " observations =", show(data))
    print("recovered EI =", show([1 / q for q in recovered]))

    matrix = a3.astype(float)
    error = np.array([0.001, 0, 0])
    print("cond_2 =", np.linalg.cond(matrix))
    print("parameter change for moment-data error", error, "=", np.linalg.solve(matrix, error))

    a4 = observation(4)
    direction = np.array([1, -3, 3, -1])
    assert all(a4 @ direction == 0)
    for q in (np.full(4, Q(1)), 1 + Q(1, 4)*direction):
        coeff = a4 @ q
        assert min(q) > 0 and list(coeff) == [Q(1, 3), Q(1, 2), Q(1)]
        print("4 segments: EI =", show([1 / v for v in q]), " observations =", show(coeff))


if __name__ == "__main__":
    main()

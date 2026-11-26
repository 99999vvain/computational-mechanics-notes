"""Exact characteristic polynomials in the centered coordinate y=lambda-2."""
from fractions import Fraction as Q
from math import sqrt

import numpy as np


def stiffness(k):
    a, b, c, d = k
    return np.array([[a+b, -b, 0], [-b, b+c, -c], [0, -c, c+d]])


def main():
    s = Q(1, 2)
    t_squared = s*s / 2
    # A has centered diagonal (s,0,-s) and two unit inner springs.
    # B has centered diagonal zero and inner springs 1+t and 1-t.
    # The constant coefficients cancel for both configurations.
    gap_a = s*s + 2
    gap_b = 2*(1 + t_squared)
    assert gap_a == gap_b
    # Expand (lambda-2)^3 - gap*(lambda-2) in descending powers.
    coefficients = (1, -6, 12-gap_a, -8+2*gap_a)
    assert coefficients == (1, -6, Q(39, 4), -Q(7, 2))
    print("det(lambda I-K):", ", ".join(map(str, coefficients)))

    t = sqrt(t_squared)
    configs = [(1+float(s), 1, 1, 1-float(s)), (1-t, 1+t, 1-t, 1+t)]
    exact_spectrum = [2-sqrt(gap_a), 2, 2+sqrt(gap_a)]
    for k in configs:
        assert min(k) > 0 and abs(sum(k)-4) < 1e-14
        eigenvalues = np.linalg.eigvalsh(stiffness(k))
        np.testing.assert_allclose(eigenvalues, exact_spectrum, rtol=0, atol=1e-13)
        print("k =", k)
        print("  lambda =", eigenvalues, " omega =", np.sqrt(eigenvalues))


if __name__ == "__main__":
    main()

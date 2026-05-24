import numpy as np
import time

np.random.seed(50)
A = np.random.randn(100, 100)
B = np.random.randn(100, 100)

def matmul(X, Y):
    """Multiplies two matrices X and Y O(n^3)"""
    a, b = X.shape
    c, d = Y.shape
    assert c == r2, f"Incompatible shapes for multiplication {X.shape} and {Y.shape}"
    out = np.zeros((a, d))
    for i in range(a):
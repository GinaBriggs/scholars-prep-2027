import numpy as np
import time

np.random.seed(50)
A = np.random.randn(100, 100)
B = np.random.randn(100, 100)

def matmul_mine(X, Y):
    """Multiplies two matrices X and Y O(n^3)"""
    a, b = X.shape
    c, d = Y.shape
    assert c == b, f"Incompatible shapes for multiplication {X.shape} and {Y.shape}"
    out = np.zeros((a, d))
    for i in range(a):
        for j in range(d):
            for k in range(b):
                out[i, j] += X[i, k] * Y[k, j]
    return out

t0 = time.perf_counter()
C_mine = matmul_mine(A, B)
t_mine = time.perf_counter() - t0

t0 = time.perf_counter()
C_numpy = A @ B
t_numpy = time.perf_counter() - t0

# No error because the results are close enough, but if they were not, an AssertionError would be raised with the message
# You can test my changing a in for i in range(a) to a-1
assert np.allclose(C_mine, C_numpy), "The results are not close enough!" 
#print(f"mine = {C_mine}")
#print(f"NumPy = {C_numpy}")

print(f"My implementation took {t_mine:.4f} seconds")
print(f"NumPy implementation took {t_numpy:.4f} seconds")
print(f"NumPy is {t_mine / t_numpy:.2f} times faster than my implementation")

"""On Day 1, 
I wrote a basic matrix multiplication script from scratch, 
timed it and proved my code works correctly by checking it against NumPy's built in multiplier. 
I've seen that my implementation is significantly slower than NumPy's, 
which is expected since NumPy uses highly optimized libraries under the hood. 
This exercise was a good reminder of the importance of using efficient algorithms and 
libraries for computational tasks."""
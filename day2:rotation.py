# 1. Define rotate(theta) -> 2x2 NumPy array
import numpy as np
import matplotlib.pyplot as plt

def rotate(theta):
    R = np.array([[np.cos(theta), -np.sin(theta)] , [np.sin(theta), np.cos(theta)]])
    return R

# 2. Define a random 2D vector v with seed 42
np.random.seed(42)
v = np.array([1.0, 0.0])

# 3. Pick three angles: 0, pi/4, pi/2 
# 4. For each angle, compute rotated v and PRINT both vectors
fig, ax = plt.subplots(figsize=(5, 4))
ax.grid(True)
ax.set_xlabel('X Axis', fontsize=10)
ax.set_ylabel('Y Axis', fontsize=10)
angle = np.radians([0, 45, 90])
for x in angle:
    v_rot = rotate(x) @ v
    R = rotate(x)
    print(f"{v_rot} and {v_rot}")

    if x == 0:
        w ='red'
    elif x == np.radians(45):
        w = 'green'
    else:
        w = 'blue'

    ax.quiver([0], [0], v_rot[0], v_rot[1], angles='xy', scale_units='xy', scale=1, color=w, label=f'{np.degrees(x):.0f}°')
ax.legend()
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')

I = np.array([[1 , 0] , [0 , 1]])

assert np.allclose(R @ R.T, I), "The matrices do not equal the identity matrix!"
assert np.allclose(np.linalg.det(R), 1.0), "The area is not preserved under this transformation!"

# 7. Matplotlib: plot original v as one arrow, rotated v as another, on the same axes
#    Use plt.quiver or plt.arrow. Set xlim/ylim symmetric. Add a grid.

# Set symmetric x and y limits ax.set_xlim(-limit, limit) ax.set_ylim(-limit, limit) # Add a grid for readability ax.grid(True)

plt.show()
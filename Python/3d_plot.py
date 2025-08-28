import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 10)
y = np.linspace(-3, 3, 10)

X, Y = np.meshgrid(x, y)

Z = np.sqrt(np.maximum(0, Y**2 - X**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(X, Y, Z)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D plot of sqrt(y^2 - x^2)")

plt.show()

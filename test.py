import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(100,1)
y = np.random.randn(100,1)

plt.scatter(x,y, 'r', fontsize=14)
plt.title("散布図")
plt.xlabel("x")
plt.ylabel("y")

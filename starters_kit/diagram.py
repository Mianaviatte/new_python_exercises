import matplotlib as mpl
from matplotlib import lines
import matplotlib.pyplot as plt
import numpy as np
import random

# Constructor of a table
fig, ax=plt.subplots(figsize=(10, 5))
layout='constrained'
ax.set_xlabel('X matplot')
ax.set_ylabel('Y matplot')
ax.set_title('MatPlotLib')
ax.legend()

# Dots with random data
x = []
y = []

for i in range(10):
    a = random.randint(1,9)
    b = random.randint(0,5)
    
    x.append(a)
    y.append(b)

ax.plot([x], [y], color='green', marker='o', )

# lines with set data
z = [9, 3, 7, 5, 2, 6]
q = np.array([[1, 3], [2, 1], [5, 2], [3, 3], [2, 5], [3, 1]])
ax.plot(z, q)

plt.show(block=True)
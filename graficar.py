import numpy as np
import matplotlib.pyplot as plt

ficheroCodigos = open("reward2.txt")
data = ficheroCodigos.readlines()
matrix = np.loadtxt(data, delimiter=" ",  dtype='int')
index = matrix[:, 0]
reward =  matrix[:, 1]
ax =plt.gca()
ax.set_xlim([np.min(index), np.max(index)])
ax.set_ylim([np.min(reward), np.max(reward)])
plt.grid(True)
plt.plot(index, reward)
plt.show()

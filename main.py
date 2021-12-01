import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 15)
y = np.random.random_sample(15)
xerr = np.random.random_sample(15) / 10
yerr = np.random.random_sample(15) / 10

plt.figure()
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='o-', ecolor='red')
plt.show()
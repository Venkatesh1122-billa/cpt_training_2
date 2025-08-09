import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)
theta = np.linspace(0, 6*np.pi, 800)
r = np.linspace(0, 50, 800) + np.random.normal(0,2,800)
z = np.linspace(-10,10,800)
x = r *np.cos(theta)
y = r *np.sin(theta)

r_value, p_value = pearsonr(x, y)
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111,projection = '3d')
sc = ax.scatter(x,y, c = theta , cmap = 'plasma', s = 5, alpha = 0.8)
plt.title(f"Pearson plotr ={r_value:.3f}", fontsize = 15)
# plt.axis('Circular ratio')
plt.colorbar(sc, ax = ax, label = "Angle theta ")
plt.show()


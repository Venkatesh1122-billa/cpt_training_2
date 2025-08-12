import numpy as np
import matplotlib.pyplot as plt
def get_r(theta, rho):
    abs_cos = np.abs(np.cos(theta))
    abs_sin = np.abs(np.sin(theta))
    a = rho * (abs_cos+abs_sin)
    b = (1-rho)/2
    if b ==0:
        r = 1/a
    else:
        disc = a**2 + 4*b
        r = (-a +np.sqrt(disc))/(2*b)
    return r
theta = np.linspace(0,2*np.pi,1000)

r_ridge = get_r(theta,rho = 0)
x_ridge = r_ridge*np.cos(theta)
y_ridge = r_ridge*np.sin(theta)

r_lasso = get_r(theta,rho = 1)
x_lasso = r_lasso*np.cos(theta)
y_lasso = r_lasso*np.sin(theta)

r_elastic = get_r(theta,rho = 0.5)
x_elastic = r_elastic*np.cos(theta)
y_elastic = r_elastic*np.sin(theta)

fig, ax = plt.subplots(figsize = (8,8))
ax.plot(x_ridge, y_ridge, label = "Ridge (L2)", color = 'blue')
ax.plot(x_lasso, y_lasso, label = "Lasso (L1)", color = 'red')
ax.plot(x_elastic, y_elastic,label = "elastic (L1+L2)",color = 'green')
ax.set_aspect('equal')
ax.axhline('B1')
ax.axvline('B2')
ax.legend()
plt.grid(True)
plt.show()
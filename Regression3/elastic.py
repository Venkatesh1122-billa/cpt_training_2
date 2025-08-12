from sklearn.linear_model import ElasticNet
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(42)
x, y = make_regression(n_samples = 100, n_features =10, n_informative = 5, noise = 15, random_state=42)
x = x-np.mean(x, axis = 0)
y = y-np.mean(y)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3, random_state=42)
elastic_net = ElasticNet(alpha = 1.0, random_state =42)
elastic_net.fit(x_train, y_train)
y_pred = elastic_net.predict(x_test)

print("Coefficient:",elastic_net.coef_)
print('MSE',mean_squared_error(y_test, y_pred))
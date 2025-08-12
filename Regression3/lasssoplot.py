from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.datasets import make_regression
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x, y = make_regression(n_samples=100, n_features=10, noise=15)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
lasso = Lasso(1.0)
lasso.fit(x_train, y_train)
y_pred = lasso.predict(x_test)

print("Coefficients: ", lasso.coef_)
print('MSE:', mean_squared_error(y_test, y_pred))

# Plot true vs predicted values
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.title('Lasso Regression: True vs Predicted')
plt.grid(True)
plt.show()

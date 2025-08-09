import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
np.random.seed(42)
x = np.random.rand(100,1)*10
y = -2*x+np.random.normal(0,1,(100,1))

x = x.reshape(-1,1)
y = y.ravel()

model = LinearRegression()
model.fit(x,y)

correlation = np.corrcoef(x.ravel(), y)[0,1]
plt.scatter(x,y,color = 'blue', label = 'Data Points')
plt.plot(x, model.predict(x), color = 'red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Negative Correlation")
plt.legend()
plt.show()

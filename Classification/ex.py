import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Data
x = np.array([[1, 2], [2, 3], [3, 4], [6, 5], [7, 7]])
y = np.array([0, 0, 0, 1, 1])
new_point = np.array([[4, 4]])

# Scaling
scaler = StandardScaler()
x_scale = scaler.fit_transform(x)
scaled_new_point = scaler.transform(new_point)

# KNN
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(x_scale, y)

# Prediction
prediction = knn.predict(scaled_new_point)
print('Predicted class:', prediction[0])

# Plotting decision boundary
h = 0.02
x_min, x_max = x_scale[:, 0].min() - 1, x_scale[:, 0].max() + 1
y_min, y_max = x_scale[:, 1].min() - 1, x_scale[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
z = z.reshape(xx.shape)

plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, z, alpha=0.3, cmap='coolwarm')

# Training points
plt.scatter(x_scale[y == 0, 0], x_scale[y == 0, 1], c='lightgrey',
            marker='o', s=100, label='Class 0')
plt.scatter(x_scale[y == 1, 0], x_scale[y == 1, 1], c='darkgrey',
            marker='^', s=100, label='Training point 1')

# New point
plt.scatter(scaled_new_point[:, 0], scaled_new_point[:, 1],
            c='black', marker='s', s=200, label='training2 Point')

# Neighbors
distances, indices = knn.kneighbors(scaled_new_point)
for idx in indices[0]:
    plt.plot([scaled_new_point[0, 0], x_scale[idx, 0]],
             [scaled_new_point[0, 1], x_scale[idx, 1]], 'k--', alpha=0.5)
    plt.scatter(x_scale[idx, 0], x_scale[idx, 1], s=150,
                facecolors='none', edgecolors='k', marker='o',
                label='Neighbor' if idx == indices[0][0] else "")

plt.legend()
plt.title("KNN Classification with Decision Boundary")
plt.grid()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier

# -------------------------------
# K-MEANS CLUSTERING
# -------------------------------
X = np.array([
    [1, 2], [1, 4], [1, 0],
    [10, 2], [10, 4], [10, 0]
])

# Apply KMeans with 2 clusters
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

print("K-Means Cluster Centers:\n", kmeans.cluster_centers_)
print("K-Means Labels:", kmeans.labels_)

# Plot clusters
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
            color='black', marker='X', s=200, label="Centroids")
plt.title("K-Means Clustering")
plt.legend()
plt.show()

# -------------------------------
# K-NEAREST NEIGHBORS (KNN)
# -------------------------------
X_train = [[0], [1], [2], [3]]
y_train = [0, 0, 1, 1]  # Labels

# Create KNN model with k=3
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predict for new data
X_test = [[1.5]]
prediction = knn.predict(X_test)

print("KNN Prediction for", X_test, ":", prediction)




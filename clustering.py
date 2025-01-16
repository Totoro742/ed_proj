from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def cluster_data(resorts, cols, n_clusters=3, method="kmeans", eps=0.5, min_samples=5):
    """
    Clusters the data using KMeans or DBSCAN.

    Parameters:
        resorts (DataFrame): The input data.
        cols (list): List of column names to cluster (2 or 3 columns).
        n_clusters (int): Number of clusters (default: 3, applicable for KMeans).
        method (str): Clustering method ('kmeans' or 'dbscan').
        eps (float): The maximum distance between two samples for DBSCAN (default: 0.5).
        min_samples (int): The number of samples for a core point in DBSCAN (default: 5).

    Returns:
        DataFrame: Input data with an additional "Cluster" column.
    """
    # Validate input
    if len(cols) not in [2, 3]:
        raise ValueError("The function supports only 2D or 3D clustering.")

    # Drop missing values in the specified columns
    data = resorts.dropna(subset=cols)[cols]

    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Apply clustering
    if method == "kmeans":
        model = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = model.fit_predict(scaled_data)
    elif method == "dbscan":
        model = DBSCAN(eps=eps, min_samples=min_samples)
        clusters = model.fit_predict(scaled_data)
    else:
        raise ValueError(f"Unsupported clustering method: {method}")

    # Add cluster labels to the data
    data["Cluster"] = clusters

    # Merge the cluster labels back to the original DataFrame
    resorts = resorts.merge(data[["Cluster"]], left_index=True, right_index=True, how="left")

    # Plot the clusters
    if len(cols) == 2:
        plt.figure(figsize=(8, 6))
        for cluster in set(clusters):
            cluster_data = data[data["Cluster"] == cluster]
            plt.scatter(cluster_data[cols[0]], cluster_data[cols[1]], label=f"Cluster {cluster}")
        plt.xlabel(cols[0])
        plt.ylabel(cols[1])
        plt.title(f"2D Clustering using {method.upper()}")
        plt.legend()
        plt.show()

    elif len(cols) == 3:
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection="3d")
        for cluster in set(clusters):
            cluster_data = data[data["Cluster"] == cluster]
            ax.scatter(cluster_data[cols[0]], cluster_data[cols[1]], cluster_data[cols[2]], label=f"Cluster {cluster}")
        ax.set_xlabel(cols[0])
        ax.set_ylabel(cols[1])
        ax.set_zlabel(cols[2])
        plt.title(f"3D Clustering using {method.upper()}")
        plt.legend()
        plt.show()

    return resorts

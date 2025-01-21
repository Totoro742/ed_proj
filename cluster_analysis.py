from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
from clustering import cluster_data
import warnings

warnings.filterwarnings("ignore")

resorts = pd.read_csv('abnormal_resorts.csv', encoding='latin1')

# Select relevant columns for clustering
features = resorts[["Average Snow", "Season Length", "Snow cannons"]]

features.dropna(inplace=True)

# Standardize the data
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Calculate WCSS for k = 1 to 10
wcss = []
k_values = range(1, 11)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(features_scaled)
    wcss.append(kmeans.inertia_)

# Plot the elbow method
plt.figure(figsize=(8, 5))
plt.plot(k_values, wcss, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.xticks(k_values)
plt.grid(True)
plt.show()

#Find optimal number of clusters
from kneed import KneeLocator

kl = KneeLocator(k_values, wcss, curve='convex', direction='decreasing')
optimal_k = kl.elbow
print(f"Optimal number of clusters: {optimal_k}")


clustered_resorts = cluster_data(resorts, ["Average Snow", "Season Length", "Snow cannons"], n_clusters=4, method="kmeans")

# Save the clustered data to a CSV file
clustered_resorts.to_csv("clustered_resorts.csv", index=False)


# Wybór istotnych kolumn
selected_columns = ['Average Snow', 'Season Length', 'Snow cannons', 'Cluster']
clustered_resorts = clustered_resorts[selected_columns]

# Statystyki opisowe dla każdego klastra
cluster_analysis = clustered_resorts.groupby('Cluster').agg(['mean', 'median', 'min', 'max', 'std', 'count']).round(2)
print(cluster_analysis.to_string())
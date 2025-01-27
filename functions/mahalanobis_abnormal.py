import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import mahalanobis
import warnings
warnings.filterwarnings("ignore")
# Load resorts.csv with specified encoding

threshold = np.sqrt(3)
def abnormal_2d(resorts, col1, col2, threshold=threshold, plot=False):
    # Delete records where Price is equal to 0
    resorts = resorts.dropna(subset=[col1, col2])
    resorts = resorts[resorts[col2] != 0]

    # Extract the relevant columns
    data = resorts[[col1, col2]]

    # Calculate the mean and covariance matrix
    mean = data.mean().values
    cov_matrix = np.cov(data.T)

    # Calculate the Mahalanobis distance for each point
    data['Mahalanobis'] = data.apply(lambda row: mahalanobis(row, mean, np.linalg.inv(cov_matrix)), axis=1)
    data['Resort'] = resorts['Resort']
    # Define a threshold for abnormal values (e.g., 3 standard deviations)

    # Identify abnormal data points
    abnormal_data = data[data['Mahalanobis'] > threshold]

    print("Abnormal Data Points:")
    print(abnormal_data)
    if plot:
    # Plot the data points and highlight the abnormal ones
        plt.scatter(data[col1], data[col2], label='Normal Data')
        plt.scatter(abnormal_data[col1], abnormal_data[col2], color='r', label='Abnormal Data')
        plt.xlabel(f'{col1}')
        plt.ylabel(f'{col2}')
        plt.title(f'Abnormal Data Points in 2D Plane of {col1} and {col2}')
        plt.legend()
        plt.show()
    return abnormal_data

def abnormal_3d(resorts, col1, col2, col3, threshold=threshold, plot=True):
    # Delete records where Price is equal to 0
    resorts = resorts.dropna(subset=[col1, col2, col3])
    resorts = resorts[resorts[col3] != 0]

    # Extract the relevant columns
    data = resorts[[col1, col2, col3]]

    # Calculate the mean and covariance matrix
    mean = data.mean().values
    cov_matrix = np.cov(data.T)

    # Calculate the Mahalanobis distance for each point
    data['Mahalanobis'] = data.apply(lambda row: mahalanobis(row, mean, np.linalg.inv(cov_matrix)), axis=1)
    data['Resort'] = resorts['Resort']

    # Identify abnormal data points
    abnormal_data = data[data['Mahalanobis'] > threshold]

    print("Abnormal Data Points:")
    print(abnormal_data)
    if plot:
    # Plot the data points and highlight the abnormal ones
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(data[col1], data[col2], data[col3], label='Normal Data', color='b')
        ax.scatter(abnormal_data[col1], abnormal_data[col2], abnormal_data[col3], color='r', label='Abnormal Data')
        ax.set_xlabel(f'{col1}')
        ax.set_ylabel(f'{col2}')
        ax.set_zlabel(f'{col3}')
        plt.title(f'Abnormal Data Points in 3D Space of {col1}, {col2}, and {col3}')
        plt.legend()
        plt.show()
    return abnormal_data
# Example usage
if __name__ == '__main__':
    resorts = pd.read_csv('../data/resorts.csv', encoding='latin1')
    abnormal_2d(resorts, 'Total slopes', 'Price')
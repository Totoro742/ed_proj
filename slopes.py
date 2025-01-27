import pandas as pd
from functions.mahalanobis_abnormal import abnormal_2d
from functions.std_abnormal import std_abnormal
from functions.clustering import cluster_data
from functions.util import hist_with_quantiles
# Load resorts.csv with specified encoding
resorts = pd.read_csv('data/resorts.csv', encoding='latin1')

# Delete records where Price is equal to 0
resorts = resorts[resorts['Price'] != 0]

# Calculate quantiles for 'Total slopes' and 'Price'
quantiles_slopes = resorts['Total slopes'].quantile([0.25, 0.5, 0.75])
quantiles_price = resorts['Price'].quantile([0.25, 0.5, 0.75])

hist_with_quantiles(resorts, 'Total slopes')
hist_with_quantiles(resorts, 'Price')
# Find abnormal data points using standard deviation method
std_abnormal(resorts, 'Total slopes')
std_abnormal(resorts, 'Price')

# Find abnormal data points using Mahalanobis distance method
abnormal_2d(resorts, 'Total slopes', 'Price')

cluster_data(resorts, ['Total slopes', 'Price'], n_clusters=3, method='kmeans')
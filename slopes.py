import pandas as pd
import matplotlib.pyplot as plt
from mahalanobis_abnormal import abnormal_2d
from std_abnormal import std_abnormal

# Load resorts.csv with specified encoding
resorts = pd.read_csv('resorts.csv', encoding='latin1')

# Delete records where Price is equal to 0
resorts = resorts[resorts['Price'] != 0]

# Calculate quantiles for 'Total slopes' and 'Price'
quantiles_slopes = resorts['Total slopes'].quantile([0.25, 0.5, 0.75])
quantiles_price = resorts['Price'].quantile([0.25, 0.5, 0.75])

# Plot histogram of ticket prices with quantiles
plt.hist(resorts['Price'], bins=30, edgecolor='black')
for quantile in quantiles_price:
    plt.axvline(quantile, color='r', linestyle='dashed', linewidth=1)
plt.xlabel('Ticket Price [Eur]')
plt.ylabel('Number of Resorts')
plt.title('Distribution of Ticket Prices with Quantiles')
plt.show()

# Plot histogram of total slopes with quantiles
plt.hist(resorts['Total slopes'], bins=30, edgecolor='black')
for quantile in quantiles_slopes:
    plt.axvline(quantile, color='r', linestyle='dashed', linewidth=1)
plt.xlabel('Total Slopes [km]')
plt.ylabel('Number of Resorts')
plt.title('Distribution of Total Slopes with Quantiles')
plt.show()

# Find abnormal data points using standard deviation method
std_abnormal(resorts, 'Total slopes')
std_abnormal(resorts, 'Price')

# Find abnormal data points using Mahalanobis distance method
abnormal_2d(resorts, 'Total slopes', 'Price')
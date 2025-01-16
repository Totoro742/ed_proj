import pandas as pd
import matplotlib.pyplot as plt

# Load resorts.csv with specified encoding
resorts = pd.read_csv('resorts.csv', encoding='latin1')

# Calculate quantiles for 'Total slopes' and 'Price'
def find_abnormalities(resorts, column_name):
    lower_quantile = resorts[column_name].quantile(0.25)
    upper_quantile = resorts[column_name].quantile(0.75)

    # Define the interquartile range (IQR)
    iqr = upper_quantile - lower_quantile

    # Define the lower and upper bounds for abnormal data
    lower_bound = lower_quantile - 1.5 * iqr
    upper_bound = upper_quantile + 1.5 * iqr

    # Find abnormal data points
    abnormal_data = resorts[(resorts[column_name] < lower_bound) | (resorts[column_name] > upper_bound)]

    return abnormal_data

# Example usage
abnormal_slopes = find_abnormalities(resorts, 'Total slopes')
abnormal_price = find_abnormalities(resorts, 'Price')

print("Abnormal Total Slopes:")
print(abnormal_slopes[['Resort', 'Total slopes']])

print("\nAbnormal Prices:")
print(abnormal_price[['Resort', 'Price']])
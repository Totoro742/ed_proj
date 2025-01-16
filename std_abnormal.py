import pandas as pd
import matplotlib.pyplot as plt

# Load resorts.csv with specified encoding
resorts = pd.read_csv('resorts.csv', encoding='latin1')

# Calculate mean and standard deviation for 'Total slopes' and 'Price'
def std_abnormal(resorts, col_name):
    mean = resorts[col_name].mean()
    std = resorts[col_name].std()

    lower_bound = mean - 3 * std
    upper_bound = mean + 3 * std

    print(f"Column: {col_name} Mean: {mean:.2f}, Standard Deviation: {std:.2f}")
    # Find abnormal data points
    abnormal_data = resorts[(resorts[col_name] < lower_bound) | (resorts[col_name] > upper_bound)]

    print("Abnormal Data:")
    print(abnormal_data[['Resort', col_name]])

if __name__ == '__main__':
    std_abnormal(resorts, 'Total slopes')
    std_abnormal(resorts, 'Price')

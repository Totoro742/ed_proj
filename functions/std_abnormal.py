import pandas as pd
import matplotlib.pyplot as plt

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
    return abnormal_data

def quant_abnormal(resorts, column_name):
    lower_quantile = resorts[column_name].quantile(0.25)
    upper_quantile = resorts[column_name].quantile(0.75)

    # Define the interquartile range (IQR)
    iqr = upper_quantile - lower_quantile

    # Define the lower and upper bounds for abnormal data
    lower_bound = lower_quantile - 1.5 * iqr
    upper_bound = upper_quantile + 1.5 * iqr

    # Find abnormal data points
    abnormal_data = resorts[(resorts[column_name] < lower_bound) | (resorts[column_name] > upper_bound)]

    print("Abnormal Data:")
    print(abnormal_data[['Resort', column_name]])
    return abnormal_data

if __name__ == '__main__':
    resorts = pd.read_csv('../data/resorts.csv', encoding='latin1')
    std_abnormal(resorts, 'Total slopes')
    std_abnormal(resorts, 'Price')

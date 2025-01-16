import matplotlib.pyplot as plt

def hist_with_quantiles(resorts, col):
    quantiles = resorts[col].quantile([0.25, 0.5, 0.75])

    plt.hist(resorts[col], bins=30, edgecolor='black')
    for quantile in quantiles:
        plt.axvline(quantile, color='r', linestyle='dashed', linewidth=1)
    plt.xlabel(f'{col}')
    plt.ylabel('Number of Resorts')
    plt.title(f'Distribution of {col} with Quantiles')
    plt.show()

    return quantiles
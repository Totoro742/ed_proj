import pandas as pd

from functions.classification import classify
from seasons import precompute_season_lengths, compute_average_snow
from functions.std_abnormal import std_abnormal
from data.mahalanobis_abnormal import abnormal_3d

# Load the data
resorts = pd.read_csv("data/resorts.csv", encoding='latin1')
snow = pd.read_csv("data/snow.csv", encoding='latin1')

# Compute additional columns
resorts["Season Length"] = resorts["Season"].map(precompute_season_lengths(resorts["Season"].unique()))
resorts["Average Snow"] = compute_average_snow(resorts, snow)

# Initialize abnormal columns
resorts["Abnormal_1D_Average_Snow"] = False
resorts["Abnormal_1D_Season_Length"] = False
resorts["Abnormal_1D_Snow_Cannons"] = False
resorts["Abnormal_3D"] = False

# Identify 1D abnormal data
abnormal_1d_snow = std_abnormal(resorts, 'Average Snow')
abnormal_1d_season_length = std_abnormal(resorts, 'Season Length')
abnormal_1d_snow_cannons = std_abnormal(resorts, 'Snow cannons')

if abnormal_1d_snow is not None:
    resorts.loc[abnormal_1d_snow.index, "Abnormal_1D_Average_Snow"] = True
if abnormal_1d_season_length is not None:
    resorts.loc[abnormal_1d_season_length.index, "Abnormal_1D_Season_Length"] = True
if abnormal_1d_snow_cannons is not None:
    resorts.loc[abnormal_1d_snow_cannons.index, "Abnormal_1D_Snow_Cannons"] = True

# Identify 3D abnormal data
abnormal_3d_data = abnormal_3d(resorts, 'Average Snow', 'Season Length', 'Snow cannons', threshold=3, plot=False)

if abnormal_3d_data is not None:
    resorts.loc[abnormal_3d_data.index, "Abnormal_3D"] = True

resorts.dropna(inplace=True)



# Save to CSV
resorts.to_csv("abnormal_resorts.csv", index=False)

# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Country']])
#
# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']], model_type='knn')
#
# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']], model_type='random_forest')
#
# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']])


classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Country']] , target_name='country',model_type='knn', )
classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Country']] , target_name='country',model_type='decision_tree')
# classify_density(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Country']])
classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Country']] , target_name='country', model_type='random_forest')

classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']] , target_name='continent',model_type='knn', )
classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']] , target_name='continent',model_type='decision_tree')
classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']] , target_name='continent', model_type='random_forest')

resorts['Average Height'] = (resorts['Highest point'] + resorts['Lowest point']) / 2
def classify_average_height(avg_height):
    if avg_height < 1000:  # Example threshold, adjust as needed
        return "Low"
    elif 1000 <= avg_height <= 2000:
        return "Medium"
    else:
        return "High"

resorts['Height Class'] = resorts['Average Height'].apply(classify_average_height)


classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class']] , target_name='height class',model_type='knn', )
classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class']] , target_name='height class',model_type='decision_tree')
classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class']] , target_name='height class', model_type='random_forest')


resorts['Average Height'] = resorts['Average Height'].sort_values(ascending=True)

lower_quantile = resorts['Average Height'].quantile(0.33)
upper_quantile = resorts['Average Height'].quantile(0.66)
def classify_average_height_quantiles(avg_height):
    if avg_height <= lower_quantile:  # Below or equal to the lower quantile
        return "Low"
    elif lower_quantile < avg_height <= upper_quantile:  # Between lower and upper quantiles
        return "Medium"
    else:  # Above the upper quantile
        return "High"


# Step 4: Apply the classification
resorts['Height Class2'] = resorts['Average Height'].apply(classify_average_height_quantiles)

classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class2']] , target_name='height class k',model_type='knn', )
classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class2']] , target_name='height class k',model_type='decision_tree')
classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class2']] , target_name='height class k', model_type='random_forest')






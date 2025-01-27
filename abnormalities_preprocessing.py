import pandas as pd

from functions.classification import classify
from seasons import precompute_season_lengths, compute_average_snow
from functions.std_abnormal import std_abnormal
from functions.mahalanobis_abnormal import abnormal_3d

# Load the data
resorts = pd.read_csv("./data/resorts.csv", encoding='latin1')
snow = pd.read_csv("./data/snow.csv", encoding='latin1')

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


# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Country']] , target_name='country',model_type='knn', )
# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Country']] , target_name='country',model_type='decision_tree')
# # classify_density(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Country']])
# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Country']] , target_name='country', model_type='random_forest')
#
# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']] , target_name='continent',model_type='knn', )
# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']] , target_name='continent',model_type='decision_tree')
# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']] , target_name='continent', model_type='random_forest')

resorts['Average Height'] = (resorts['Highest point'] + resorts['Lowest point']) / 2

print(resorts.count())
def classify_average_height(avg_height):
    if avg_height < 1300:  # Example threshold, adjust as needed
        return "Low"
    elif 1300 <= avg_height <= 2000:
        return "Medium"
    else:
        return "High"

resorts['Height Class'] = resorts['Average Height'].apply(classify_average_height)


# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class']] , target_name='height class',model_type='knn', )
# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class']] , target_name='height class',model_type='decision_tree')
# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class']] , target_name='height class', model_type='random_forest')


resorts['Average Height'] = resorts['Average Height'].sort_values(ascending=True)
resorts.sort_values(by='Average Height', ascending=True, inplace=True)
print(resorts.head())
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

# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class2']] , target_name='height class k',model_type='knn', )
# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class2']] , target_name='height class k',model_type='decision_tree')
# classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class2']] , target_name='height class k', model_type='random_forest')



# lista = [ [10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10], [100, 11], [100,12],
#           [100,13], [100,14], [100,15], [100,16], [100,17], [100,18], [100,19], [100,20]]
#
# for i in lista:
#     print(f'params: {i}')
#
#     classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Country']], target_name='country',
#              model_type='knn', params=i )
#     classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Country']], target_name='country',
#              model_type='decision_tree', params=i)
#
#     classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Country']], target_name='country',
#              model_type='random_forest', params=i)
#
#     classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']], target_name='continent',
#              model_type='knn', params=i)
#     classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']], target_name='continent',
#              model_type='decision_tree', params=i)
#     classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']], target_name='continent',
#              model_type='random_forest', params=i)
#
#     classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class']],
#              target_name='hc1',
#              model_type='knn', params=i)
#     classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class']],
#              target_name='hc1',
#              model_type='decision_tree', params=i)
#     classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class']],
#              target_name='hc1',
#              model_type='random_forest', params=i)
#
#     classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class2']],
#              target_name='hc2',
#              model_type='knn', params=i)
#     classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class2']],
#              target_name='hc2',
#              model_type='decision_tree', params=i)
#     classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class2']],
#              target_name='hc2',
#              model_type='random_forest', params=i)
# print()


# lista = [[x, x] for x in range (1, 120)]
#
# for i in lista:
#     print(f'params: {i[0]}')
#     classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']],
#                  target_name='continent',
#                  model_type='knn', params=i)

classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class']],
                 target_name='hc1',
                 model_type='knn', params=[7, 7])
classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Height Class2']],
                 target_name='hc2',
                 model_type='knn', params=[4,4])
classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Continent']],
             target_name='continent',
             model_type='knn', params=[3, 3])
classify(resorts[['Average Snow', 'Season Length', 'Snow cannons']], resorts[['Country']],
                 target_name='country',
                 model_type='knn', params=[6,6])




#params: 7 Dokładność modelu knn dla hc1:0.49
#params: 4 Dokładność modelu knn dla hc2:0.44
#params: 6 Dokładność modelu knn dla country:0.30
#params: 3 Dokładność modelu knn dla continent:0.77








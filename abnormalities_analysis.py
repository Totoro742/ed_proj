import pandas as pd

file_path = 'data/abnormal_resorts.csv'
data = pd.read_csv(file_path)

abnormal_snow = data[(data['Abnormal_1D_Average_Snow'] == True)]
abnormal_length = data[(data['Abnormal_1D_Season_Length'] == True)]
abnormal_cannons = data[(data['Abnormal_1D_Snow_Cannons'] == True)]

print(f"Liczba wartości abnormalnych w poryciu śniegu: {len(abnormal_snow)}")
print(f"Liczba wartości abnormalnych w długości sezonu: {len(abnormal_length)}")
print(f"Liczba wartości abnormalnych w ilości armatek: {len(abnormal_cannons)}")

abnormal_3d = data[(data['Abnormal_3D'] == True)]

print(f"Liczba wartości abnormalnych w poryciu śniegu, długości sezonu i ilości armatek: {len(abnormal_3d)}")

#print all records with abnormal snow or length values and snow_length values or abnormal 3d values, all in one markdown
abnormal_combined = data[(data['Abnormal_1D_Average_Snow'] == True) |
                         (data['Abnormal_1D_Season_Length'] == True) |
                         (data['Abnormal_1D_Snow_Cannons'] == True) |
                         (data['Abnormal_3D'] == True)]


abnormal_combined = abnormal_combined[['Resort', 'Average Snow', 'Season Length', 'Snow cannons', 'Abnormal_1D_Average_Snow', 'Abnormal_1D_Season_Length', 'Abnormal_1D_Snow_Cannons', 'Abnormal_3D']]

#rename columns
abnormal_combined.columns = ['Resort', 'Average Snow', 'Season Length', 'Snow cannons', 'A. Avg Snow', 'A. Season', 'A. Cannons', 'A. 3D']

print(abnormal_combined.to_markdown())

import geopandas as gpd
import matplotlib.pyplot as plt

# Load world map
world = gpd.read_file('data/ne_110m_admin_0_countries.shp')

# Create a GeoDataFrame for abnormal points
abnormal_combined = data[(data['Abnormal_1D_Average_Snow'] == True) |
                         (data['Abnormal_1D_Season_Length'] == True) |
                         (data['Abnormal_1D_Snow_Cannons'] == True) |
                         (data['Abnormal_3D'] == True)]

gdf = gpd.GeoDataFrame(
    abnormal_combined, geometry=gpd.points_from_xy(abnormal_combined.Longitude, abnormal_combined.Latitude))

# Plot the world map
fig, ax = plt.subplots(figsize=(15, 10))
world.plot(ax=ax, color='lightgrey')

# Plot the abnormal points
gdf.plot(ax=ax, color='red', markersize=5, label='Abnormal Points')

plt.title('Abnormal Resorts on World Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()


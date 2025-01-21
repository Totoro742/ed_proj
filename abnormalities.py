import pandas as pd
import numpy as np

from seasons import precompute_season_lengths, compute_average_snow
from std_abnormal import std_abnormal
from mahalanobis_abnormal import abnormal_2d, abnormal_3d

# Load the data
resorts = pd.read_csv("resorts.csv", encoding='latin1')
snow = pd.read_csv("snow.csv", encoding='latin1')

# Compute additional columns
resorts["Season Length"] = resorts["Season"].map(precompute_season_lengths(resorts["Season"].unique()))
resorts["Average Snow"] = compute_average_snow(resorts, snow)

# Initialize abnormal columns
resorts["Abnormal_1D_Average_Snow"] = False
resorts["Abnormal_1D_Season_Length"] = False
resorts["Abnormal_1D_Snow_Cannons"] = False
resorts["Abnormal_2D_Average_Snow_Season_Length"] = False
resorts["Abnormal_2D_Average_Snow_Snow_Cannons"] = False
resorts["Abnormal_2D_Season_Length_Snow_Cannons"] = False
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


# Identify 2D abnormal data
abnormal_2d_snow_season_length = abnormal_2d(resorts, 'Average Snow', 'Season Length', threshold=np.sqrt(3))
abnormal_2d_snow_snow_cannons = abnormal_2d(resorts, 'Average Snow', 'Snow cannons', threshold=np.sqrt(3))
abnormal_2d_season_length_snow_cannons = abnormal_2d(resorts, 'Season Length', 'Snow cannons', threshold=np.sqrt(3))

if abnormal_2d_snow_season_length is not None:
    resorts.loc[abnormal_2d_snow_season_length.index, "Abnormal_2D_Average_Snow_Season_Length"] = True
if abnormal_2d_snow_snow_cannons is not None:
    resorts.loc[abnormal_2d_snow_snow_cannons.index, "Abnormal_2D_Average_Snow_Snow_Cannons"] = True
if abnormal_2d_season_length_snow_cannons is not None:
    resorts.loc[abnormal_2d_season_length_snow_cannons.index, "Abnormal_2D_Season_Length_Snow_Cannons"] = True


# Identify 3D abnormal data
abnormal_3d_data = abnormal_3d(resorts, 'Average Snow', 'Season Length', 'Snow cannons', threshold=1)

if abnormal_3d_data is not None:
    resorts.loc[abnormal_3d_data.index, "Abnormal_3D"] = True

resorts.dropna(inplace=True)



# Save to CSV
resorts.to_csv("abnormal_resorts.csv", index=False)
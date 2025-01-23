import pandas as pd
import numpy as np
from datetime import datetime
from scipy.spatial import cKDTree
from std_abnormal import std_abnormal
from mahalanobis_abnormal import abnormal_2d, abnormal_3d
from clustering import cluster_data
from util import hist_with_quantiles

resorts = pd.read_csv("resorts.csv", encoding='latin1')
snow = pd.read_csv("snow.csv", encoding='latin1')


def precompute_season_lengths(seasons):
    months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5,
              "June": 6, "July": 7, "August": 8, "September": 9, "October": 10,
              "November": 11, "December": 12}

    season_lengths = {}
    for season in seasons:
        if season == "Year-round":
            season_lengths[season] = 365
        elif season == "Unknown":
            season_lengths[season] = None
        else:
            try:
                total_days = 0
                for range_ in season.split(", "):
                    if "-" not in range_:
                        start_date = datetime(2022, months[range_], 1)
                        if range_ == "February":
                            days_in_month = 28
                        else:
                            days_in_month = (datetime(2022, months[range_] % 12 + 1, 1) - start_date).days
                        total_days += days_in_month
                    else:
                        start, end = range_.split(" - ")
                        start_date = datetime(2022, months[start], 1)
                        end_date = datetime(2022, months[end], 1)
                        if end_date < start_date:
                            end_date = datetime(2023, months[end], 1)
                        total_days += (end_date - start_date).days
                season_lengths[season] = total_days
            except Exception:
                season_lengths[season] = None
    season_lengths["December"] = 31
    return season_lengths


unique_seasons = resorts["Season"].unique()
season_lengths = precompute_season_lengths(unique_seasons)
resorts["Season Length"] = resorts["Season"].map(season_lengths)

def compute_average_snow(resorts, snow, threshold_km=50):
    snow_coords = snow[["Latitude", "Longitude"]].to_numpy()
    snow_values = snow["Snow"].to_numpy()

    tree = cKDTree(snow_coords)
    max_distance = threshold_km / 111
    average_snow = []
    for _, resort in resorts.iterrows():
        resort_coord = [resort["Latitude"], resort["Longitude"]]
        distances, indices = tree.query(resort_coord, k=len(snow_coords), distance_upper_bound=threshold_km / 111)

        valid_indices = indices[distances < np.inf]
        if valid_indices.size > 0:
            avg_snow = np.mean(snow_values[valid_indices])
        else:
            avg_snow = None

        average_snow.append(avg_snow)

    return average_snow

resorts["Average Snow"] = compute_average_snow(resorts, snow)

hist_with_quantiles(resorts, 'Average Snow')
hist_with_quantiles(resorts, 'Season Length')
hist_with_quantiles(resorts, 'Snow cannons')

std_abnormal(resorts, 'Average Snow')
std_abnormal(resorts, 'Season Length')
std_abnormal(resorts, 'Snow cannons')

abnormal_3d(resorts, 'Average Snow', 'Season Length', 'Snow cannons', threshold=3)

cluster_data(resorts, ['Average Snow', 'Season Length', 'Snow cannons'], n_clusters=4, method='kmeans')

cluster_data(resorts, ['Average Snow', 'Season Length', 'Snow cannons'], n_clusters=5, method='kmeans')

cluster_data(resorts, ['Average Snow', 'Season Length', 'Snow cannons'], n_clusters=6, method='kmeans')
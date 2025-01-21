import pandas as pd

file_path = 'abnormal_resorts.csv'
data = pd.read_csv(file_path)

abnormal_snow = data[(data['Abnormal_1D_Average_Snow'] == True)]
abnormal_length = data[(data['Abnormal_1D_Season_Length'] == True)]
abnormal_cannons = data[(data['Abnormal_1D_Snow_Cannons'] == True)]

print(f"Liczba wartości abnormalnych w poryciu śniegu: {len(abnormal_snow)}")
print(f"Liczba wartości abnormalnych w długości sezonu: {len(abnormal_length)}")
print(f"Liczba wartości abnormalnych w ilości armatek: {len(abnormal_cannons)}")

abnormal_2d_snow_length = data[(data['Abnormal_2D_Average_Snow_Season_Length'] == True)]
abnormal_2d_snow_cannons = data[(data['Abnormal_2D_Average_Snow_Snow_Cannons'] == True)]
abnormal_2d_length_cannons = data[(data['Abnormal_2D_Season_Length_Snow_Cannons'] == True)]

print(f"Liczba wartości abnormalnych w poryciu śniegu i długości sezonu: {len(abnormal_2d_snow_length)}")
print(f"Liczba wartości abnormalnych w poryciu śniegu i ilości armatek: {len(abnormal_2d_snow_cannons)}")
print(f"Liczba wartości abnormalnych w długości sezonu i ilości armatek: {len(abnormal_2d_length_cannons)}")

abnormal_3d = data[(data['Abnormal_3D'] == True)]

print(f"Liczba wartości abnormalnych w poryciu śniegu, długości sezonu i ilości armatek: {len(abnormal_3d)}")


#print all recoreds with abnormal snow or length values and snow_length values
print(abnormal_snow[['Resort', 'Average Snow']])
print(abnormal_length[['Resort', 'Season Length']])
print(abnormal_cannons[['Resort', 'Snow cannons']])
print(abnormal_2d_snow_length[['Resort', 'Average Snow', 'Season Length']])
print(abnormal_2d_snow_cannons[['Resort', 'Average Snow', 'Snow cannons']])
print(abnormal_2d_length_cannons[['Resort', 'Season Length', 'Snow cannons']])
print(abnormal_3d[['Resort', 'Average Snow', 'Season Length', 'Snow cannons']])

print(data[(data['Abnormal_1D_Average_Snow'] == False) & (data['Abnormal_1D_Season_Length'] == False) & (data['Abnormal_1D_Snow_Cannons'] == False) & (data['Abnormal_2D_Average_Snow_Season_Length'] == False) & (data['Abnormal_2D_Average_Snow_Snow_Cannons'] == False) & (data['Abnormal_2D_Season_Length_Snow_Cannons'] == False) & (data['Abnormal_3D'] == True)])

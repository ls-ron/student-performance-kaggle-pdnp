import pandas as pd
import numpy as np

spotify_df = pd.read_csv('Student_performance_data _.csv')
print(spotify_df)

total_gpa_f = 0
num_girls = 0
total_gpa_m = 0
num_boys = 0
for i in range(len(spotify_df)):
    if int(spotify_df['Gender'][i]) == 1:
        total_gpa_f += float(spotify_df['GPA'][i])
        num_girls += 1
    elif int(spotify_df['Gender'][i]) == 0:
        total_gpa_m += float(spotify_df['GPA'][i])
        num_boys += 1
    else:
        continue

mean_girl_gpa = round(total_gpa_f / num_girls, 5)
print(mean_girl_gpa)
mean_boy_gpa = round(total_gpa_m / num_boys, 5)
print(mean_boy_gpa)



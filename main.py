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

mean_girl_gpa = round(total_gpa_f / num_girls, 3)
mean_boy_gpa = round(total_gpa_m / num_boys, 3)
print(f"The average male's GPA was {mean_boy_gpa}, while the average female's GPA was {mean_girl_gpa}")

gender_arr = np.array(spotify_df['Gender'])
print(f"for every 100 students, {round(100 * np.mean(gender_arr))} will be male")

absences = np.array(spotify_df['Absences'])
mean_absences = round(np.mean(absences))
print(f'There are {np.sum(absences)} total absences with an average of {mean_absences} for each student')


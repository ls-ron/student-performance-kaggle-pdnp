import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

student_performance_df = pd.read_csv('Student_performance_data _.csv')
print(student_performance_df)

total_gpa_f = 0
num_girls = 0
total_gpa_m = 0
num_boys = 0
for i in range(len(student_performance_df)):
    if int(student_performance_df['Gender'][i]) == 1:
        total_gpa_f += float(student_performance_df['GPA'][i])
        num_girls += 1
    elif int(student_performance_df['Gender'][i]) == 0:
        total_gpa_m += float(student_performance_df['GPA'][i])
        num_boys += 1
    else:
        continue

mean_girl_gpa = round(total_gpa_f / num_girls, 3)
mean_boy_gpa = round(total_gpa_m / num_boys, 3)
print(f"The average male's GPA was {mean_boy_gpa}, while the average female's GPA was {mean_girl_gpa}")

gender_arr = np.array(student_performance_df['Gender'])
print(f"For every 100 students, {round(100 * np.mean(gender_arr))} will be male")

absences = np.array(student_performance_df['Absences'])
mean_absences = round(np.mean(absences))
print(f'There are {np.sum(absences)} total absences with an average of {mean_absences} for each student')

def line_graph(x_axis, y_axis):
    head = student_performance_df.sort_values(x_axis, ascending=False).head(15)
    print(head)
    plt.plot(head[x_axis], head[y_axis])
    plt.show()

line_graph('GPA', 'ParentalEducation')
print(f"The plot shows no significant correlation between the education level of the parents, and the resulting GPA of the students")

def histogram(x_axis):
    plt.hist(student_performance_df[x_axis])
    plt.show()

histogram('Age')
print(f"There are a relatively equal amount of students in each age group")

def scatter(x_axis, y_axis):
    random_sample = student_performance_df.sample(50)
    sns.scatterplot(x=random_sample[x_axis], y=random_sample[y_axis], hue=random_sample.Gender)
    plt.show()

scatter('GPA', 'Absences')
print(f"There is a negative correlation where as absences are lower for a particular student, the GPA is higher/lower for females than males.")




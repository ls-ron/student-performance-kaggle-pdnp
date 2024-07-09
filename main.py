# importing the required 3rd party libraries (dont forget to pip install them)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# loading in the .csv file to create a dataframe of data
student_performance_df = pd.read_csv('Student_performance_data _.csv')
print(student_performance_df)

# initialising variables to get info from a different vector within the dataframe
total_gpa_f = 0
num_girls = 0
total_gpa_m = 0
num_boys = 0
# a loop that counts the number of boys/girls and aggregates the GPA values for each gender
for i in range(len(student_performance_df)):
    if int(student_performance_df['Gender'][i]) == 1:
        total_gpa_f += float(student_performance_df['GPA'][i])
        num_girls += 1
    elif int(student_performance_df['Gender'][i]) == 0:
        total_gpa_m += float(student_performance_df['GPA'][i])
        num_boys += 1
    else:
        continue

# the mean of each gender's GPA
mean_girl_gpa = round(total_gpa_f / num_girls, 3)
mean_boy_gpa = round(total_gpa_m / num_boys, 3)
print(f"The average male's GPA was {mean_boy_gpa}, while the average female's GPA was {mean_girl_gpa}")

# used np.array to be able to get the mean gender (numerically) using NumPy
gender_arr = np.array(student_performance_df['Gender'])
print(f"For every 100 students, {round(100 * np.mean(gender_arr))} will be male")

# same as the previous comment but for absences
absences = np.array(student_performance_df['Absences'])
mean_absences = round(np.mean(absences))
print(f'There are {np.sum(absences)} total absences with an average of {mean_absences} for each student')

# a plot that utilises the line graph from matplotlib library by sorting values 
# in descending order of the x-axis to show the relationship between GPA and Parental Education
def line_graph(x_axis, y_axis):
    head = student_performance_df.sort_values(x_axis, ascending=False).head(15)
    print(head)
    plt.plot(head[x_axis], head[y_axis])
    plt.show()

line_graph('GPA', 'ParentalEducation')
print(f"The plot shows no significant correlation between the education level of the parents, and the resulting GPA of the students")

# a histogram from matplotlib (that is a bit bugged since it looks like a 
# bar chart) that shows the distribution of age groups: 15, 16, 17, 18
def histogram(x_axis):
    plt.hist(student_performance_df[x_axis])
    plt.show()

histogram('Age')
print(f"There are a relatively equal amount of students in each age group")

# a scatterplot from seaborn library to show the relationship from randomly selected rows in the df
# based off how GPA and Absences affect each other, with hue differentiating the points on the graph
def scatter(x_axis, y_axis):
    random_sample = student_performance_df.sample(50)
    sns.scatterplot(x=random_sample[x_axis], y=random_sample[y_axis], hue=random_sample.Gender)
    plt.show()

scatter('GPA', 'Absences')
print(f"There is a negative correlation where as absences are lower for a particular student, the GPA is higher/lower for females than males.")




import pandas as pd

data = {
    'Student': ['John', 'Sara', 'Mike', 'Anna', 'David', 'Emily', 'Chris', 'Sophia'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Marks': [85, 72, 90, 65, 78, 88, 92, 55],
    'Attendance': [92, 80, 95, 70, 85, 90, 97, 60]
}

df = pd.DataFrame(data)
avg_marks = df.groupby('Subject')['Marks'].mean()
print("Average Marks by Subject:")
print(avg_marks)
high_scorers_low_attendance = df[(df['Marks'] > 85) & (df['Attendance'] < 95)]
print("Students with Marks > 85 and Attendance < 95:")
print(high_scorers_low_attendance)
def assign_grade(marks):
    if marks >= 90:
        return 'A'
    elif 80 <= marks < 90:
        return 'B'
    elif 70 <= marks < 80:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Marks'].apply(assign_grade)

print("\nUpdated DataFrame with Grades:")
print(df)
grade_counts = df['Grade'].value_counts()
print("\nGrade Distribution:")
print(grade_counts)
correlation = df[['Marks', 'Attendance']].corr().iloc[0, 1]
print("\nCorrelation between Marks and Attendance:", round(correlation, 2))
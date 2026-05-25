import pandas as pd

# 1. Load Dataset (simple relative path)
df = pd.read_csv('student_performance.csv')
df['total_score'] = df['math_score'] + df['programming_score']

# Task 1: Title
print("--- STUDENT EXPLORER ---\n")

# Task 2 & 3: Overview & Departments
print("Total Students:", len(df))
print("\nStudents per Department:")
print(df['department'].value_counts())

# Task 4 & 5: Basic Stats & Grouping
print("\nAverage Math Score:", df['math_score'].mean())
print("\nAverage Total Score by Gender:")
print(df.groupby('gender')['total_score'].mean())

# Task 6: Top Performers 
print("\nTop 2 Students:")
top_students = df.nlargest(2, 'total_score')
print(top_students[['name', 'department', 'total_score']])

# Task 7: Attendance Alert
print("\nLow Attendance Alert (<75%):")
low_attendance = df[df['attendance_percentage'] < 75]

if len(low_attendance) == 0:
    print("Everyone is above 75%!")
else:
    print(low_attendance[['name', 'attendance_percentage']])
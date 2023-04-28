import math

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# Get total number of students and total heights
number_of_students = len(student_heights)
total_heights = sum(student_heights)

# Calculate average and round up
average = total_heights / number_of_students
average = round(average)

print(average)

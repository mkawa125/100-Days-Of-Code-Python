
# Get scores inputs from user
student_scores = input("Input a list of student heights ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)

# First way of calculating highest score
highest_score = max(student_scores)
print(f"The highest score in the class is: {highest_score}")


# Other way of calculating highest score
highest_score_2 = 0
for score in student_scores:
    if score > highest_score_2:
        highest_score_2 = score
print(f"The highest score in the class is: {highest_score_2}")

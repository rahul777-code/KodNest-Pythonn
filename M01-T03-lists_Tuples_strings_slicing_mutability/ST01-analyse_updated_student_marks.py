student_count = int(input())
marks = []

# Read and store all marks using append()
for i in range(student_count):
    marks.append(int(input()))

position = int(input())
corrected_mark = int(input())
passing_mark = int(input())

# Update the mark at the entered student position
marks[position - 1] = corrected_mark

# Calculate the total, average, highest and lowest marks
total_marks = sum(marks)
average_marks = total_marks / student_count
highest_mark = max(marks)
lowest_mark = min(marks)

# Count the students whose marks satisfy the passing condition
passed_students = 0
for mark in marks:
    if mark >= passing_mark:
        passed_students += 1

# Display the updated analysis
print("Updated Marks:", marks)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Mark:", highest_mark)
print("Lowest Mark:", lowest_mark)
print("Passed Students:", passed_students)
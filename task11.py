import numpy as np

marks = np.array([85, 90, 78, 92, 88])

mean_marks = np.mean(marks)
median_marks = np.median(marks)
max_marks = np.max(marks)
min_marks = np.min(marks)
std_marks = np.std(marks)

print("Student Marks:", marks)
print("Mean:", mean_marks)
print("Median:", median_marks)
print("Maximum:", max_marks)
print("Minimum:", min_marks)
print("Standard Deviation:", std_marks)

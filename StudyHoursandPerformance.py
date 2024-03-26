# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 00:55:48 2024

@author: mural
"""

import matplotlib.pyplot as plt

# Sample student data
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
study_hours = [5, 7, 3, 8, 6]  # Hours of study per day
math_grades = [85, 90, 80, 75, 95]
science_grades = [80, 85, 75, 70, 90]
english_grades = [90, 85, 80, 85, 95]

# Plotting the data
plt.figure(figsize=(10, 6))

plt.scatter(study_hours, math_grades, label='Math', color='red', s=100, alpha=0.7)
plt.scatter(study_hours, science_grades, label='Science', color='blue', s=100, alpha=0.7)
plt.scatter(study_hours, english_grades, label='English', color='green', s=100, alpha=0.7)

plt.xlabel('Study Hours per Day')
plt.ylabel('Average Grades')
plt.title('Relationship Between Study Hours and Academic Performance')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
'''
Created on Mar 12, 2024

@author: student
'''
numbers = [1, 2, 3, 4, 5]
squares = [num**2 for num in numbers]
print(squares)

students = [("Alice", 85), ("Bob", 45), ("Charlie", 72), ("David", 90), ("Eve", 55)]
passed_students = [name for (name, grade) in students if grade >= 60 ]
print(passed_students)

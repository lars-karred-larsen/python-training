'''
Created on Mar 6, 2024

@author: student
'''
class Student:
    def __init__(self, student_id, student_name, student_marks):
        self.student_id = student_id
        self.student_name = student_name
        self.student_marks = student_marks

student = Student(8717585, "Lars Karred Larsen", 98)
print(student.student_id)
print(student.student_name)
print(student.student_marks)
print(student.__dict__)

print(round(1.242424,2))
import main
print(main.first_name)

import math
print(dir(math.trunc))

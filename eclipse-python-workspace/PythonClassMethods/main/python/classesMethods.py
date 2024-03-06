'''
Created on Mar 6, 2024

@author: student
'''
class Student:
    def __init__(self, student_id, student_name, student_marks):
        self.student_id = student_id
        self.student_name = student_name
        self.__student_marks = student_marks

    def get_student_id(self):
        return self.__student_id
         
    def get_student_name(self):
        return self.__student_name
         
    def get_student_marks(self):
        return self.__student_marks
         
    def set_student_id(self, value):
        self.__student_id = value
        
    def set_student_name(self, value):
        self.__student_name = value
        
    def set_student_marks(self, value):
        self.__student_marks = value
        
    def validate_marks(self):
        if self.get_student_marks() >= 70:
            return "Passed"
        return "Not Passed"
        
student = Student(8717585, "Lars Karred Larsen", 98)
print(student.student_id)
print(student.student_name)
print(student.__dict__)
print(student.validate_marks())         

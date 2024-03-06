'''
Created on Mar 6, 2024

@author: student
'''
class Person:
    def __init__(self,name):
        self.name = name
    
    def get_name(self):
        return self.__name
     
    def set_name(self, value):
         self.__name = value
    
class Student(Person):
    def __init__(self, student_id, student_marks):
        self.__student_id = student_id
        self.__student_marks = student_marks
        
    def get_student_id(self):
        return self.__student_id
    
    def get_student_marks(self):
        return self.__student_marks
    
    def set_student_id(self, value):
        self.__student_id = value
    
    def set_student_marks(self, value):
        self.__student_marks = value

student = Student(8717585, 98)
student.set_name("Lars Karred Larsen")
print("All the get()",student.get_name(),student.get_student_id(),student.get_student_marks())
print("__name__",Student.__name__)
print("__module__", Student.__module__)
print("__bases__", Student.__bases__)

    
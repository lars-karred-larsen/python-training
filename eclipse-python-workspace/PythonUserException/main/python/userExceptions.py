'''
Created on Mar 4, 2024

@author: student
'''
class MyCustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

def divide(x,y):
    if y == 0:
        raise MyCustomError("Division by zero not allowed!")
    return x/y

try:
    result = divide(10, 0)
    print("Result:", result)
except MyCustomError as e:
    print("Custom error occurred:",e.message)

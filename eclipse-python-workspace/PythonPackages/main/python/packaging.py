'''
Created on Mar 5, 2024

@author: student
'''
import math

#Now you can use functions from math module like this:
print("Square root of 16:", math.sqrt(16))

from math import sqrt
#Now you can directly use the sqrt function without referencing the math module:
print("Square root of 25:", sqrt(25))

import math as m
#You can now use the alias 'm' to reference the math module:
print("Value of pi:", m.pi)

from math import *
#Now you can use all functions and constants from the math module directly:
print("Square root of 36:", sqrt(36))
print("Value of pi:", m.pi)

class MyClass:
    def __init__(self):
        self.name = "Lars"
        self.age = 56
        
        def greet(self):
            print("Hello, I'm", self.name)

#Create an instance of the class
obj = MyClass()
#Use dir() to list attributes and methods of the object
print("Attribbutes and methods of obj:", dir(obj))

import sys
#Print the list of directories in the sys.path
print("List of directories in sys.path:")
for directory in sys.path:
    print(directory)

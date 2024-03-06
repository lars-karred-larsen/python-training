'''
Created on Mar 5, 2024

@author: student
'''
class MyClass:
    def __init__(self):
        #Public variable
        self.public_var = 10
        self.__private_var = 20
    
    def get_private_var(self):
        return self.__private_var
    
    def set_private_var(self, value):
        self.__private_var = value

#Creating an instance of MyClass
obj = MyClass()

#Accessing public variable
print("Public variable:",obj.public_var)

#Accessing private variable using getter method
print("Private variable (using getter):",obj.get_private_var())

#Trying to access private variable directly (will raise AtrributeError)
#print("Private variable (direct access):", obj.__private_var)

#Modifying private variable using setter method
obj.set_private_var(30)
print("Private variable (after modification):",obj.get_private_var())

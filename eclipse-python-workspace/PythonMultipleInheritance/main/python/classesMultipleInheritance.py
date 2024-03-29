'''
Created on Mar 6, 2024

@author: student
'''
class Animal:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"I am an animal named {self.name}"
    
    def make_sound(self):
        pass
    
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
            
    def make_sound(self):
        return "Some generic mammal sound"
        
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
            
    def make_sound(self):
        return "Some generic bird sound"
            
class Bat(Mammal, Bird):
    def __init__(self, name):
        super().__init__(name)
            
    def make_sound(self):
        return "Squeak"
            
bat = Bat("Batty")
bat2 = bat

print(isinstance(bat, Bat))
print(isinstance(bat, Mammal))
print(isinstance(bat, Bird))
print(isinstance(bat, Animal))

print(bat) #Calls __str__ from Animal class
print(bat2)
print(bat2 is bat)
num1 = 10
num2 = num1
num1 = 40
print(num2 is num1)

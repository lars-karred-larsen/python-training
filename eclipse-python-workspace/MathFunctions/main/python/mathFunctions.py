'''
Created on Mar 5, 2024

@author: student
'''
import math

#ceil() function rounds up a number to the nearest integer
print("ceil(4.3) =", math.ceil(4.3))

#floor() function rounds up a number to the nearest integer
print("floor(4.7) =", math.floor(4.7))

#trunc() function truncates a floating-point number to an integer (Removes decimal part)
print("trunc(4.9) =", math.trunc(4.9))

#factorial() function returns the factorial of a number
print("factorial(5) =", math.factorial(5))

#hypot() function returns the Euclidean norm, sqrt(x*x+y*y)
print("hypot(3,4) =", math.hypot(3,4))

#sqrt() function returns the square root of a number
print("sqrt(25) =", math.sqrt(25))

import random
#Setting seed for reproducibility - meaning it will return same number on every run
#random.seed(123)
#random() function returns a random floating-point number in the range [0.0, 1.0]
print("Random number:", random.random())
#choice function returns a random element from a non-empty sequence
colors = ['red', 'blue', 'green', 'yellow']
print("Random choice from colors:", random.choice(colors))
#sample() function returns a list of unique elements chosen randomly from a population
print("Random sample from colors:", random.sample(colors,2))
#If you want to select with replacement, you can use choices() instead of sample
print("Random choices from colors with replacement:", random.choices(colors,k=3))



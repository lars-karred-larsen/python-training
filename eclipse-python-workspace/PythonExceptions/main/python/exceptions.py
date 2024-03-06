'''
Created on Mar 4, 2024

@author: student
'''
my_list = [1, 2, 3]
try:
    print(my_list[5]) #Accessing an index out of range
except IndexError as e:
    print("IndexError occurred:", e)

my_dict = {'a': 1, 'b': 2}
try:
    print(my_dict['c']) #Accessing non-existent key
except KeyError as e:
    print("KeyError occurred:", e)

try:
    x = 10 + "5" #Adding an integer and a string
except TypeError as e:
    print("TypeError occurred:", e)

try:
    num = int("hello") #Converting letters to integer
except ValueError as e:
    print("ValueError occurred:", e)

try:
    my_list = [1, 2, 3]
    print(my_list[4]) #Accessing an index out of range
except LookupError as e:
    print("LookupError occurred:", e)

try:
    result = 10 / 0 #Dividing with zero
except ArithmeticError as e:
    print("ArithmeticError occurred:", e)

try:
    while True:
        user_input = input("Enter something:")
        print("You entered:", user_input)
except KeyboardInterrupt:
    print("\nProgram interrupted by use. Exiting gracefully.")

import sys
try:
    sys.exit("Exiting the program")
except SystemExit as e:
    print("SystemExit occurred:", e)

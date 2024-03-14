'''
Created on Mar 12, 2024

@author: student
'''
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a century and a leap year")
                return True
            else:
                print(year, "is a century, but not a leap year")
                return False
        else:
            print(year, "is a leap year")
            return True
    else:
        print(year, "is not a leap year")
        return False

def factorial(number):
    #print("\tThe factorial() function was called, number is", number)
    if number == 0 or number == 1:
        #print("\tReturning", str(number))
        return 1
    else:
        #print("\tReturning", str(number) + "*factorial(" + str(number-1) + ")")
        return number*factorial(number-1)

is_leap_year(2001)
num1=10 #999 is maximum recursion depth for current setup 
print("The factorial of", num1, "is",factorial(num1))

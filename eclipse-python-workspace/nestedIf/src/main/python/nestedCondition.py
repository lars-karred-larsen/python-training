'''
Created on Feb 29, 2024

@author: student
'''
year=2103
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0: 
            print(year, "is a century and a leap year")
        else:
            print(year, "is a century, but not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")

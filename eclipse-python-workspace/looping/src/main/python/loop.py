'''
Created on Feb 29, 2024

@author: student
'''
for year in 2000,2100,2103,2104:
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

Year=""
while year != 0:
    year=input("Enter year or type 0 to exit\n")
    year=int(year)
    if year != 0:
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

print("This is last statement of the script")
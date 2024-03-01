'''
Created on Feb 29, 2024

@author: student
'''
city="Chiang Mai"
#city="Berlin"
match city:
    case "Copenhagen":
        print("Country of", city, "is Denmark")
    case "Chiang Mai":
        print("Country of", city, "is Thailand")
    case "London":
        print("Country of", city, "is England")
    case "New York":
        print("Country of", city, "is USA")
    case _:
        print("Country of", city, "is not in list")

        print("This is last statement in case")
print("This is last statement in script")
'''
Created on Feb 29, 2024

@author: student
'''
for number in range(1,21):
    num1=number
    flag=True
    for index in range(2,num1):
        if num1 % index != 0:
            continue # Will continue as long as modulus is not zero
        print(num1, "is not a prime number") #If modulus is zero, number can't be a prime number
        break
    else: #Break never happened
        print(num1,"is a prime number")
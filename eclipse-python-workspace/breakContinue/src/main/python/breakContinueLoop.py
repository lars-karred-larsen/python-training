'''
Created on Feb 29, 2024

@author: student
'''
num1=7
flag=True
for index in range(2,num1):
    if num1 % index != 0:
        continue # Will continue as long as modulus is not zero
    print(num1, "is not a prime number") #If modulus is zero, number can't be a prime number
    flag = False
    break
if flag:
    print(num1,"is a prime number")
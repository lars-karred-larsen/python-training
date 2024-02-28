'''
Created on Feb 28, 2024

@author: student
'''
full_name = "Lars Karred Larsen"
print("Full name is ", full_name)
num1=50
num2=12
print("The numbers are \"num1\"=",num1," \"num2\"=",num2)
print("Addition: ",num1+num2)
print("Subtraction: ",num1-num2)
print("Multiplication: ",num1*num2)
print("Rounded Division: ",round(num1/num2))
print("Division: ",num1/num2)
print("Integer division: ",num1//num2)
print("Modulus: ",num1%num2)
print("Exponential: ",num1**num2)

first_name = "Lars"
middle_name = "Karred"
sir_name = "Larsen"

print("String concatenation: ", first_name + middle_name + sir_name)
print("String concatenation: ", first_name, middle_name, sir_name,sep=" ")

binary_num1 = 0b1110
binary_num2 = 0b1011
print("The binary numbers are \"binary_num1\"=",bin(binary_num1)," (decimal: ",binary_num1, "), \"binary_num2\"=",bin(binary_num2)," (decimal: ",binary_num2, ")",sep="")
print("\"and\" operation: ",end=" ")
print(bin(binary_num1 & binary_num2))
print("\"or\" operation: ",end=" ")
print(bin(binary_num1 | binary_num2))

print("\"num1\" and \"num2\" are equal:",num1==num2)
print("\"num1\" and \"num2\" are not equal:",num1!=num2)
print("\"num1\" is less than \"num2\":",num1<num2)
print("\"num1\" is less than or equal ro \"num2\":",num1<=num2)
print("\"num1\" is greater than \"num2\":",num1>num2)
print("\"num1\" is greater than or equal ro \"num2\":",num1>=num2)

print("\"and\" operator:", True and True)
print("\"or\" operator:", True or False)
print("\"not\" operator:", not True)


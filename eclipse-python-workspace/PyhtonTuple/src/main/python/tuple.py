'''
Created on Mar 1, 2024

@author: student
'''
tuple1=(1,10,20,1)
print(tuple1)
print("Total occurrences of \"1\" is",tuple1.count(1))
print("Length of tuple1 is",len(tuple1))
print("Index position of \"10\" is", tuple1.index(10,0))
print("Index position of \"1\" is", tuple1.index(1))
print("Index position of \"1\" from index \"0\" and onwards is", tuple1.index(1,0))
print("Index position of \"1\" from index \"2\" and onwards is", tuple1.index(1,2))
print("Value at index position \"2\" is", tuple1[2])

'''
Created on Mar 1, 2024

@author: student
'''
list1 = ["apple","orange",1,4,10,1,"John Hammond"]
list2 = [1,10,20,2,30]
list2_reference=list2
list2_copy=list(list2)
list2_copy2=list2[:]
print("List operations")
print("list1 is", list1)
print("Element at index position 4 is",list1[4])
print("List slicing for list1[0:3]", list1[0:3])
print("Total occurrences of 1 in list1 is",list1.count(1))
print("Index position of value 1 in list1 from position 5 and onwards is",list1.index(1,5))
print("Reverse of list1 is",end=" ")
list1.reverse()
print(list1)
print("Appending a value 20")
list1.append(20)
print(list1)
print("Inserting a value 100 at index position 0")
list1.insert(0,100)
print(list1)
print("Sorting of list2 is", end=" ")
list2.sort()
print(list2)
print("Removing first occurrence of vaule 4")
list1.remove(4)
print(list1)
print("Traversing through nested list")
nested_list = [
    [1,2,3,4],
    list2,
    list1
]
for value in nested_list:
    print(value)
print("Clearing list1:")
del list1[:]
print("Length of list1 is", len(list1))
print("The type of list2 is", type(list2))
print("The type of \"0\" is", type(0))
print("Popping index 0 in list2")
pop_value=list2.pop(0)
print("Popped value was:",pop_value)
print("Popping again index 0 in list2")
pop_value=list2.pop(0)
print("Popped value was:",pop_value)
print("Now lis2 looks like this:")
print(list2)
print("This is list2_reference",list2_reference)
print("This is list2_copy",list2_copy)
print("This is list2_copy too",list2_copy2)

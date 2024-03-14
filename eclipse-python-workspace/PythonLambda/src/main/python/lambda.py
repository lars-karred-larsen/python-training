'''
Created on Mar 12, 2024

@author: student
'''
add_lambda = lambda x,y: x + y
print(add_lambda(3, 5)) # Output: 8

def sort_names_by_length(names, key_func):
    print("This is names:", names)
    print("This is key_func:", key_func) 
    return sorted(names, key=key_func)

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Sort the names by their lengths using a lambda function
sorted_names = sort_names_by_length(names, key_func=lambda x: len(x))
print("Sorted names by length:", sorted_names)

#'''
for value in sorted_names:
    print("This is value:", value)
    print("This is index:", value.index)
#'''

# Sort the names in reverse order of the lengths using another lambda function
sorted_names_reverse = sort_names_by_length(names, key_func=lambda x: -len(x))
print("Sorted names by length in reverse order:", sorted_names_reverse)

names = ["Alice", "Bob", "Charlie", "David", "Eve", "Anna", "Alex"]
# Using map() to convert each name to uppercase and filter to keep only names starting with "A"
filtered_names = list(filter(lambda x: x.startswith('A'), map(lambda x: x.upper(), names)))

print(filtered_names)

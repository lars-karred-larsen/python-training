'''
Created on Mar 13, 2024

@author: student
'''
import errno
import os

print("This is current working directory:", os.getcwd())

# Attempt to open a non-existent file
print("Trying to open \"non_existing_file.txt\":")
try:
    with open("non_existing_file.txt", 'r') as file:
        content = file.read()
        print(content)
except IOError as e:
    # Check if the error is due to the file not being found
    if e.errno == errno.ENOENT:
        print("File not found!")
    else:
        print("An error occurred:", e)
        
file_path = "example.txt"
'''
file = open(file_path, "a")

file.write("\nHello World!\n")
file.write("This is a test.\n")
file.write("Python is awesome!\n")

file.close()
'''

file = open(file_path, "r")

content = file.read()
print("Content of the file (using read()):")
print(content)

file.close()

file = open(file_path, "r")

print("\nContent of the file (using readline()):")
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()

file.close()

file = open(file_path, "r")

print("\nContent of the file (using readlines()):")
lines = file.readlines()
for line in lines:
    print(line.strip())

file.close()


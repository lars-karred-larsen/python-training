'''
Created on Mar 1, 2024

@author: student
'''
from xml.etree.ElementPath import find
full_name = "John Hammond doesn\'t wait\nJurassic Park\nJurassic World"
print("String operations")
print("String is",full_name)
print("Character at index position \"2\" is",full_name[2])
print("Length of string \"full_name\" is",len(full_name))
print("Slicing string \"full_name[2:6]\"",full_name[2:6])
print("Second line of string is",full_name.splitlines()[1])
print("Unicode vaule for \"A\" is",ord('A'))
print("Character value for unicode value \"65\" is",chr(65))
print("Looping through string;")
for character in full_name:
    print(character,end="-")
print("")
first_name = "John"
last_name = "Hammondmm"
print("Adding whitespace using \"join\" function")
print((" ".join(first_name)))
print("Using other string with \"join\" function")
print(((" " + last_name + " ").join(first_name)))
print("Splitting string on newlines")
print(full_name.split("\n"))
print("Sorting string", first_name)
print(sorted(first_name))
print("Finding index of substring \"mm\" in\"", last_name,end="\": ")
print(last_name.find("mm"))
print("Finding index of substring \"mm\" in\"", last_name,end="\": ")
print(last_name.index("mm"))
print("Finding index of substring \"mm\" after index \"3\" in\"", last_name,end="\": ")
print(last_name.index("mm",3))
print("Finding index of substring \"mm\" in\"", last_name,end="\": ")
print(last_name.rfind("mm"))
print("Counting string \"mm\" in \"", last_name,end="\": ")
print(last_name.count("mm"))
print("String concatenation", first_name+ last_name)
print("String multiplication",3*"py")
print("Enclosing with double-qoutes to write ' without escape")
print('Enclosing with single-qoutes to write " without escape')


'''
Created on Mar 1, 2024

@author: student
'''
dictionary1={
    "name":"Lars Karred Larsen",
    "age":56,
    "city":"Chiang Mai",
}
print("Dictionary operation")
print("Dictionary is",dictionary1)
print("Dictionary keys are",dictionary1.keys())
print("Dictionary values are",dictionary1.values())
print("Dictionary items are",dictionary1.items())
print("Looping through dictionary")
for key,value in dictionary1.items():
    print(key,value,sep=";")
print("Checking if country exists:", dictionary1.get("country","Key not found"))
print("Adding key \"country\":")
dictionary1["country"]="Thailand"
print("Dictionary is",dictionary1)
print("Checking again if country exists:", dictionary1.get("country","Key not found"))
print("Removing the key \"age\":")
pop_value=dictionary1.pop("age","Key not found")
print("The pop value is", pop_value)
print("Dictionary is",dictionary1)
print("Removing the key \"age\" again:")
pop_value=dictionary1.pop("age","Key not found")
print("The pop value is", pop_value)


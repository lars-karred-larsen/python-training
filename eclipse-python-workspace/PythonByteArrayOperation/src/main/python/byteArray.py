'''
Created on Mar 13, 2024

@author: student
'''
# Simulate binary datato be written to a file 
binary_data = b'Hello, World!\nThis is a test.\nPython is awesome!\n'

# Create a byte array buffer to store binary data
buffer = bytearray(len(binary_data))
#buffer = bytearray(10) # Why doesn't this affect output?

# Write binary data to the buffer
buffer[:len(binary_data)] = binary_data
#buffer[:10] = binary_data # Why doesn't this affect output?

# Display the contents of the buffer
print("Initial buffer contents:")
print(buffer)

# Open the file for writing in binary mode
with open("output.bin", "wb") as file:
    # Write the buffer contents to the file
    file.write(buffer)
    
# Clear the buffer
buffer.clear()

# Open the file for reading in binary mode
with open("output.bin", "rb") as file:
    # Read data from the file into the buffer
    file.readinto(buffer)
    content = file.read()
    print(content)
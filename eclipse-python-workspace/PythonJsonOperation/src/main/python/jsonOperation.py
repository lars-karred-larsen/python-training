'''
Created on Mar 13, 2024

@author: student
'''
import os
import json

# Define the path to the JSON file
file_path = "example.json"

# Check if the file exists
if os.path.exists(file_path):
    # Read JSON data from file
    with open(file_path) as lakl_json_file:
        data = json.load(lakl_json_file)
        
    # Insert or update a key-value pair
    data['country'] = "Thailand"
    
    # Delete a key-value pair
    if "city" in data:
        del data["city"]
    else:
        data['city'] = "Chiang Mai"
        
    # Write modified data back to file
    with open(file_path, "w") as any_filename_will_do:
        json.dump(data, any_filename_will_do, indent = 4)
else:
    print("File doesn't exist.")
    

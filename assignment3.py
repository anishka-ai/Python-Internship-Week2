#Assignment 3: JSON File Reader
#Aim: To load JSON data from a file and print it in a formatted way using Python.

import json
import os

file_path= os.path.join(os.path.dirname(__file__), "data.json")
with open(file_path, "r" , encoding="utf-8") as file:
    data = json.load(file)

print("Formatted JSON Data:")
print(json.dumps(data, indent=4))
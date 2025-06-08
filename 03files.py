
# File read and write

# Writing to a file
with open("sample.txt", "w") as f:
    f.write("Hello, world!\nThis is a sample file.")

# Reading from a file
with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

# File delete, copy, move, rename
import os
import shutil

# Copy file
shutil.copy("sample.txt", "sample_copy.txt")

# Rename file
os.rename("sample_copy.txt", "sample_renamed.txt")

# Move file
shutil.move("sample_renamed.txt", "moved_sample.txt")

# Delete file
os.remove("moved_sample.txt")

# Exception handling
try:
    with open("nonexistent.txt", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print("Error:", e)

# CSV operations
import csv

# Write to CSV
with open("sample.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 24])
    writer.writerow(["Bob", 30])

# Read from CSV
with open("sample.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print("CSV row:", row)

# JSON operations
import json

data = {"name": "Alice", "age": 24}

# Write to JSON
with open("sample.json", "w") as jsonfile:
    json.dump(data, jsonfile)

# Read from JSON
with open("sample.json", "r") as jsonfile:
    loaded_data = json.load(jsonfile)
    print("JSON data:", loaded_data)

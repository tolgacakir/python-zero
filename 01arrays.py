#arrays
numbers = [2,8,6,4,10,5,9,1,3,7]


numbers.append(12)
numbers.append(11)
numbers.append(13)
numbers.append(15)
numbers.append(14)

print(numbers)

selected_number = numbers[0]
box = 0

for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            box = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = box

print(numbers)

# set: unique elements, unordered, not indexed
unique_numbers = { 4,1,2,9,8}
print("unique numbers: ", unique_numbers)
#print(unique_numbers[0])  # This will raise an error because sets do not support indexing


# tuple: immutable, ordered, allows duplicates, indexed
coordinates = (1, 3, 2, 5)
#coordinates[2]=2# This line will raise an error because tuples are immutable and cannot be modified
print("tuple: ", coordinates)
print(coordinates[2])


# dictionary: key-value pairs, unordered, mutable
student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Science", "History"]
}
print("student: ", student)

phonebook = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}
print("phonebook: ", phonebook)
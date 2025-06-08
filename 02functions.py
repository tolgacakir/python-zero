# Default değeri olan parametre alan, return değeri olmayan fonksiyon
def greeting(name="Unknown"):
    print("Hello, World" + " " + name + "!")

greeting()
greeting("John")

# 2 parametre alan, return değeri olan fonksiyon
def add_numbers(num1, num2):
    return num1 + num2
print(add_numbers(5, 10))
print(add_numbers(num1 = 5, num2 = 10))

# Function with no parameters and no return value
def say_hello():
    print("Hello!")

say_hello()

# Function with multiple parameters and a return value
def multiply(a, b):
    return a * b

result = multiply(3, 4)
print("Multiplication result:", result)

# Function with a docstring
def divide(a, b):
    """
    Returns the result of dividing a by b.
    """
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

print(divide(10, 2))
print(divide(5, 0))

# Function with variable number of arguments
def print_names(*names):
    for name in names:
        print("Name:", name)

print_names("Alice", "Bob", "Charlie")

# Function with keyword arguments
def describe_person(name, age, city="Unknown"):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person("Eve", 30, city="London")
describe_person("Tom", 25)

# Example with map: Get the squares of a list of numbers
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# Example with filter: Filter even numbers from a list
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# Example with reduce: Get the product of all numbers in a list
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)

# Example with zip: Combine two lists into a list of tuples
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 22]
zipped = list(zip(names, ages))
print("Names and ages:", zipped)


message = "Hello, World!"
print(message)

number1 = 5
number2 = 10
sum_result = number1 + number2
print(f"The sum of {number1} and {number2} is {sum_result}.")

name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the program.")

veight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in centimeters: ")) * 0.01
bmi = veight / (height ** 2)
print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
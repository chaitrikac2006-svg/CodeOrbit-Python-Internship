# Display calculator title
print("Simple Calculator")

# Get the first number from the user
num1 = float(input("Enter first number: "))

# Get the second number from the user
num2 = float(input("Enter second number: "))

# Perform arithmetic operations
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

# Handle division safely
try:
    print("Division:", num1 / num2)
except ZeroDivisionError:
    print("Cannot divide by zero.")

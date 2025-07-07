# @title 1. Basic Calculator

"""
A basic calculator is one of the fundamental
projects in Python programming. It provides essential
arithmetic operations such as addition, subtraction,
multiplication, and division. Understanding how to
implement a calculator helps in learning user input
handling, conditional statements, and function creation in
Python.

Key Concepts of Basic Calculator in Python
 Arithmetic Operations:
 Addition ( + )
 Subtraction (- )
 Multiplication ( * )
 Division ( / )
 Modulus ( % )
 Exponentiation ( ** )
 User Input Handling:
 Using input() function
 Converting strings to integers or floats
 Functions in Python:
 Defining functions for calculations
 Calling functions with user inputs
 Error Handling:
 Parameter Table
 Operator
 Handling division by zero
 Handling invalid inputs
 """

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract second number from first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide first number by second
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Function to get the square root by second number
def sqrt(a, b):
    if b == 2:
        return a**(1/b)
    else:
        return "BASIC CALCULATOR..."

# Function to get an exponentiation that raises a to the power of b
def power(a, b):
    if a == 0 and b == 0:
        return "Error"
    else:
        return a**b

# Main calculator loop
while True:
    print("\n" + "="*30)
    print("     BASIC CALCULATOR MENU     ")
    print("="*30)
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root")
    print("6. Exponentiation")
    print("7. Exit")

    # Take input from the user for operation choice
    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice == '7':
        print("Thank you for using the calculator. Goodbye!")
        break

    try:
        # Get two numbers as input from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    # Perform calculation based on user's choice
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", sqrt(num1, num2))
    elif choice == '6':
        print("Result:", power(num1, num2))
    else:
        print("Invalid choice. Please select a valid option.")

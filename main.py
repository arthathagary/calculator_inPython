import math
import sys


# Addition
def add(x, y):
    return x + y


# Subtraction
def subtract(x, y):
    return x - y


# Multiplication
def multiply(x, y):
    return x * y


# Division
def divide(x, y):
    if y == 0:
        raise ValueError("You can't divide number by 0 ")
    return x / y


def main():
    print("Select A Option:")
    print("1. Add Numbers")
    print("2. Subtract Numbers")
    print("3. Multiply Numbers")
    print("4. Divide Numbers")
    print("5. Exit The Program")

    choice = input("Enter choice (1/2/3/4/5): ")
    if choice == '5':
        sys.exit("Program is ended")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choice == '5':
        sys.exit("Program is ended")
    else:
        print("Invalid choice")
        return

    print("Result:", result)
    main()


if __name__ == "__main__":
    main()

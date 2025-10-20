# calculator.py
# Author: Rajeshwari Mukunda | BFSI Domain Practice Project

# Step 1: Define functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed!"
    return x / y


# Step 2: Create a function to display the menu
def show_menu():
    print("\n===== Simple CLI Calculator =====")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")


# Step 3: Main loop to take user input
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        # Exit condition
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Validate input
        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice! Please enter a number between 1 and 5.")
            continue

        # Take numbers as input
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Perform the operation
        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} ÷ {num2} = {divide(num1, num2)}")


# Step 4: Run the program
if __name__ == "__main__":
    main()

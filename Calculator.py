# Function to perform calculations based on the operation
def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operation choice."

# Main function to run the calculator
def main():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        # Take input from the user
        operation = input("Enter operation choice (1/2/3/4): ")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform calculation and display the result
        result = calculate(num1, num2, operation)
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the main function
if __name__ == "__main__":
    main()

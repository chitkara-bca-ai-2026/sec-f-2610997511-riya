
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
def modulus(a, b):
    if b == 0:
        return "Error: Cannot find remainder with zero"
    return a % b
def power(base, exp=2):
    return base ** exp


history = []

print("==========================================")
print("       ENTERPRISE MODULAR UTILITY CALCULATOR")
print("==========================================")

while True:
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (Remainder %)")
    print("6. Power / Exponentiation (default: Square)")
    print("7. View Calculation History")
    print("8. Exit")

    choice = int(input("\nEnter your choice (1-8): "))
    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = add(a, b)
        print("Result:", result)
        history.append("Addition: " + str(a) + " + " + str(b) + " = " + str(result))
    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = subtract(a, b)
        print("Result:", result)
        history.append("Subtraction: " + str(a) + " - " + str(b) + " = " + str(result))
    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = multiply(a, b)
        print("Result:", result)
        history.append("Multiplication: " + str(a) + " * " + str(b) + " = " + str(result))
    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = divide(a, b)
        print("Result:", result)
        history.append(
            "Division: " + str(a) + " / " + str(b) + " = " + str(result)
        )
    elif choice == 5:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = modulus(a, b)
        print("Result:", result)
        history.append(
            "Modulus: " + str(a) + " % " + str(b) + " = " + str(result)
        )
    elif choice == 6:
        base = float(input("Enter base: "))
        exponent = input("Enter exponent (press Enter for square): ")
        if exponent == "":
            result = power(base)
            text = str(base) + "^2 = " + str(result)
        else:
            exponent = float(exponent)
            result = power(base, exponent)
            text = str(base) + "^" + str(exponent) + " = " + str(result)
        print("Result:", result)
        history.append("Power: " + text)
    elif choice == 7:
        print("\n--- Calculation History ---")
        if len(history) == 0:
            print("No calculations performed yet.")
        else:
            for item in history:
                print(item)
    elif choice == 8:
        print("\nThank you for using Utility Calculator.")
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1 to 8.")
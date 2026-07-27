# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# (instructions as given)
#

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    return a ** b


def get_two_numbers():
    try:
        a = float(input("Enter first number : "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Error: please enter valid numbers.")
        return None


def print_menu():
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main():
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("%", modulus),
        "6": ("**", exponentiate),
    }

    while True:
        print_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Error: invalid choice. Please enter a number from 1 to 7.")
            print()
            continue

        symbol, func = operations[choice]

        numbers = get_two_numbers()
        if numbers is None:
            print()
            continue

        a, b = numbers

        if choice in ("4", "5") and b == 0:
            print("Error: Cannot divide by zero.")
            print()
            continue

        result = func(a, b)

        # Print integers without a trailing .0 for cleaner output
        a_display = int(a) if a.is_integer() else a
        b_display = int(b) if b.is_integer() else b

        print(f"Result: {a_display} {symbol} {b_display} = {result}")
        print()


if __name__ == "__main__":
    main()
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# (instructions as given)
#

def print_single_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number}  x  {i:<2} =  {number * i}")


def print_tables_up_to_n(n):
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    for number in range(1, n + 1):
        print_single_table(number)
        print("---------------------------")


def main():
    # Part A
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Error: please enter a valid integer.")
        return

    print_single_table(number)

    print()

    # Part B
    try:
        n = int(input("Enter N (for tables 1 to N): "))
    except ValueError:
        print("Error: please enter a valid integer.")
        return

    print_tables_up_to_n(n)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
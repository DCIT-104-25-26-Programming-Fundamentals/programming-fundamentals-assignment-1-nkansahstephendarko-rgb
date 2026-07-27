# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# (instructions as given)
#

def print_fibonacci_terms(n):
    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    print("Fibonacci sequence:", " ".join(str(num) for num in sequence))


def is_fibonacci_number(num):
    if num < 0:
        return False

    a, b = 0, 1
    while a < num:
        a, b = b, a + b

    return a == num


def main():
    # Part A
    try:
        n = int(input("How many terms? "))
    except ValueError:
        print("Error: N must be a positive integer.")
        return

    print_fibonacci_terms(n)

    print()

    # Part B
    try:
        num = int(input("Enter a number to check: "))
    except ValueError:
        print("Error: please enter a valid integer.")
        return

    if is_fibonacci_number(num):
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()
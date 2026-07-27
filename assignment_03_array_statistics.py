# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# (instructions as given)
#

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def main():
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: Number of values must be a positive integer.")
        return

    numbers = []
    for i in range(n):
        value = int(input(f"Enter number {i + 1}: "))
        numbers.append(value)

    print()
    print("Results:")
    print(f"Sum:     {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Maximum: {find_max(numbers)}")
    print(f"Minimum: {find_min(numbers)}")


if __name__ == "__main__":
    main()
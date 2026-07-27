# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# (instructions as given)
#

def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        line = "".join(f"{val:5}" for val in row)
        print(line)


def transpose_matrix(matrix, rows, cols):
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


def add_matrices(a, b, rows, cols):
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(a[i][j] + b[i][j])
        result.append(new_row)
    return result


def multiply_matrices(a, rows_a, cols_a, b, rows_b, cols_b):
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


def main():
    print("Matrix Operations Menu:")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")
    choice = int(input("Enter choice (1-3): "))

    if choice == 1:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        matrix = read_matrix(rows, cols)
        result = transpose_matrix(matrix, rows, cols)

        print()
        print("Original Matrix:")
        print_matrix(matrix)
        print()
        print("Transposed Matrix:")
        print_matrix(result)

    elif choice == 2:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        print()
        print("Enter Matrix A:")
        a = read_matrix(rows, cols)
        print("Enter Matrix B:")
        b = read_matrix(rows, cols)

        result = add_matrices(a, b, rows, cols)

        print()
        print("Sum Matrix:")
        print_matrix(result)

    elif choice == 3:
        rows_a = int(input("Enter rows of Matrix A: "))
        cols_a = int(input("Enter columns of Matrix A: "))
        rows_b = int(input("Enter rows of Matrix B: "))
        cols_b = int(input("Enter columns of Matrix B: "))

        if cols_a != rows_b:
            print("Error: Columns of A must equal rows of B for multiplication.")
            return

        print()
        print("Enter Matrix A:")
        a = read_matrix(rows_a, cols_a)
        print("Enter Matrix B:")
        b = read_matrix(rows_b, cols_b)

        result = multiply_matrices(a, rows_a, cols_a, b, rows_b, cols_b)

        print()
        print("Product Matrix (A x B):")
        print_matrix(result)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
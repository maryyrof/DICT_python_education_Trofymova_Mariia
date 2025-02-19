def read_matrix():
    """
    Зчитує матрицю з вводу користувача.

    Повертає:
        tuple: (int, int, list) — кількість рядків, кількість стовпців, матриця у вигляді списку списків.
    """
    n, m = map(int, input("Enter matrix size: > ").split())
    print("Enter matrix:")
    matrix = [list(map(float, input("> ").split())) for _ in range(n)]
    return n, m, matrix


def add_matrices():
    """
    Зчитує дві матриці та додає їх, якщо вони мають однакові розміри.

    Виводить:
        Результуючу матрицю або повідомлення про неможливість виконання операції.
    """
    n1, m1, a = read_matrix()
    n2, m2, b = read_matrix()

    if n1 != n2 or m1 != m2:
        print("The operation cannot be performed.")
        return

    result = [[a[i][j] + b[i][j] for j in range(m1)] for i in range(n1)]

    print("The result is:")
    for row in result:
        print(*row)


def multiply_matrix_by_constant():
    """
    Зчитує матрицю та множить її на введену константу.

    Виводить:
        Результуючу матрицю.
    """
    n, m, matrix = read_matrix()
    k = float(input("Enter constant: > "))

    result = [[matrix[i][j] * k for j in range(m)] for i in range(n)]

    print("The result is:")
    for row in result:
        print(*row)


def multiply_matrices():
    """
    Зчитує дві матриці та перемножує їх, якщо вони сумісні для множення.

    Виводить:
        Результуючу матрицю або повідомлення про неможливість множення.
    """
    n1, m1, a = read_matrix()
    n2, m2, b = read_matrix()

    if m1 != n2:
        print("The operation cannot be performed.")
        return

    result = [[sum(a[i][k] * b[k][j] for k in range(m1)) for j in range(m2)] for i in range(n1)]

    print("The result is:")
    for row in result:
        print(*row)


def transpose_matrix():
    """
    Зчитує матрицю та транспонує її залежно від вибору користувача.

    Виводить:
        Транспоновану матрицю або повідомлення про невірний вибір.
    """
    n, m, matrix = read_matrix()

    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    choice = input("Your choice: > ").strip()

    if choice == "1":
        result = [[matrix[j][i] for j in range(n)] for i in range(m)]
    elif choice == "2":
        result = [[matrix[n - j - 1][m - i - 1] for j in range(n)] for i in range(m)]
    elif choice == "3":
        result = [row[::-1] for row in matrix]
    elif choice == "4":
        result = matrix[::-1]
    else:
        print("Invalid choice.")
        return

    print("The result is:")
    for row in result:
        print(*row)


def determinant(matrix):
    """
    Обчислює визначник квадратної матриці.

    Аргументи:
        matrix (list[list[float]]): Вхідна квадратна матриця.

    Повертає:
        float: Визначник матриці.
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        submatrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(submatrix)
    return det


def calculate_determinant():
    """
    Зчитує квадратну матрицю та обчислює її визначник.

    Виводить:
        Значення визначника або повідомлення про помилку, якщо матриця не квадратна.
    """
    n, m, matrix = read_matrix()

    if n != m:
        print("The operation cannot be performed.")
        return

    result = determinant(matrix)

    print("The result is:")
    print(result)


def inverse_matrix():
    """
    Зчитує квадратну матрицю та обчислює її обернену, якщо вона існує.

    Виводить:
        Обернену матрицю або повідомлення про те, що обернена матриця не існує.
    """
    n, m, matrix = read_matrix()

    if n != m:
        print("This matrix doesn't have an inverse.")
        return

    det = determinant(matrix)
    if det == 0:
        print("This matrix doesn't have an inverse.")
        return

    # Обчислення матриці алгебраїчних доповнень
    cofactors = []
    for i in range(n):
        row = []
        for j in range(n):
            minor = [matrix[x][:j] + matrix[x][j+1:] for x in range(n) if x != i]
            row.append(((-1) ** (i + j)) * determinant(minor))
        cofactors.append(row)

    # Транспонування матриці алгебраїчних доповнень
    cofactors = [[cofactors[j][i] for j in range(n)] for i in range(n)]

    # Ділення на визначник
    inverse = [[cofactors[i][j] / det for j in range(n)] for i in range(n)]

    print("The result is:")
    for row in inverse:
        print(*map(lambda x: f"{x:.2f}", row))  # Форматування до 2 знаків після коми


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    my_choice = input("Your choice: > ").strip()

    if my_choice == "1":
        add_matrices()
    elif my_choice == "2":
        multiply_matrix_by_constant()
    elif my_choice == "3":
        multiply_matrices()
    elif my_choice == "4":
        transpose_matrix()
    elif my_choice == "5":
        calculate_determinant()
    elif my_choice == "6":
        inverse_matrix()
    elif my_choice == "0":
        break
    else:
        print("Invalid choice. Try again.")
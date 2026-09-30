"""Исходная система"""
A = [[-6.0, -8.0, -2.0, -8],
    [9.0, 0.0, 8.0, 3.0],
    [0, -9.0, -5.0, 9.0],
    [-1.0, 4.0, -8.0, -4.0]]

b = [-32,
     8.0,
     -2.0,
     -36.0]

def gauss_solve(A, b):
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    E = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    det = 1.0

    """Прямой ход"""
    for i in range(n):
        pivot_row = i
        max_val = abs(M[i][i])
        for k in range(i + 1, n):
            if abs(M[k][i]) > max_val:
                max_val = abs(M[k][i])
                pivot_row = k

        if pivot_row != i:
            M[i], M[pivot_row] = M[pivot_row], M[i]
            E[i], E[pivot_row] = E[pivot_row], E[i]
            det *= -1

        lead_elem = M[i][i]
        det *= lead_elem

        for j in range(n + 1):
            M[i][j] /= lead_elem
        for j in range(n):
            E[i][j] /= lead_elem

        for k in range(n):
            if k != i:
                factor = M[k][i]
                if factor == 0:
                    continue

                for j in range(n + 1):
                    M[k][j] -= factor * M[i][j]
                for j in range(n):
                    E[k][j] -= factor * E[i][j]

    x = [M[i][n] for i in range(n)]
    A_inv = E

    return x, det, A_inv

def print_matrix(matrix, name="Матрица"):
    print(f"{name}:")
    for row in matrix:
        print("[ " + "  ".join(f"{val:8.4f}" for val in row) + " ]")
    print()

"""Решение"""
try:
    x, det, A_inv = gauss_solve(A, b)
    print("Вектор решений (x1, x2, x3, x4):")
    for i, val in enumerate(x):
        print(f"x{i + 1} = {val:.5f}")
    print()
    print(f"Определитель матрицы: {det:.5f}")
    print()
    print("Обратная матрица:", A_inv)
except ValueError as e:
    print(e)
import numpy as np
import matplotlib.pyplot as plt

# Часть 1
# Исходные данные для кубического сплайна (5 точек)
X = [-3, -1, 1, 3, 5]
Y = [-4.2490, -1.7854, 1.7854, 4.2490, 6.3734]
x0 = -0.5
y0 = ()

h = [X[i] - X[i - 1] for i in range(1, 5)]

A = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(3):
    for j in range(3):
        if i == j:
            A[i][j] = 2 * (h[i] + h[i + 1])
        if i == j - 1 or i == j + 1:
            A[i][j] = h[max(i, j)]

def r(t):
    return (Y[t + 1] - Y[t]) / h[t]


B = [3 * (r(i + 1) - r(i)) for i in range(3)]

# Решение системы A * c = B методом прогонки
alpha = [((-1) * A[0][1] / A[0][0])]
beta = [(B[0] / A[0][0])]

for i in range(1, 2):
    alpha.append((-1) * A[i][i + 1] / (A[i][i] + alpha[i - 1] * A[i][i - 1]))
    beta.append((B[i] - A[i][i - 1] * beta[i - 1]) / (A[i][i] + alpha[i - 1] * A[i][i - 1]))

c = [(B[2] - A[2][1] * beta[1]) / (A[2][2] + A[2][1] * alpha[1])]

for j in range(2, 0, -1):
    c.insert(0, (alpha[j - 1] * c[0] + beta[j - 1]))
c.insert(0, 0)

a = [Y[i] for i in range(4)]
b = [r(i) - 1 / 3 * h[i] * (c[i + 1] + 2 * c[i]) for i in range(3)] + [r(3) - 2 / 3 * h[3] * c[3]]
d = [(c[i + 1] - c[i]) / h[i] / 3 for i in range(3)] + [c[3] / (-3) / h[3]]

x1 = np.array(X)

# Построение сплайна
fig, ax = plt.subplots(figsize=(10, 6))

for i in range(4):
    x = np.linspace(X[i], X[i + 1], 25)
    y = a[i] + b[i] * (x - X[i]) + c[i] * (x - X[i]) ** 2 + d[i] * (x - X[i]) ** 3
    ax.plot(x, y, 'b-', lw=2, label='Кубический сплайн' if i == 0 else "")
    if (x0 >= X[i]) and (x0 <= X[i + 1]):
        y0 = a[i] + b[i] * (x0 - X[i]) + c[i] * (x0 - X[i]) ** 2 + d[i] * (x0 - X[i]) ** 3
        print('Значение функции в точке X* = - 0.5 равно', y0)

ax.plot(x0, y0, 'ro', markersize=6, label='Точка X*')

# Часть 2
# Исходные данные
X_2= np.array([-5.0, -3.0, -1.0, 1.0, 3.0, 5.0])
Y_2 = np.array([-6.3734, -4.249, -1.7854, 1.7854, 4.249, 6.3734])
ax.plot(X_2, Y_2, 'ko', markersize=6, label='Исходные точки')

n = len(X_2)
Sx = np.sum(X_2)
Sx2 = np.sum(X_2**2)
Sy = np.sum(Y_2)
Sxy = np.sum(X_2 * Y_2)

A1 = np.array([[n, Sx], [Sx, Sx2]])
B1 = np.array([Sy, Sxy])
coeffs1 = np.linalg.solve(A1, B1)
a0, a1 = coeffs1

Sx3 = np.sum(X_2**3)
Sx4 = np.sum(X_2**4)
Sx2y = np.sum(X_2**2 * Y_2)

A2 = np.array([[n, Sx, Sx2],
               [Sx, Sx2, Sx3],
               [Sx2, Sx3, Sx4]])
B2 = np.array([Sy, Sxy, Sx2y])
coeffs2 = np.linalg.solve(A2, B2)
b0, b1, b2 = coeffs2

# Вычисление суммы квадратов ошибок Ф
# Для полинома 1-й степени
y_pred1 = a0 + a1 * X_2
Phi1 = np.sum((Y_2 - y_pred1)**2)

# Для полинома 2-й степени
y_pred2 = b0 + b1 * X_2 + b2 * X_2**2
Phi2 = np.sum((Y_2 - y_pred2)**2)

print(f'Полином 1-й степени: y = {a0:.4f} + {a1:.4f} * x')
print(f'Сумма квадратов ошибок Ф1 = {Phi1:.6f}')
print(f'Полином 2-й степени: y = {b0:.4f} + {b1:.4f} * x + {b2:.4f} * x^2')
print(f'Сумма квадратов ошибок Ф2 = {Phi2:.6f}')

# Построение графиков полиномов
x_plot = np.linspace(min(X_2), max(X_2), 200)
y_plot1 = a0 + a1 * x_plot
y_plot2 = b0 + b1 * x_plot + b2 * x_plot**2

ax.plot(x_plot, y_plot1, 'g--', lw=2, label='Полином 1-й степени')
ax.plot(x_plot, y_plot2, 'm-.', lw=2, label='Полином 2-й степени')

# Настройки графика
ax.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
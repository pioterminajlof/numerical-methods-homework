# Исходные данные
dy0 = 0
x0 = 1
x1 = 3

def dy3(y3, z3):
    return y3 - z3 - 31 / 9

# dz
def f(x, y, z):
    return (2 * y - 2 * (x + 1) * z) / (x * (2 * x + 1))

# Метод стрельбы
# dy
def g(x, y, z):
    return z

h = 0.2
X = [x0 + i * h for i in range(int((x1 - x0) / h) + 1)]

def koshi(n_val):
    Y = [n_val]
    Z = [dy0]
    for i in range(1, len(X)):
        k1 = h * g(X[i - 1], Y[i - 1], Z[i - 1])
        l1 = h * f(X[i - 1], Y[i - 1], Z[i - 1])
        k2 = h * g(X[i - 1] + h / 2, Y[i - 1] + k1 / 2, Z[i - 1] + l1 / 2)
        l2 = h * f(X[i - 1] + h / 2, Y[i - 1] + k1 / 2, Z[i - 1] + l1 / 2)
        k3 = h * g(X[i - 1] + h / 2, Y[i - 1] + k2 / 2, Z[i - 1] + l2 / 2)
        l3 = h * f(X[i - 1] + h / 2, Y[i - 1] + k2 / 2, Z[i - 1] + l2 / 2)
        k4 = h * g(X[i - 1] + h, Y[i - 1] + k3, Z[i - 1] + l3)
        l4 = h * f(X[i - 1] + h, Y[i - 1] + k3, Z[i - 1] + l3)
        Y.append(Y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)
        Z.append(Z[i - 1] + (l1 + 2 * l2 + 2 * l3 + l4) / 6)
    return Y, Z

e = 0.0001
n0 = 2.0  # начальное приближение для y(x0)
n1 = 4.0  # второе приближение

Y, Z = koshi(n0)
F0 = dy3(Y[-1], Z[-1])
Y, Z = koshi(n1)
F1 = dy3(Y[-1], Z[-1])

c = 0
while abs(F1) > e:
    if F1 - F0 == 0:
        break
    n2 = n1 - F1 * (n1 - n0) / (F1 - F0)
    n0, F0 = n1, F1
    n1 = n2
    Y, Z = koshi(n1)
    F1 = dy3(Y[-1], Z[-1])
    c += 1

# Ответ
print('Метод стрельбы:')
print("X  =", [round(x, 3) for x in X])
print("Y  =", [round(y, 6) for y in Y])

# Конечно-разностный метод
N = len(X)

# Cистема уравнений
a = [0.0] * N
b = [0.0] * N
c = [0.0] * N
d = [0.0] * N

xi = X[0]
a_0 = xi * (2 * xi + 1) - (xi + 1) * h
b_0 = -2 * xi * (2 * xi + 1) - 2 * h ** 2
c_0 = xi * (2 * xi + 1) + (xi + 1) * h
b[0] = b_0
c[0] = a_0 + c_0
d[0] = 0.0

a[N - 1] = 1.0 / h
b[N - 1] = 1.0 - 1.0 / h
d[N - 1] = 31.0 / 9.0

for i in range(1, N - 1):
    xi = X[i]
    a[i] = xi * (2 * xi + 1) - (xi + 1) * h
    b[i] = -2 * xi * (2 * xi + 1) - 2 * h ** 2
    c[i] = xi * (2 * xi + 1) + (xi + 1) * h
    d[i] = 0.0

# Решение системы методом прогонки
alpha_kr = [0.0] * N
beta_kr = [0.0] * N

alpha_kr[0] = -c[0] / b[0]
beta_kr[0] = d[0] / b[0]

for i in range(1, N):
    de = b[i] + a[i] * alpha_kr[i - 1]
    if i < N - 1:
        alpha_kr[i] = -c[i] / de
    beta_kr[i] = (d[i] - a[i] * beta_kr[i - 1]) / de

y_kr = [0.0] * N
y_kr[N - 1] = beta_kr[N - 1]

for i in range(N - 2, -1, -1):
    y_kr[i] = alpha_kr[i] * y_kr[i + 1] + beta_kr[i]

# Ответ
print('Конечно-разностный метод:')
print("X  =", [round(x, 3) for x in X])
print("Y  =", [round(y, 6) for y in y_kr])
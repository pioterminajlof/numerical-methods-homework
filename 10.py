# Исходные данные
def f(x, y):
    return -y / x - x ** 2
x1 = 1
x2 = 2
h = 0.1
X = [x1 + i * h for i in range (int((x2 - x1) / h) + 1)]
y0 = 0.75
x0 = 1
Y = [y0]
print('X =',[round(i, 3) for i in X])
print ()

# Метод Эйлера
for i in range (1, len (X)):
    Y.append (Y[i - 1] + h * f(X[i - 1], Y[i - 1]))
print ('Метод Эйлера:')
print('Y =', [round(i, 9) for i in Y])
print ()

# Первый улучшенный метод Эйлера
Y = [y0]
for i in range(1, len (X)):
    y05 = Y[i - 1] + h/2 * f(X[i - 1], Y[i - 1])
    x05 = X[i - 1] + h/2
    y_ = Y[i - 1] + h * (f(x05, y05))
    Y.append(y_)
print('Первый улучшенный метод Эйлера:')
print('Y =', [round(i, 9) for i in Y])
print ()

# Метод Рунге-Кутты 4 порядка
Y = [y0]
for i in range(1, len (X)):
    k1 = h * f(X[i - 1], Y[i - 1])
    k2 = h * f(X[i - 1] + h/2, Y[i - 1] + k1/2)
    k3 = h * f(X[i - 1] + h/2, Y[i - 1] + k2/2)
    k4 = h * f(X[i - 1] + h, Y[i - 1] + k3)
    dy = (k1 + 2 * k2 + 2 * k3 + k4) / 6
    y_ = Y[i - 1] + dy
    Y.append(y_)
print('Метод Рунге-Кутты 4 порядка:')
print('Y =', [round(i, 9) for i in Y])
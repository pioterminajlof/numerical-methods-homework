import math

#Исходная система
def f1(x1, x2):
     return x1 ** 2 - 2 * math.log10(x2) - 1
def f2(x1, x2):
     return  x1 ** 2 - 3 * x1 * x2 + 3

#Производные функций
def df11(x1, x2):
    return 2 * x1
def df12(x1, x2):
    return -2 * (1 / (x2 * math.log(10)))
def df21(x1, x2):
    return 2 * x1 - 3 * x2
def df22(x1, x2):
    return -3 * x1

def det_j (x1, x2):
     return df11(x1, x2) * df22(x1, x2) - df21(x1, x2) * df12(x1, x2)
def det_a1 (x1, x2):
     return f1(x1, x2) * df22(x1, x2) - f2(x1, x2) * df12(x1, x2)
def det_a2 (x1, x2):
     return df11(x1, x2) * f2(x1, x2) - df22(x1, x2) * f1(x1, x2)

#Нулевое приближение
x = [[1],
     [1]]

c = 0

#Решение
while True:
     c += 1
     x[0] += [x[0][c-1] - (det_a1(x[0][c-1], x[1][c-1]) / det_j(x[0][c-1], x[1][c-1]))]
     x[1] += [x[1][c-1] - (det_a2(x[0][c-1], x[1][c-1]) / det_j(x[0][c-1], x[1][c-1]))]

     if max(abs(x[0][c] - x[0][c-1]), abs(x[1][c] - x[1][c-1])) <= 0.0001:
          # Ответ
          print('Метод Ньютона (', c, 'итераций, eps = 0.0001 ):')
          print('x1 =', x[0][c] - (det_a1(x[0][c], x[1][c]) / det_j(x[0][c], x[1][c])))
          print('x2 =', x[1][c] - (det_a2(x[0][c], x[1][c]) / det_j(x[0][c], x[1][c])))
          break

#Метод простой итерации
#Функции fi1 и fi2 (выражены из исходных уравнений)
def fi1(x1, x2):
     return (2 * math.log10(x2) + 1) ** 0.5
def fi2(x1, x2):
     return (x1 ** 2 + 3) / (3 * x1)

x = [[1],
     [1]]

c = 0

#Решение
while True:
     c += 1
     x[0] += [fi1(x[0][c-1], x[1][c-1])]
     x[1] += [fi2(x[0][c-1], x[1][c-1])]
     if max(abs(x[0][c] - x[0][c-1]), abs(x[1][c] - x[1][c-1])) <= 0.0001:
          # Ответ
          print('Метод простой итерации (', c, 'итераций, eps = 0.0001 ):')
          print('x1 =', fi1(x[0][c], x[1][c]))
          print('x2 =', fi2(x[0][c], x[1][c]))
          break
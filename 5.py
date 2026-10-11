import math
'''from autograd import grad'''

#Исходная функция
def f(r):
     return 3 * (r + 1) ** 0.5 - math.e ** r - 0.5

#Производная функции
'''df = grad(f)'''
def df(r):
    return 3 / (2 * math.sqrt(r + 1)) - math.e ** r

x0 = 1.2
x = [0, x0]
c = 0

#Решение
while abs(x[c + 1] - x[c]) >= 0.001:
     c += 1
     x += [x[c] - (f(x[c]) / df(x[c]))]

#Ответ
print ('Метод Ньютона (', c, 'итерации ):')
print ('x =', x[c + 1])
print ()

#Метод простой итерации
#Функция fi (выражена из исходного уравнения)
def fi(t):
     return math.log(3 * math.sqrt(t + 1) - 0.5)

x0 = 1.0
x = [0, x0]
c = 0

#Решение
while abs(x[c + 1] - x[c]) >= 0.001:
     c += 1
     x += [fi(x[c])]

#Ответ
print('Метод простой итерации (', c, 'итераций ):')
print('x =', x[c + 1])

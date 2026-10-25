import math
import sympy as sp
x = sp.symbols('x')

#Исходные данные
def f(s):
     return math.atan(s) + s
Xa = [-3, -1, 1, 3]
Xb = [-3, 0, 1, 3]
Xo = -0.5
Ya = [f(Xa[m]) for m in range (4)]
Yb = [f(Xb[m]) for m in range (4)]
L = 0
P = Yb[0]

Y1 = [[Yb[0]],
      [Yb[1]],
      [Yb[2]],
      [Yb[3]]]

for j in range (4):
     p = 1
     for l in range (4):
          if l != j:
               p *= sp.expand((x - Xa[l]) / (Xa[j] - Xa[l]))
     L += sp.expand(Ya[j] * p)

print ('Многочлен Лагранжа:')
print (L)
print ()

for k in range(1, 4):
    for i in range(4 - k):
        val = (Y1[i+1][k-1] - Y1[i][k-1]) / (Xb[i+k] - Xb[i])
        Y1[i].append(val)
    pr = 1
    for o in range (k):
        pr *= sp.expand(x - Xb[o])
    P += sp.expand(Y1[0][k] * pr)

print ('Многочлен Ньютона:')
print (P)
print ()

L = sp.lambdify([x], L)
P = sp.lambdify([x], P)

print ('Отклонение в точке X* = -0.5 для многочлена:')
print ('Лагранжа', f(Xo) - L(Xo))
print ('Ньютона', f(Xo) - P(Xo))
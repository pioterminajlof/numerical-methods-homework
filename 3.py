"""Исходная система"""
A = [[24.0, 9.0, -1.0, -5.0],
    [-1.0, -14.0, 1.0, 9.0],
    [-7, 5.0, -21.0, 0.0],
    [1.0, 4.0, 8.0, -22.0]]

b = [-24.0,
     40.0,
     -84.0,
     -56.0]

alpha = [[0.0, 0.0, 0.0, 0.0],
         [0.0, 0.0, 0.0, 0.0],
         [0.0, 0.0, 0.0, 0.0],
         [0.0, 0.0, 0.0, 0.0],]
for i in range (4):
    for j in range (4):
        if i!=j:
            alpha[i][j]=-1*(A[i][j]/A[i][i])
        else:
            alpha[i][j]=0

beta = [0.0,
        0.0,
        0.0,
        0.0]

for k in range (4):
    beta[k] = b[k]/A[k][k]

"""Метод простых итераций"""

summ_str = [0.0, 0.0, 0.0, 0.0]
for d in range (4):
    for e in range (4):
        summ_str[d] += abs(alpha[d][e])
norm_alpha = max (summ_str)

x=[beta[:]]
c= 0
eps=1000000.0

while eps>=0.01:
    c += 1
    x += [[0.0, 0.0, 0.0, 0.0]]
    for p in range (4):
        x[c][p] = beta[p]
        for q in range (4):
            x[c][p] += x[c-1][q]*alpha[p][q]

    m = [0.0, 0.0, 0.0, 0.0]
    for l in range (4):
        m[l] = x[c][l] - x[c-1][l]
    norm_1 = max(abs(m[l]) for l in range(4))

    eps = norm_alpha / (1 - norm_alpha) * norm_1

print("\nРешение методом простых итераций:")
print("Вектор решений x =", x[c])
print("(",c, "итераций, eps < 0,01).")

"""Метод Зейделя"""
n = 4
xz = [beta[:]]
c = 0
eps = 1.0

while eps >= 0.01:
    c += 1
    xz.append([0.0] * n)

    for p in range(n):
        s = beta[p]
        for q in range(n):
            if q < p:
                s += alpha[p][q] * xz[c][q]
            else:
                s += alpha[p][q] * xz[c-1][q]
        xz[c][p] = s
    m = [abs(xz[c][l] - xz[c-1][l]) for l in range(n)]
    norm_1 = max(m)

    eps = norm_alpha / (1 - norm_alpha) * norm_1

print("\nРешение методом Зейделя:")
print(f"x = {xz[-1]}")
print(f"Число итераций: {c}")

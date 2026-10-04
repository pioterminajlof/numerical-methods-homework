import math

#Исходная матрица
A = [[-4.0, 1.0, 7.0],
     [1.0, 8.0, -5.0],
     [7.0, -5.0, 1.0]]

#Функция перемножения матриц
def mxm(a, b):
     r = [[0.0, 0.0, 0.0],
          [0.0, 0.0, 0.0],
          [0.0, 0.0, 0.0]]
     for k in range(3):
          for l in range(3):
               for m in range(3):
                    r[k][l] += a[k][m] * b[m][l]
     return r

t = 1
cou = 0
H = [[1.0, 0.0, 0.0],
     [0.0, 1.0, 0.0],
     [0.0, 0.0, 1.0]]

#Решение
while t > 0.01:
     cou += 1
     am = 0.0
     c = [0, 1]
     for i in range(3):
          for j in range(3):
               if i != j and abs(A[i][j]) > am:
                    am = abs(A[i][j])
                    c = [i, j]

     i, j = c
     fi = 0.5 * math.atan2(2*A[i][j], A[i][i] - A[j][j])
     sf = math.sin(fi)
     cf = math.cos(fi)

     U = [[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]]
     U[i][i] =  cf
     U[j][j] =  cf
     U[i][j] = -sf
     U[j][i] =  sf

     Ut = [[U[q][p] for q in range(3)] for p in range(3)]

     A = mxm(mxm(Ut, A), U)

     H = mxm(H,U)
     t = math.sqrt(sum(A[p][q] ** 2 for p in range(3) for q in range(3) if p != q))

#Вывод
print ("Собственные значения (",cou, "итераций, eps = 0,01 ):")
print ("lambda 1 =", A[0][0])
print ("lambda 2 =", A[1][1])
print ("lambda 3 =", A[2][2])
print ()
print ("Матрица собственных векторов: H =")
print (H[0])
print (H[1])
print (H[2])

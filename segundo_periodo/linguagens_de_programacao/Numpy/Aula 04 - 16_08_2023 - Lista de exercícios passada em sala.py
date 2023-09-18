import numpy as np
import numpy.random as npr 
from numpy.linalg import det, inv

############################ EXERCÍCIO 01 ############################

A1D_1 = np.arange(1, 17, 1).reshape(16, 1)
A1D_2 = np.arange(17, 33, 1).reshape(16, 1)

A1D_3 = A1D_1 + A1D_2

############################ EXERCÍCIO 02 ############################

A2D_4 = A1D_3.reshape(4, 4).astype("float32")

A2D_5 = A2D_4[::-1]

############################ EXERCÍCIO 03 ############################

A1D_6 = np.arange(0, 16, 1).reshape(1, 16)

A2D_7 = np.matmul(A1D_3, A1D_6)
A2D_8 = np.matmul(A1D_6, A1D_3)

############################ EXERCÍCIO 04 ############################

A1D_9 = npr.randint(10, size=10)
A1D_10 = npr.randint(10, size=10)

numeros_em_comum, A1D_9_ind, A1D_10_ind = np.intersect1d(A1D_9, A1D_10,return_indices=True)

numeros_exclusivos = A1D_9[np.isin(A1D_9, A1D_10, invert=True)]

############################ EXERCÍCIO 05 ############################

A2D_5_1 = np.arange(1, 10, 1).reshape(3, 3)
A2D_5_2 = np.arange(1, 10, 1).reshape(3, 3)

A2D_5_3 = np.hstack([A2D_5_1, A2D_5_2])

desvio_padrao = np.std(A2D_5_3)
variancia = np.var(A2D_5_3)

A2D_5_3[A2D_5_3%2==1] = -1
A2D_5_3[A2D_5_3%2==0] = 1

############################ EXERCÍCIO 06 ############################

A1D_6_1 = np.array([1, 2, 3])
A1D_6_2 = np.array([6, 7, 8])

A1D_6_3 = np.cross(A1D_6_1, A1D_6_2)

############################ EXERCÍCIO 07 ############################
A2D_7_1 = np.array([10, 25, 6, 14, 39, 78, 23, 22, 15]).reshape(3, 3)
A2D_7_2 = np.identity(3)

determinante = det(A2D_7_1)
matriz_inversa = inv(A2D_7_1)

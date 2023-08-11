import numpy as np 
import numpy.random as npr

A1 = np.array([0]*42)
print(A1)
print()

A2 = np.array([1]*42)
print(A2)
print()

A3 = np.array([0]*25).reshape(5, 5)
np.fill_diagonal(A3, 1)
print(A3)
print()

A4 = np.arange(7, 43)
print(A4)
print()

A5 = np.arange(8, 43, 2)
print(A5)
print()

A6 = npr.random_sample()
print(A6)
print()

A7 = 10*npr.randn(10, 1) + 20
print(A7)
print()

A8 = np.array([42]*10)
print(A8)
print()

A9 = np.arange(1, 10).reshape(3, 3)
print(A9)
print()

#SOLUÇÃO
A1 = np.zeros(42)
A2 = np.ones(42)
A3 = np.eye(5)
A4 = np.arange(7, 43)
A5 = np.arange(8, 43, 2)
A6 = npr.rand(1)
A7 = npr.randn(10) #atenção
A8 = np.ones(10) * 42
A9 = np.arange(1, 10).reshape(3, 3)
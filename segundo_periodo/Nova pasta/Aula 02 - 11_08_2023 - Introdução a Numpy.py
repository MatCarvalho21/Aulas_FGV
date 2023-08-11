import	numpy as np
import numpy.random as npr

#OPERAÇÕES EM NDARRAYS
salto_de_linhas = lambda: print("#"*80, end="\n\n")

'''
salto_de_linhas()
a1D_1 = np.arange(10) # -> vai criar arrays, nesse caso um vetor, em uma sequência (funciona como o range - star, stop, step)
print(a1D_1, end="\n\n")

salto_de_linhas()
a1D_1 = a1D_1.reshape(5, 2) # -> o reshape é um método do objeto nparray, nesse caso transforma um array [1, 10] em uma [5, 2], note que temos o mesmo número de elementos
print(a1D_1, end="\n\n")

salto_de_linhas()
a1D_1 = a1D_1.transpose() # -> vai inverter o número de linhas e colunas [5, 2] em [2, 5]
print(a1D_1)
'''

'''
salto_de_linhas()
a1D_2 = np.arange(16)
print(a1D_2, end="\n\n")

salto_de_linhas()
a1D_2 = a1D_2.reshape(4, 4)
print(a1D_2, end="\n\n")

salto_de_linhas()
a1D_4 = np.arange(start = 17, stop=33, step=1)
a1D_4 = a1D_4.reshape(4, 4)
print(a1D_4, end="\n\n")

#JUNTANDO VERTICALMENTE
salto_de_linhas()
a1D_3 = np.vstack((a1D_2, a1D_2)) # -> vai empilhar verticalmente
print(a1D_3, end="\n\n")

#JUNTANDO HORIZONTAMENTE
salto_de_linhas()
a1D_3 = np.hstack((a1D_2, a1D_4)) # -> vai empilhar verticalmente
print(a1D_3, end="\n\n")

salto_de_linhas()
print(f"Dados sobre a1D_3: \n- Dimensão: {a1D_3.ndim} \n- Forma: {a1D_3.shape}")
'''

'''
#SHALLOW COPY
a1D_5 = np.arange(10)
print(a1D_5, end="\n\n")

a1D_5_copy = a1D_5 # -> Fazer isso, significa dar um novo nome. Criar uma nova referência para o mesmo objeto. Isso não cria uma variável nova. Elas vão ter o mesmo endereço de memória.
print(a1D_5_copy, end="\n\n")

# -> Não podemos fazer uma cópia superficial, temos que fazer uma cópia de verdade (deep copy)
# -> tudo que eu fizer em uma variável, vai alterar a outra
a1D_5_copy[0] = 45
print(a1D_5, end="\n\n")
print(a1D_5_copy, end="\n\n")

print(id(a1D_5))
print(id(a1D_5_copy))
'''

'''
#DEEP COPY
a1D_5 = np.arange(10)
print(a1D_5, end="\n\n")

a1D_5_copy = a1D_5.copy() # -> esse é o método que devemos usar para fazer uma deep copy
print(a1D_5_copy, end="\n\n")

a1D_5_copy[0] = 45
print(a1D_5, end="\n\n")
print(a1D_5_copy, end="\n\n")

print(id(a1D_5))
print(id(a1D_5_copy))
'''

#RETORNO DE FUNÇÕES (DEEP COPY OU SHALLOW COPY)
A1 = np.arange(50)
A2 = A1.reshape(10, 5)

A2[:, 0] = 50

print(id(A1[0]))
print(id(A2[0]))
print()

print(id(A1))
print(id(A2))
print()

print(A1)
print()
print(A2)



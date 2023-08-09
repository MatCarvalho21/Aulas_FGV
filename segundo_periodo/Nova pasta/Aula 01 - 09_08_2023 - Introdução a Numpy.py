# -> ndarray vai simular uma lista em python, mas é bem mais rápido (um vetor/matriz de n dimensões) <- 
import numpy as np

''' COMANDOS DESNECESSÁRIOS

print(np.__version__) -> vai imprimir a versão da biblioteca

lista_teste = [1, 2, 3, 4, 5, 6, 7, 8, 0, 0, 0, 0] -> na hora de printar, a difereça está que os elementos da lista/tupla ficam separados por vírgula
print(lista_teste) -> o ponto é que arrays não, são como se fossem matrizes (tabelas de elementos)

-> PARA ACESSAR OS ELEMENTS, É DA MESMA MANEIRA QUE COM LISTAS (OS ÍNDICES COMEÇANDO EM 0)
print(a1D[3])

-> QUANDO TEMOS MATRIZES DE MÚLTIPLAS DIMENSÕES, PARA ACESSAR UMA LINHA BASTA UM COLCHETE, MAS PARA ACESSAR UM ELEMNTO SÃO NECESSÁRIOS DOIS COLCHETES
-> É NECESSÁRIO PENSAR COMO SE FOSSEM COORDENADAS (MSA DA MESMA FORMA OS ÍNDICES COMEÇAM NO 0)
a2D_1 = np.array(([1, 2, 3, 4], [5, 6, 7, 8]))
print(a2D_1[0][2])

-> SLICES 
print(a1D[1:7:2]) -> start:stop(exclusivo):step
print()
print(a2D_1[::-1, ::-1]) -> vai inverter a matriz/array (posso intercalar os slices por vírgula, denpendendo do número de dimensões)

'''

#PRODUZINDO ARRAYS (A PARTIR DE LISTAS, MAS PODE SER OUTRO TIPO DE ESTRUTURA)
a1D_1 = np.array([1, 2, 3, 4])
a1D_2 = np.array([5, 6, 7, 8])

#CONCATENANDO OS DOIS ARRAYS (O MÉTODO ESPERA RECEBER UMA TUPLA DE ARRAYS) -> Dentro da tupla, é possível inserir não só arrays, mas outras estruturas.
a1D = np.concatenate((a1D_1, a1D_2, [0, 0, 0, 0]))

a2D_1 = np.array(([1, 2, 3, 4], [5, 6, 7, 8]))

a3D_1 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])

print(f"Dados sobre um array (a1D): \n- Dimensões: {a1D.ndim} \n- Tamanho (Número de Elementos): {a1D.size} \n- Tipo: {a1D.dtype} \n- Formato: {a1D.shape} \n- Tamanho do Elemento: {a1D.itemsize} bytes\n")
print(f"Dados sobre um array (a2D_1): \n- Dimensões: {a2D_1.ndim} \n- Tamanho (Número de Elementos): {a2D_1.size} \n- Tipo: {a2D_1.dtype} \n- Formato: {a2D_1.shape} \n- Tamanho do Elemento: {a2D_1.itemsize} bytes\n")
print(f"Dados sobre um array (a3D_1): \n- Dimensões: {a3D_1.ndim} \n- Tamanho (Número de Elementos): {a3D_1.size} \n- Tipo: {a3D_1.dtype} \n- Formato: {a3D_1.shape} \n- Tamanho do Elemento: {a3D_1.itemsize} bytes\n")

#ARRAYS DE 3 DIMENSÕES
a3Dim = np.array([ [ [1, 2], [3, 4] ], [ [5, 6], [7, 8] ] ], dtype=np.float32)   
print(f"Dados sobre um array (a3Dim): \n- Dimensões: {a3Dim.ndim} \n- Tamanho (Número de Elementos): {a3Dim.size} \n- Tipo: {a3Dim.dtype} \n- Formato: {a3Dim.shape} \n- Tamanho do Elemento: {a3Dim.itemsize} bytes\n")
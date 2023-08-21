import numpy as np 
import numpy.random as npr 
import math

'''
BROADCASTING
não precisamos fazer loops para resolver problemas com numpy, isso gera eficiência

É RECOMENDADO QUE AO INVÉS DE USAR LISTAS PARA FAZER OPERAÇÕES, USAR ARRAYS NUMPY

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

a1d_a = np.array([1, 2, 3, 4])
a1d_b = np.array([0, 1, 2, 3])


# -> OPERAÇÕES BÁSICAS <- # TODAS AS OPERAÇÕES SERÃO FEITAS ELEMENTO A ELEMENTO

print(a1d_a*a1d_b) # vai multiplicar elemento por elemento ("combinação linear dos dois vetores TEM QUE SER MESMA DIMENSÃO")
print(a1d_a*10) # vai multiplicar elemento a elemento pelo escalar em questão que é 10
print(a1d_a + a1d_b)
print(a1d_a - a1d_b)
# print(a1d_a / a1d_b) # vai dar erro pois b tem um elemento nulo
print(a1d_b / a1d_a)
print(a1d_a + 10)
print(a1d_a**2)
print(a1d_b/0) #pode dar infinito ou nan (0/0)

# POSSO FORMAR ARRAYS COM STRINGS, MAS NUNCA MISTURANDO OS TIPOS
a1d_3 = np.array(["a", "b", "c", "d"])


# PRODUTO MATRICIAL

# cria uma matriz com true/false fazendo a operação lógica para cada elemento
ndarray = np.array([1, 2, 3, 4, 5, 6])

indices = ndarray > 3
print(indices)
print(ndarray[indices]) # vai pegar os elemntos que retornam true. No caso os maiores que 3


indices = ndarray%2 == 0 # verificação de pares e ímpares
print(indices)
print(ndarray[indices]) #vai retornar todos os elementos da matriz que são pares

# TODOS OS PARES MENORES QUE 1000
ndarray = np.arange(0, 1000, 1)
print(ndarray[ndarray%2 == 0].reshape(25, 20))

ndarray = np.arange(9).reshape(3,3)
indices = np.array(([True, False, True], [False, True, False], [True, False, True])).reshape(3, 3)
print(ndarray[indices]) # vai printar apenas os elementos que batem true com a segunda matriz


#MEDIDAS ESTATÍSTICAS
#BREAKING BAD
notas = np.array([87, 72, 95, 93, 70, 100])

#AVERAGE
print("Average: ", round(np.average(notas), 2))

#MEDIAN
print("Median: ", round(np.median(notas), 2))

#MEDIAN
print("Standard Deviation: ", round(np.std(notas), 2))

#MINIMUN E MAXIMUN
print("Maximun e Minimun: ", np.amax(notas), "e", np.amin(notas))

#PERCENTILE
print("Percentile [95]: ", round(np.percentile(notas, 95), 2))

#PEAK TO PEAK (distância entre o mínimo e o máximo)
print("Peak to Peak: ", round(np.ptp(notas), 2))
'''

#ELABORAR UM PROGRAMA QUE TRATA UMA MATRIZ 2 POR N COMPOSTA POR:
    # UMA COLEÇÃO DE VALORES ESTIMADOS
    # UMA COLEÇÃO DE VALORES OBSERVADOS
    
#elaborem 4 funções 
'''
1 - Exibir o Erro médio absoluto
2 - Exibir o Erro médio quadrático
3 - Exibir os Dados gerais da coleção (estatístico)
4 - Exibiro histograma da coleção
'''

a1d_1 = np.array(([1, 2, 3, 4], [2, 3, 4, 5]))

def erro_medio(array1):
    
    nparray_erro = array1[0] - array1[1]
    erro_medio = np.sum(nparray_erro)/len(nparray_erro)
    
    print(f"O erro médio absoluto é: {round(erro_medio, 2)}")
    print()
    
def erro_qusadratico(array1):
    
    nparray_erro = (array1[0] - array1[1])**2
    erro_medio = np.sum(nparray_erro)/len(nparray_erro)
    
    print(f"O erro médio quadrático é: {round(erro_medio, 2)}")
    print()
    
    
def dados_estatisticos (array):
    print(f"DADOS ESTATÍSTICOS MATRIZ ESTIMADA: \n- Média: {np.average(array[0])} \n- Mediana (Percentil 50): {np.median(array[0])} \n- Desvio Padrão: {np.std(array[0])} \n- Máximo: {np.amax(array[0])} \n- Mínimo: {np.amin(array[0])} \n- Diferença de Picos: {np.ptp(array[0])} \n- Percentil [5]: {np.percentile(array[0], 5)} \n- Percentil [25]: {np.percentile(array[0], 25)} \n- Percentil [75]: {np.percentile(array[0], 75)} \n- Percentil [95]: {np.percentile(array[0], 95)}")
    print(f"\nDADOS ESTATÍSTICOS MATRIZ OBSERVADA: \n- Média: {np.average(array[1])} \n- Mediana (Percentil 50): {np.median(array[1])} \n- Desvio Padrão: {np.std(array[1])} \n- Máximo: {np.amax(array[1])} \n- Mínimo: {np.amin(array[1])} \n- Diferença de Picos: {np.ptp(array[1])} \n- Percentil [5]: {np.percentile(array[1], 5)} \n- Percentil [25]: {np.percentile(array[1], 25)} \n- Percentil [75]: {np.percentile(array[1], 75)} \n- Percentil [95]: {np.percentile(array[1], 95)}")

erro_medio(a1d_1)
erro_qusadratico(a1d_1)
dados_estatisticos(a1d_1)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
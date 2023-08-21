import numpy as np 
import numpy.random as npr 

"""
encontrar os valores comuns entre dois vetores
em um vetor com 100 elementos (0-99) inverta os valores de 42 até 66
encontre o elemento de um vetor mais próximo de um determinado valor
"""

####################################################################

def valores_em_comum(array1, array2):
    numeros_em_comum = np.intersect1d(array1, array2)
    return numeros_em_comum


def valor_mais_proximo(valor, array):
    indice = np.abs(array - valor).argmin()
    return array[indice]

def inverter_intervalo(array):
    array[42:67] = array[42:67]*(-1)
    return array

####################################################################

# -> CORREÇÃO 

def inverter_intervalos_corrigido(array, valor_inicial, valor_final):
    array[(array >= valor_inicial) & (array <= valor_final)] *= -1
    return array


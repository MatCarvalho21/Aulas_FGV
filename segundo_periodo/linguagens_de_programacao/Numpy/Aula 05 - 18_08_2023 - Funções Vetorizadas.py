import numpy as np 
import time

# VETORIZAÇÃO DE FUNÇÕES #
"""
no numpy as operações são feitas elemento a elemento, logo não precisamos 
criar loops ou algo do tipo pora operar sobre a matriz, isso geralmente acontece com operações algébricas.
podemos fazer isso também com funções, as chamadas funções vetorizadas
"""

'''
# LOOP DE FOR 

inicio_tempo_loop = time.time()

vetor_loop = list(range(1, 1000001)) # um range é uma sequência, não uma lista, temos um tipo próprio

for cada_numero in range(len(vetor_loop)):
    vetor_loop[cada_numero] = vetor_loop[cada_numero]**2
    
fim_tempo_loop = time.time()

print("Tempo de loop: ", fim_tempo_loop - inicio_tempo_loop) # no compilador online deu 7.1 microsegundos 



# NUMPY

inicio_tempo_numpy = time.time()

vetor_numpy = np.array(range(1, 1000001)).reshape(1000, 1000)
vetor_numpy = vetor_numpy ** 2

fim_tempo_numpy = time.time()

print("Tempo de Numpy: ", fim_tempo_numpy - inicio_tempo_numpy) 
'''

'''
def calcular_quadrado(numero):
    return numero**2

def impar_ou_par(numero):
    
    try:
        numero = int(numero)
    except ValueError:
        return None
    
    if numero%2 == 0:
        return True
    else:
        return False
    
vetor = np.array(range(1, 101)).reshape(20, 5)

# ASSIM QUE VAMOS VETORIZAR NOSSAS FUNÇÕES, ELAS NÃO VÃO TER O MESMO TIPO. NUMPY VECTORIZE É O NOME DO TIPO DA FUNÇÃO VETORIZADA 
funcao_vetorizada = np.vectorize(impar_ou_par)

print(funcao_vetorizada(vetor))
'''


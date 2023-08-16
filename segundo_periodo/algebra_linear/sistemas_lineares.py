import numpy as np  

def sistemas_lineares(matriz):
    """
    a função recebe uma matriz extendida, ou seja, n por n + 1
    explicando melhor seria a concatenação da matriz A com a B
    e retorna o vetor solução do sistema linear em questão
    """

    if matriz.shape[0] == matriz.shape[1] + 1:
        
    else:
        print("Sua matriz não se encaixa nas descrições!")
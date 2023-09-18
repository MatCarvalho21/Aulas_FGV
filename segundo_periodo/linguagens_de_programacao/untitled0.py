import numpy as np
import numpy.random as npr
import pandas as pd

npr.seed(42)
serie_numeros = pd.Series(npr.randint(1, 10, 42))


serie_frequencias = serie_numeros.value_counts().tail(8).index.values.tolist()

for cada_valor in serie_frequencias:
    serie_numeros = serie_numeros.replace(cada_valor, "DESCONSIDERADO")

#USAR O MÉTODO UNIQUE PARA RESOLVER O MESMO PROBLEMA

serie_1 = pd.Series(npr.randint(0, 11, 10))
serie_2 = pd.Series(npr.randint(0, 11, 10))

def verificador_de_exclusividade(serie_1, serie_2):
    serie_uniao = pd.Series(np.union1d(serie_1, serie_2))
    serie_intersecao = pd.Series(np.intersect1d(serie_1, serie_2))
    
    passo1 = serie_uniao.isin(serie_intersecao)
    passo2 = ~passo1
    print(serie_1)
    print(serie_2)
    print(serie_uniao[passo2])
    
    
verificador_de_exclusividade(serie_1, serie_2)

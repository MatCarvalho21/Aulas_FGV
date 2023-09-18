import pandas as pd 
import numpy as np 

""" SÉRIES 
- UFUNCs
"""
"""
#Estruturas de Dados Iniciais 

lista_1 = [1, 2, 3, 4, 5]
lista_2 = ["I", "II", "III", "IV", "V"]


dict_1 = {"I":1, "II":2, "III":3, "IV":4, "V":5}

ndarray_1 = np.array(lista_1)

print("#"*100)

print(lista_1)
print(lista_2)
print(dict_1)
print(ndarray_1)

print("#"*100)


as séries possuem os mesmos métodos de um array unidimensional

no caso das séries pandas, temos uma indexação explícita, podemos 
mudar os índices e sair do padrão numpy que são os números ordenados

sempre que printamos uma série pandas teremos os índices na esquerda, os 
valores na direita e os tipos embaixo

quando passamos um dicionário para o método séries, ele pega os índices 
do dicionário e transforma no índice da série automaticamente 



ser_1 = pd.Series(lista_1)
print(ser_1)
ser_2 = pd.Series(lista_2)
print(ser_2)
ser_3 = pd.Series(dict_1)
print(ser_3)
ser_4 = pd.Series(ndarray_1)
print(ser_4)

print(ser_1.shape, ser_1.values, ser_1.index)

ser_5 = pd.Series(data=lista_1, index=lista_2)
print(ser_5)

print(ser_5.tolist())
print(ser_5.to_list())

print("#"*100, sep="\n")

#Acessando os Elementos
print("\nAcessando os Elemnentos: \n", ser_1[:3], sep='\n')
print("\nAcessando os Elemnentos: \n", ser_1[-3:], sep='\n')
print("\nAcessando os Elemnentos: \n", ser_1.head(3), sep='\n')
print("\nAcessando os Elemnentos: \n", ser_1.tail(3), sep='\n')
print("\nAcessando os Elemnentos: \n", ser_1[4], sep='\n')
print("\nIndice Máx: \n", ser_1.idxmax(), sep='\n')
print("\nIndice Mín: \n", ser_1.idxmin(), sep='\n')

print("\nLOC: \n", ser_1.loc[1:4:2], sep='\n') #busca no rótulo do índice, o nome que eu dei 
print("\nILOC: \n", ser_1.iloc[0:3], sep='\n') #obriga a buscar no indice do indice 

"""

# podemos usar underlines para separar números grandes, mas apenas em python
dicionario_2 = {"I":10, "II":42, "III":7, "V":1_000_000}
dicionario_3 = {"I":1, "II":12, "III":13, "IV":0}

# temos que lembra do rótulo do indice e do indice em si
ser_2 = pd.Series(dicionario_2)
ser_3 = pd.Series(dicionario_3)

print(ser_2)
print(ser_3)




















#lista = [1,2,3] #Lista de Inteiros 
#tupla = (1,2,3)
#print(lista) #A formatação é típica e aponta para uma lista 
#print(tupla)
#print(type(lista), type(tupla))


#ista1 = [1, 1.1, 'matheus', [1, 2, 3, 4, 5], ["EMAp"], ("texto", 1)] #Lista alinhada, quando temos uma lista dentro de outra
"""
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
"""
#lista = ["E", "M", "A", "p", [2,0,0,3]]
#print(lista[4][0])
"""
lista = ["E", "M", "A", "p"]
print(lista[0:5]) #Começa no 0 mas para no 4, ele não chega ao 5
print(lista[1:4]) #Vai pegar do 1 ao 3
print(lista[:4])
print(lista[1:]) 
print(lista[-3:])
"""
"""
lista = ["E", "M", "A", "p"]
del lista[0] #vai apagar definitivamente um objeto, matamos o E pra sempre
# vale lembrar que quando apagamos os elementos, os índices mudam, o novo elemento 0 passa a ser M
# posso deletar com slices também, deletando pedaços da lista  
del lista #Não vou conseguir printar mais, essa lista vai ser completamente apagada da memória 
# print(lista)
"""
"""
minha_lista = ["M","A","T","H","E","U","S","A","A"]
# minha_lista.remove("A") #Vai retirar apenas o primeiro elemento correspondente 
# minha_lista.remove("A")
# minha_lista.clear() #Vai limpar uma lista
print(minha_lista)
"""
impares = [2,4,6,8]
impares[0] = 1
print(impares)

impares[1:4] = [3,5,7]
print(impares)

impares.append(9)
print(impares)

impares.extend([11, 13, 15]) #Vai receber um iteravel e adicionar item a item
print(impares)

impares_e = [17, 19, 21]
print(impares + impares_e)

print(1 in impares)
print(2 in impares)
print(2 not in impares)

for i in impares:
    print(i, "é um número ímpar!")
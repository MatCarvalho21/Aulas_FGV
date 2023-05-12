# slices vai pegar pedaçoes de uma lista
lista = [0, 1, 2, 3, 4, 5]
# range(start, stop, step)
# print(lista[0:5:1]) # vai pegar o primeiro termo, até o 5, pulando de 1 em 1, sem pegar o 5.
# a função range também faz a mesma coisa, não pega o segundo elemento.
# operador in vai ser um operador de pertencimento, vendo se o elemento está dentro de um iterável. Posso usar esse in como uma condição, pois ele vai retornar true ou false. 

# os métodos são dependentes de outras classes, por exemplo existem métodos específicos de lista. 
# existem os métodos que retornam algo novo e os que alteram a classe dependente. O método .sort() vai alterar a lista que entrar nele, a partir dali a lista passa a estar ordenada. a função sorted() não altera a lista original, ela me retorna uma lista nova e ordenada. 
# in-place vai modificar o elemento original.

#quando eu faço lista1 == lista2 eu não crio uma lista nova. eu apenas crio um outro nome pra lista, logo se eu modificar uma, eu modifico a outra. Shallow copy 
#para copiuar lista1 = lista.copy() vai me retornar um novo objeto mas igual ao original que foi copiado. O método copy resolve isso. 

#pesquiar list comprehention w3schools 

# a = input('Digite aqui um valor qualquer: ') #aguarda que o usuário insira alguma coisa e executa o programa. ele também imprime uma string antes disso. para indicar para o usuário oq digitar 
# print(f'Você digitou {a}!') #vale lembrar que o input, por padrão retorna uma string, se você quiser um inteiro é necessário converter int(input())

# se eu colocar um float dentro de int() ele vai truncar e retirar as casas decimais 

#control ponto e virgula é o comando para comentar todas as linhas 

lista1=[1, 2, 3, 4, 5]
lista2=[6, 7, 8, 9, 10]

# JEITO RUIM

# for i in lista:
#     print(i**2)

# for i in lista2:
#     print(i**2)

# JEITO BOM

def quadrado(lista): #nesse caso recebe 2 argumentos 
    for numero in lista:
        print(numero**2)
    return None

quadrado(lista1)
quadrado(lista2)

def imprimeoi(): #nesse caso não recebe argumento 
    print('oi')

imprimeoi()

# FUNÇÕES COM VÁRIOS ARGUMENTOS 
import math 

def media_tres_valores(n1, n2, n3):
    media = (n1+n2+n3)/3
    print(media)
    return media

media = media_tres_valores(25, 30, 20) #to atribuindo o retorno da funcao a uma variável

# quando uma função tem mais de um retorno e esse retorno é atribuido para um unica variável, essa variável vai ser uma tupla com aqueles valores 
# tuplas são definidas como uma lista imutável, porém é mostrada com parênteses 
# os argumentos default da função são dados por uma igualdade na hora da definição
def potencia(base, exponte = 2): #expoente 2 é um argumento que por padrão é 2, mas eu posso alterar esse valor se quiser 
    print(base**exponte)
    return base**exponte

potencia(10) #não inseri o argumento, pq ele é opicional 
potencia(10, 5) #inseri pq eu queria outro retorno 


#### monitoria 02 ####

# Vamos usar if/elif/else quando temos escolhas para serem feitas. O else é descartável, mas é recomendado se você não conseguir mapear todas a possibilidades com o if, elif, and, or e not. 

aluno = "Matheus"
idade = 18
# Uso simples do if para determinar a permissão para beber bebida alcoólica 

if idade < 18:
    print(f"Calma aí, {aluno}! Espere mais um pouco. ")
else:
    print(f"Você pode encher a cara, {aluno}!")

# Operadores lógicos "and" e "or". Eles vão ter tabelas verdades diferentes. Para "and" ser verdadeiro, as duas tem que ser verdade. No caso do "or", basta que uma seja verdadeira para que ele execute o código. 

if idade >= 18 and idade >= 60:
    print("Você pode se embreagar e se aposenta!")
elif idade>18:
    print("Você pode apenas se embreagar...")
else:
    print("Você não pode nem beber, nem se aposentar. Vai estudar, pirralho!!")

# Podemos comparar strings também
aluno1 = "Matheus"
aluno2 = "Carlos"

if aluno1 == aluno2:
    print("Os alunos tem o mesmo nome.")
else:
    print("Eles têm nomes diferentes.")

# O if pode ser usado para detectar se existe um conteúdo na string. Aluno1 é verdadeiro pois é uma string que possui um conteúdo que eu atribui mais acima.

if aluno1:
    print("SIM")
else:
    print("NÃO")

# 0, None, "", []... São termos naturalmente falsos. Não tem como mudar.
# Laços: for, while, until. Vamos usar para criar laços.

lista = ["a", "b", "c", "d", "e"] #uma lista é um exemplo de algo iterável, que é algo que eu possa percorrer. O "for", vai exigir um elemento iterável como as listas, tuplas, dicionários...
for letra in lista:
    print(letra) # vai printar todas as vezes que letra estiver em lista
i = 0
while i <= 10: #uma condição que sempre vai ser verdadeira (1 == 1), logo é um loop infinito. Temos que usar uma variável de controle. 
    print("Matheus")
    i += 1 #vai alterar a variável de controle e encerrar o loop quando a condição for atendida. Nesse caso ele vai imprimir "Matheus" 10 vezes. Toda vez que for executado, i vai aumentar 1.
    
#posso usar uma variável sentinela também

sentinela = True
x = 10
while sentinela == True:
    print("Opa")
    x = x - 1
    if x == 0:
        break #vai quebrar o loop, mesmo que ele seja infinito, quando atender uma condição.

# verificador de par 
m = 1
while True: #vai ser sempre true, logo um loop infinito.
    m += 1
    if (m % 2) != 0:
        continue #vai voltar pro início, com o m uma unidade maior.
    else:
        print(f"O {m} um número par")
    if m >=100: #vai ser a condição responsável por quebrar o loop. logo teremos os pares até 100.
        break #geralmente o limite são três laços ou ifs. 

#lista 

lista = [1, 2, 3, "a", "b", "c"] #para criar uma lista, eu dou um nome, abro colchetes e insiro os valores. não existem restrições quanto ao tipo de um elemento em uma lista. 
print(lista) #os elementos serão identificados por um índice (que começa em 0) que indica a sua posição na lista 
print(lista[2]) #3 é o terceiro elemento, mas é o elemento de índice 2. Pois a contagem começa no 0. 
lista2 = ["a", "b", "c"]
lista3 = [1, 2, 3]
lista4 = lista2 + lista3 #podemos concatenar listas, apenas emendar as suas listas, note que nesse caso a ordem importa 
print(lista2*2) #Vai operar a lista, no caso vai duplicar. Isso idepende dos tipos dos elementos, mesmo que eu tivesse um número, ele não seria multiplicado por 2. Apenas teríamos 2 listas. 
print(lista4)
lista3[1] = 10 #vai substituir o elemento de índice 1 pelo valor que eu atribui 
print(lista3)
lista3.append(100) #um método usado para inserir um valor dentro de uma lista, no caso adiciona no final da lista o valor 100
print(lista3)
lista3.append([10, 20, 30, 40, 50]) #posso inserir uma lista dentro de outra. O último elemento agora é uma lista, nada mais que uma matriz 
print(lista3)
print(lista3[4][2]) #tenho que usar dois colchetes consecutivos para acessar um elemento de uma lista dentro de uma lista. o primeiro indica a posição da lista, e o segundo a posição do elemento dentro dessa lista secundária

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #assim que criamos a matriz, listas dentro de listas
print(matriz)
for linha in matriz: #método usado para imprimir linha por linha. Imprime a primeira, pula. A segunda, pula. E tal. 
    print(linha)
# para imprimir sem os colchetes, tenho que criar dois for. Vai primeiro imprimir as linhas por linhas e depois elemento por elemento
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ") #toda vez que ele imprimir um elemento, ele imprime um espaço 
    print(" ") #quando ele termina de imprimir uma linha, ele imprime nada, apenas para poder pular uma linha 

print(matriz[2][1]) #para acessar elementos dentro de uma matriz 

retirado = lista2.pop() #vai tirar o último item da lista e retorna esse item. se eu tivesse um print, iria mostrar o elemento c que ele tirou. atribui esse elemento na variável
print(lista2)  #note que o elemento c realmente foi retirado da lista 
 # As funções são ferramentas independentes. Os métodos são coisas que um objeto consegue fazer. Por exemplo, as listas conseguem executar o ".append()" que adiciona um elemento no final dela. Um inteiro não consegue fazer o "append()".
lista2.append(retirado) #venho e adiciono novamente o item que eu havia retirado 
print(lista2)

# indices negativos se referem a partir do últuimo termo. Por exemplo o índice -1 se refere ao ultimo elemento de uma lista. (Se tras pra frente não começa do 0)

"""

if Condição: 
    Se a condição for verdadeira, faça isso.
elif Condição_2:
    Se a segunda condição for verdadeira, faça isso.
else:
    Se nenhuma condição for verdadeira, faça isso. 

"""

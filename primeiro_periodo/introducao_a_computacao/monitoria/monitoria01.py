print("Hello, world!") #A função print retorna no terminal o que foi passado para ela. 
x = "Hello, world!" #As variáveis são usadas para guardar dados. Nesse caso atribuimos uma string, graças as aspas, à variável x. (as variáveis não podem começar com valor númerico e nem ter espaços)
y = 2
print(x)
print(type(x)) #A função type vai retornar o tipo do "objeto" dentro dos parênteses. No caso foi uma "str", que é o nome dado para tipos que são interpretados como palavras. 
print(y.__dir__())

#### Operadores Aritméticos (o python vai respeitar a ordem das operações, privilegiando parênteses)
a = 2
b = 3
print(a + b) #soma
print(a - b) #diferença
print(a * b) #multiplicação
print(a / b) #divisão
print(a % b) #resto da divisão
print(a ** b) #potência
print(a//b) #parte inteira da divisão

a, b, c = 1, 1, 1
print(a, b, c, a+b, (a+b+c)*(a+b)) #as variáveis devem ter nomes do que elas significam, apenas letras não é suficiente, pode confundir. não devemos colocar letras maiúsculas também.

#Operadores de comparação vão retornar valores true e false. 
print(b < a)
a = a + 5
print(b < a)

primeiro_nome = "Matheus"
segundo_nome = "Carvalho"
print("O meu nome é: ", primeiro_nome, segundo_nome)
print(f"O meu nome é {primeiro_nome} {segundo_nome}.") #a string formatada permite colcoar variáveis dentro do texto, mas eu tenho que colocar o f no início e as chaves com as variáveis dentro
print("O meu nome é: ", primeiro_nome, segundo_nome, sep = "$") #sep vai configurar o seprador, que normalmente é espaço para separar os argumentos dentro do print. 
print("O meu nome é: ", primeiro_nome, segundo_nome)  #o end gearlmente é uma quebra de linha depois do print, podemos configurar e colocar o que eu quiser após o print


f_string = f"O meu nome é {primeiro_nome} {segundo_nome}."
print(type(f_string))

import math #importe a biblioteca math que possui funções especiais para usar em operações matematicas
import math as ma #posso atribuir apelidos para as minhas bibliotecas, o nome original para de funcionar 
print(ma.sqrt(4))
print(ma.pi)
from math import sqrt #usado para importar apenas uma função de uma biblioteca, nesse caso não será mais necessário usar o math antes do sqrt. 
from math import * #todas as funções de math passam a ser conhecidas pelo código e não é necessário usar o math antes das funções 

#comando para criar uma função que vai ficar dentro do código
def matheus(recebe): 
    x = recebe
    return x + 15
print(matheus(a))

#variáveis globais são dadas por valores maiúsculos e devem ser importadas de outros arquivos (que estão na mesma pasta)
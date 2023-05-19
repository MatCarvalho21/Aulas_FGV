# Definição de Funções (arg, *args, **kwargs)
# *args -> lista
# **kwargs -> dicionario 
"""
def media_args(*args): #Vai transformar todos os elementos recebidos em lista. Depois podemos operar nessa lista. 
    soma = sum(args)
    media = soma/len(args)
    return media

def media_kwargs(**kwargs): #Vai receber associações e transformar em dicionário.
    print(kwargs)

media_kwargs(a=5,c=4,d=5) #Vai transformar isso em dicionário atribuindo chaves e valores. 

def funcao_completa(a, b, *args, **kwargs): #Os dois primeiros argumentos vão ser a e b, os outros que tiverem soltos são args e os que tiverem valores atribuídos são kwargs.
    print(a, b, args, kwargs)

funcao_completa('abacaxi', 'bola', 1, 5, 8, 6, 5, 4, 7, 8, c=8, d=10, e=15)
"""
# A biblioteca pprint vai printar cada info em uma linha. 
#TAREFA
biblioteca = {}
def novo_livo(**kwargs):
    for key in kwargs.keys():
        kwargs[key] = str(kwargs[key]).title()
    return kwargs

matheus = novo_livo(autor="matheus", editora="novo rio")

def adicionar_livro(biblioteca, livro_criado, titulo):
    biblioteca[titulo] = livro_criado
    return biblioteca

print(adicionar_livro(biblioteca, matheus, "matheus"))
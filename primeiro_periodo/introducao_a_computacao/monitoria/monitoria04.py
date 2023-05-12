# Definição de Lista
lista = []
# Definição de Tupla
tupla = ()
# Definição de Set (Conjunto)
set = {}
# Definição de Dicionário
dicionario = {1:"Matheus", 2:"Lucas", 3:"João", True:"Carlos", (1,2,3):"Pedro"} # Vai receber uma chave, valor e um item (chave + valor). Podemos usar também a função dict().
## Acesso a item do dicionário 
print(dicionario[1]) #Vai printar o elemento do dicionário que está vinculado a essa chave.
dicionario[0] = "Matheusao" # Para adicionar novos pares a um dicionário é necessário inserir manualmente a chave nova e o novo item. Se a chave já existir, ele vai sobrescrever.
print(dicionario[0])
# Podemos usar o método update para inserir dados de um dicionário em um outro dicionário. 
dicionario.pop(1)
print(dicionario)

def divisores(n):
    lista = []
    for i in range(1, n+1, 1):
        if n//i == n/i:
            lista.append(i)
    print(lista)
    return lista

divisores(100)

def fatoracao(n):
    for i in range(1, n+1, 1):
        for t in range(1, i+1, 1):
            if i%t == 0:
                lista_divisores = []
                lista_divisores.append

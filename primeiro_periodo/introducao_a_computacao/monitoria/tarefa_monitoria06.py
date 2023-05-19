def f_media(lista):
    return sum(lista)/len(lista)

def f_mediana(lista): #A ideia está correta, mas matematicamente errada. 
    lista_valores = sorted(list(lista))
    if (len(lista_valores)/2) == (len(lista_valores)//2):
        teste = len(lista_valores)/2
        mediana = (lista_valores[int(teste)] + lista_valores[int(teste + 1)])/2
    else:
        mediana = lista_valores[int(len(lista_valores)/2)]
    return mediana

def f_moda(lista):
    moda = 0
    for valores in lista:
        if lista.count(valores) > moda:
            moda = lista.count(valores)
    return valores

def analise(*args):
    lista = list(args)
    media = f_media(lista)
    mediana = f_mediana(lista)
    moda = f_moda(lista)
    dicionario_estatistico = {"Média": media, "Mediana": mediana, "Moda": moda}
    return dicionario_estatistico

print(analise(1,1,2,5,1,4,8,5,5,1,4,5,5,8,7,5,2,13,5,45,4,5,5,8))
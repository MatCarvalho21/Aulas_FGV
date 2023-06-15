def cifra_reversa(mensagem):
    resultado = ""
    caracteres_restantes = len(mensagem) - 1
    
    while caracteres_restantes >= 0:
        resultado = resultado + mensagem[caracteres_restantes] #Vai montar uma string de tras pra frente
        caracteres_restantes -= 1
        
    return resultado

def cifra_de_cesar(mensagem, modo, chave):
    resultado = ""
    
    for cada_letra in mensagem:
        if cada_letra in dicionario:
            indice_caracter = dicionario.find(cada_letra)
            
            if modo == 'encriptar':
                indice_corrigido = indice_caracter + chave
                
            elif modo == "decriptar":
                indice_corrigido = indice_caracter - chave
            
            if indice_corrigido >= len(dicionario):
                indice_corrigido = indice_corrigido - len(dicionario)
                
            elif indice_corrigido < 0:
                indice_corrigido = indice_corrigido + len(dicionario)
            
                
            resultado = resultado + dicionario[indice_corrigido]
        else:
            resultado = resultado + cada_letra
        
    return resultado

dicionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,"

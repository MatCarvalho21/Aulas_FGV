def geo_linha(nome_arquivo):
    with open(nome_arquivo, "r") as f: 
        for i, l in enumerate(f.readlines()):
            if i >= 4:
                yield l.strip().strip('"').split('","') #Apenas métodos de string. Vaio transformar uma linha em uma lista de palavras.
#O yield vai transformar a função em um gerador. Um return iterável. 
#Um gerador retorna objetos um atrás do outro. Toda vez que o for rodar, ele vai retornar o yield. A própria função é iterável. Vamos acessar o gerador iterando sobre ele.         

def converte_linha(nome_arquivo): #Apenas vai formatar as palavras do arquivo. Se for número vai converter para número. 
    for linha in geo_linha(nome_arquivo):
        linha_convertida = []
        for elemento in linha:
            try:
                f = float(elemento)
                if int(f) == f:
                    linha_convertida.append(int(f))
                else:
                    linha_convertida.append(f)
            except ValueError:
                linha_convertida.append(elemento) 
        yield linha_convertida


if __name__ == "__main__":  #O main é o arquivo que iniciou o script. O arquivo onde o código for executado/gerado. O arquivo rodado é sempre __main__. Essa linha só roda se esse arquivo for executado diretamente, se importado essa linha não roda.
    nome_arquivo = "dados.csv"
    for l in converte_linha(nome_arquivo):
        print(l)
#Vai criar uma restrição. 

#Venv é uma forma de usar ferramentas de python sem precisar instalar no seu computador. 
#Vai instalar essa pasta venv na pasta do seus arquivos e ela vai gerenciar as suas bibliotecas, assim como no programa da froca python venv -m PATH. 


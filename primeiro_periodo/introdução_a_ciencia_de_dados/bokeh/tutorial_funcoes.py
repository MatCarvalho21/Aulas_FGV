# FUNÇÕES SIMPLES
def saudacoes():
    print("Eu adoro a EMAp!")
# FUNÇÕES COM UM ARGUMENTO
def saudacoes_argumentos(nome_usuario):
    print(f"Olá, {nome_usuario.title()}! Eu adoro a EMAp!") #Title vai colocar a primeira letra das palavras em maiúsculo. 
# FUNÇÕES COM MAIS DE UM ARGUMENTOS (NÃO USAR MAIS DE 10 ARGUMENTOS)
def saudacoes_argumentos_posicionais(nome_usuario, escola_usuario):
    print(f"Olá, {nome_usuario.title()}! Eu adoro a {escola_usuario.title()}!")

saudacoes()
saudacoes_argumentos("matheus")
saudacoes_argumentos("floquinho de neve")
saudacoes_argumentos_posicionais("matheus", "emap")

# FUNÇÕES COM ARGUMENTOS PADRÕES 
def saudacoes_default(nome_usuario = "Matheus", nome_escola = "EMAp"):
    print(f"Olá, {nome_usuario.title()}! Eu adoro a {nome_escola.title()}!")

saudacoes_default()
saudacoes_default('Lucas')
saudacoes_default(nome_escola='Leon Reanult')
        
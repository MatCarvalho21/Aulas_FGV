from monitoria07 import Aluno

# INSTÂNCIA 1
matheus = Aluno("Matheus Fillype Ferreira de Carvalho", "Ciência de Dados e Inteligência Artificial", 42) # assim contruimos uma instância, vamos aplicar o sinal de igual a variável e inserir os parâmetros necessários.
print(f"O nome do aluno é {matheus.__nome__}.") # eu acesso as propriedades da minha classe assim, com o nome de instância ponto a propriedade que eu quero acessar 
print(f"O nome do curso é {matheus.curso}.")

# INSTÂNCIA 2
lucas = Aluno("Lucas Eduardo Ferreira de Carvalho", "Economia", 0)
print(f"O nome do aluno é {lucas.__nome__}.")
print(f"O nome do curso é {lucas.curso}.")

# para que o objeto seja printável, é necessário definir um método para mostrar pro print oq imprimir. Sem isso, ele printa o local da memória que aquele objeto está armazenado.
# colocar apenas underlines na frente de uma propriedade torna ela oculta, colocar duas underlines no método torna ela oculta.
print(matheus.nome) # é um método que vai contornar os métodos ocultos listados acima, o script desse método está no outro arquivo.
# matrícula é um método oculto, e só usando esses métodos geters abaixo eu consigo acessar essa propriedade. print(matheus.__matricula) não iria funcionar
print(matheus.matricula)
print(lucas.matricula)

matheus.curso = "Direiro Rio" # assim que eu vou acessar o meu SETTER, preciso igualar a oq ele recebe 
print(matheus.curso)

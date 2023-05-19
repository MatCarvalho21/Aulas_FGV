'''
Plano de Hoje:
Criar uma classe Aluno() com propriedades:
- nome
- matrícula
- bolsista
- curso
- notas (tupla com nota e carga horária)
- cr

Métodos:
- get_nome
- get_mat
- set_cr (oculto)
- calcular_cr 
- adicionar_notas
- __init__ (oculto)
'''


matriculas = [0]


class Aluno():

    def __init__(self, nome, curso, bolsa): # vai ser o método construtor, chamado no momento de ativação da classe. O self é um objeto se enxergar no código. Self vai ser o objeto, cada objeto. Dentro do init temos que definir as propriedades.
        self.__nome__ = nome

        self.__matricula = matriculas[-1] + 1
        matriculas.append(self.__matricula)

        self.__curso = curso

        self.__bolsista = bolsa

        self.__notas = None

        self.__cr = None
    ### SEMPRE QUE VOU DEFINIR UM MÉTODO, EU PAÇO O PARÂMETRO SELF

    ### OS GETTERS SÃO SEMPRE DEFINIDOS COM O PROPERTY
    @property # é uma forma de falar com o python que esse não deve ser utilizado, mas quando o usuário pedir ela tem que retornar. 
    def nome(self):
        return self.__nome__
    
    @property # toda vez que for fzer um método que acessa uma propriedade oculta, devo colocar o @property. quando eu tentar acessar, o python executa esse geter e retorna a propriedade. 
    def matricula(self): # é uma boa prática nomear o método get apenas com o nome da variável que pretendemos acessar
        return self.__matricula
    
    @property
    def cr(self):
        return self.__cr
    
    @property
    def curso(self):
        return self.__curso
    
    @curso.setter # assim se define um setter, ele vai ter a função de alterar a propriedade, sem ele não tem como, ele tem ESSA funcao
    def curso(self, curso_novo):
        self.__curso = curso_novo

    @property
    def bolsista(self):
        return self.__bolsista
    @property
    def notas(self):
        return self.__notas
    
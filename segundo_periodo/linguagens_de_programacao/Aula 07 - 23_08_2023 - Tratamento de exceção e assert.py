'''
numero = 890

assert isinstance(numero, int), "Erro, tipo diferente recebido."
# são linhas de código que permitem localizar os erros que estão acontecendo com o script (técnica diagnóstica)
# assert (operador booleano), (mensagem de erro)
assert numero%2==0, "O seu número é ímpar!"


# verificar se o código está rodando no modo depuração (quando o arquivo roda normal, __debug__ é true)
print(__debug__)

if __debug__:
    print("Execução em modo normal")
else:
    print("Execução em modo o otimizado")
    
# o código de fato vai ser rodado no modo otimizado, nunca em modo debugado -o ou -oo para modo otimizado 1 e 2
'''

''' Tratamento
# erro de sintaxe (o código escrito não segue a gramática formal de python)
var -> 0/0
# erro semântico (a grmática está correta, mas não é possíel realizá-la)
var = 0/0

-> para tratar essas exeções, vamos user os blocos try-except

variável = "matheus"

try:
    numero = int(variável)
except ValueError as erro:
    print("Não foi possível converter para inteiro. ->", erro)
except NameError:
    print("A variável variável não está definida.")
except (ZeroDivisionError, OverFlowError): # um except pode tratar várias exceções de uma vez, dando o mesmo tratamento
    print("Nem sei como isso aconteceu, mas aconteceu!")

-> posso enfileirar excepts e dar um tratamento diferente para cada erro

raise ValueError
-> vai levantar uma exceção e com isso acionar um except

-> as classes de erros então umas contidas nas outras, como foi visto em sala 
o erro aritmético engloba o erro de divião por zero, float point e overflow

-> sempre vamos enfileirar excepts dos mais específicos para os mais genéricos
erro.__class__.mro() mostra a onde aquele método está contido
NameError.mro() é a mesma coisa, pois erro.__class__ é no nosso exemplo NameError
'''
'''
variável = "matheus"

try:
    numero = int(variável)
except ValueError as erro:
    print("Não foi possível converter para inteiro. ->", NameError.mro())
except NameError:
    print("A variável variável não está definida.")
    
'''
'''
x = 10
y = 1

try:
    resultado = x/1
except (NameError, ZeroDivisionError) as erro:
    print("Estude na EMAp! Erro:", type(erro), erro.__class__.mro())
else:
    print("Se caiu aqui é porque deu certo!")
finally:
    print("foi uma honra estudar ao seu lado!")
'''
peso = 10
try:
    if peso < 0:
        raise ValueError("O peso deve ser positivo!")
except ValueError: #vai rodar se esse erro for encontrado
    print("Você inseriu um peso inválido, rode o comando novamente.")
else: #vai rodar se nenhuma exceção for acionada
    print("Peso válido! Próximo passo.")
finally: #vai rodar de qualquer jeito 
    print("Muito obrigado por usar esse código top.")

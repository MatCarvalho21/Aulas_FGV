import sys 

sys.path.append("C:\\Users\\B51084\\Aulas_FGV\\segundo_periodo\\linguagens_de_programacao\\modulo")
sys.path = sys.path[0:10]
print(sys.path)

from modulo.modulo import saudacao

saudacao()
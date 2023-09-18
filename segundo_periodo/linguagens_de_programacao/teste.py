import unittest 
import fatorial as ft

# Teste Automatizado X Teste Manual

class TestFactorial(unittest.TestCase): #tô criando uma classe e indicando de onde estou herdando as características, funciona como um árvore

    # Equivalende Partitioning Method
    # Métodos de Partições de Equivalência (dividir o domínio da função e testar cada uma delas)
    # Equivalence Class Partitioning (ECP)
    
    def test_greater_than_1(self):
        self.assertEqual(ft.fatorial(2), 2)
        
    def test_lesser_than_0(self):      
        self.assertEqual(ft.fatorial(-1), 1)
      

   # Boundary Value Analysis ou Boundaryu Value Test (Análise de Valor Limite)
   # Vou testar valores ao entorno do meu limite. No caso da maioridade eram o 17, 18 e 19.
   
    def test_equal_1(self):
        self.assertEqual(ft.fatorial(1), 1)
      
    def test_equal_0(self):
       self.assertEqual(ft.fatorial(0), 1)
   
    # Temos que entender que testar -1 e -100 é a mesma coisa, se formos tentar valores negativos.
    # Note que o teste de 2 vai testar tanto valores maiores que 1, quanto valores no limite de 1.
    
    # Data Type Checking
    # Testagem do Tipo do Dado
    
    def test_input_value_type(self):
        self.assertEqual(ft.fatorial(2.0), 2.0)
        self.assertRaises(TypeError, ft.fatorial, "OI")
                                                             
if __name__ == "__main__":
    unittest.main() #o módulo unittest só vai funcionar se os métodos de teste estiverem dentro de uma classe filha da classe TestCase

'''
# Teste Exploratório
print(ft.fatorial(5))
'''
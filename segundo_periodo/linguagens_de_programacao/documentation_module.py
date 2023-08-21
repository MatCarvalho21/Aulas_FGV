"""Documentação do Módulo (primeira linha especial):

Descriçaõ do Módulo (tudo que for importante descrever) 

"""

# função que calcula o montante e juros em um regime de juros simples
# Type Hint: MyPY (vai avisar se os tipos esperados não estão sendo atendidos)
# TODO: (algo que deva ser alterado mais tarde, mas de forma rápida)
# FIXME: (algo que é necessário resolver em algum momento)

def juros_simples(capital: int, taxa: float, tempo: int) -> tuple:
    """Cálculo  de Juros Compostos
    
    Parameters
    -------------------
    capital: int
        blá-blá-blá
    taxa: float
        blá-blá-blá
    tempo: int
        blá-blá-blá
        
    Returns
    -------------------
    tuple:
        blá-blá-blá

    """
    juros = capital * (taxa/100) * tempo
    montante = capital + juros
    
    return (montante, juros)

def juros_compostos(capital: int, taxa: float, tempo: int) -> tuple:
    """Cálculo  de Juros Compostos
    
    Parameters
    -------------------
    capital: int
        blá-blá-blá
    taxa: float
        blá-blá-blá
    tempo: int
        blá-blá-blá
        
    Returns
    -------------------
    tuple:
        blá-blá-blá

    """
    montante = capital * (pow(1+taxa/100, tempo))
    juros = montante - capital
    
    return (round(montante, 2), round(juros, 2))
    
if __name__ == "__main__":
    print("funcionando")
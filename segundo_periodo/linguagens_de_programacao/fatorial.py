# RECURSIVIDADE

def fatorial(num):
    """
    Parameters
    ----------
    num : INT
            Vai ser um número inteiro que será base do fatorial.

    Returns
    -------
    INT
        Vai retorar um número inteiro, fruto da multiplicação recursiva de valores.

    Examples
    -------
    fatorial(0)
    >>> 1
    
    fatorial(1)
    >>> 1
    
    fatorial(3)
    >>> 6
    """
    if num <= 1:
        return 1

    return num * fatorial(num - 1)


def fibonacci(posição_do_valor):

    if posição_do_valor < 0:
        print("Insira um valor válido.")
        return None
    
    elif posição_do_valor <= 1:
        return 1

    else:
        return fibonacci(posição_do_valor - 1) + fibonacci(posição_do_valor - 2)


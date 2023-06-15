def adicionar_pedido(numero_do_pedido, pedidos_em_preparo):
    pedidos_em_preparo.append(numero_do_pedido)
    print(f"Pedido {numero_do_pedido} adicionado!") 

def preparacao_de_pedidos(pedidos_em_preparo):
    print(f"O pedido {pedidos_em_preparo[0]} está pronto!")
    pedidos_em_preparo.remove(pedidos_em_preparo[0])
    
def listar_pedidos_em_preparo(pedidos_em_preparo):
    for pedido in pedidos_em_preparo:
        print(f"O pedido {pedido} está sendo preparado...")

def verificar_pedido(id_pedido, pedidos_em_preparo):
    if pedidos_em_preparo.count(id_pedido) == 0:
        print("O seu pedido não está sendo preparado. Confira se já está pronto.")
        return 
    else:
        indice = pedidos_em_preparo.index(id_pedido) + 1
        print(f"Sua posição na fila é {indice}")
        
pedidos_em_preparo = []
    
print("Digite 1 para lista pedidos.")
print("Digite 2 para adicionar um pedido.")
print("Digite 3 para preparar um pedido.")
print("Digite 4 para verificar um pedido.")
print("Digite 5 para encerrar o programa.")

while True: 
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        listar_pedidos_em_preparo(pedidos_em_preparo)
        
    elif opcao == 2:
        pedido = int(input("Digite o numero do pedido: "))
        adicionar_pedido(pedido, pedidos_em_preparo)
        
    elif opcao == 3:
        preparacao_de_pedidos(pedidos_em_preparo)
        
    elif opcao == 4:
        pedido = int(input("Digite o numero do pedido: "))
        verificar_pedido(pedido, pedidos_em_preparo)
        
    elif opcao == 5:
        print(opcao)
        break
    else:
        print("Opção incorreta. Digite outra vez.")
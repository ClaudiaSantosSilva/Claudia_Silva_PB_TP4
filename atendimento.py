from menu_atendimento import *
from tabulate import tabulate

def novo_item(produtos, quantidade_item):  
    #quantidade_item vem de def efetuar_atendimento
    produto_escolhido = obter_produto_escolhido()
    
    quantidade_produto_escolhido = obter_quantidade_produto_escolhido(produto_escolhido)
    atualizar_quantidade_estoque(produto_escolhido, quantidade_produto_escolhido)
                
    preco_produto_escolhido = produto_escolhido.preco    
    preco_total_produto_escolhido= preco_produto_escolhido * quantidade_produto_escolhido    
    return Item(quantidade_item + 1,produto_escolhido.nome, quantidade_produto_escolhido, preco_produto_escolhido, preco_total_produto_escolhido)  # é um objeto da classe Item
          
def atendimento(produtos):  
    lista_atendimentos = []  
    opcao_do_caixa = menu_escolher_atendimento()
    numero_cliente = 1
    while opcao_do_caixa != 2:
        match (opcao_do_caixa):
            case 1: #iniciar atendimento
                id_cliente = obter_id_cliente()
                print(f"Cliente: {id_cliente}")
                atendimento = efetuar_atendimento(produtos, numero_cliente)
                lista_atendimentos.append([f"Cliente {numero_cliente}", atendimento])
                numero_cliente+=1
            case _:
                print("Opção inválida") 
        opcao_do_caixa = menu_escolher_atendimento()
    fechar_caixa(lista_atendimentos, produtos) 

def finalizar_atendimento(lista_itens, numero_cliente):
    print("\nFinalizando atendimento")
    print(f"Cliente {numero_cliente}") 
    print(f"{obter_data_hora()}\n")
    #lista_itens é uma lista de lista de objetos gerada no efetuar_atendimento.
    tabela = [["Item", "Produto", "Quant.", "Preço", "Total"]]
    for item in lista_itens:
       #print(item)
       linha = [item.numero_item, item.nome_produto, item.quantidade_produto, item.preco_produto, item.preco_item]
       tabela.append(linha)
    print(tabulate(tabela, headers="firstrow"))   
    print()
    print(f"Itens: {len(lista_itens)}")
    print(f"Total: {sum(item.preco_item for item in lista_itens)}")
    print()
    return numero_cliente

def efetuar_atendimento(produtos, numero_cliente):    
    lista_itens_compra = [] #será lista de objetos (cada novo_item)
    opcao_atendimento = situacao_atendimento() #ter while das opçoes situacao atendimento
    while opcao_atendimento !=2:
        match(opcao_atendimento):
            case 1: #incluir item
                lista_itens_compra.append(novo_item(produtos, len(lista_itens_compra))) #append de 1 item (objeto)
                #print(lista_itens_compra)
            case _:
                print("Opção inválida")
        opcao_atendimento = situacao_atendimento()
    finalizar_atendimento(lista_itens_compra, numero_cliente)
    return lista_itens_compra


            
        
       
            

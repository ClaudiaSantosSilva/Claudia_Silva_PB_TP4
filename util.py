from datetime import datetime
from tabulate import tabulate
from atendimento_db import *

def entrar_inteiro(mensagem):
    while True:
        try:
            numero= int(input(mensagem))
            break
        except Exception:
            print("Erro: valor invalido.")    
    return numero        

def obter_data_hora():
    agora = datetime.now()
    return agora.strftime("%d/%m/%Y %H:%M")

def fechar_caixa(lista_atendimentos, produtos): 
    print("\nFechamento do Caixa")
    print(f"{obter_data_hora()}\n")
    total_vendas = 0
    tabela = [["Cliente", "Total"]]
    for atendimento in lista_atendimentos:
        dado_cliente = atendimento[0] #aqui pego o Cliente numero tal
        dados_compra = atendimento[1] #aqui pego o objeto com o atendimento
        total_compra = sum(item.preco_item for item in dados_compra)
        total_vendas+= total_compra
        tabela.append([dado_cliente, total_compra])
    print(tabulate(tabela, headers="firstrow"))   
    print()    
    print(f"Total de vendas: {total_vendas}") 
    print()
#VERIFICAR PRODUTOS ZERADOS EM PRODUTOS/ESTOQUE
    produtos_zerados = consultar_produtos_zerados_db()
    print("Produtos sem estoque:")
    for produto in produtos_zerados:
        print(produto.nome) 
    print()    

    #gravar_produtos(produtos)    
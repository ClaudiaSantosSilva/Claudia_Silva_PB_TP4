from datetime import datetime
from tabulate import tabulate
from atendimento_db import *
from conexao import *
from models import *
import pandas as pd

def entrar_inteiro(mensagem):
    while True:
        try:
            numero= int(input(mensagem))
            return numero 
            #break
        except Exception:
            print("Erro: valor invalido.")    
    #return numero 

def carregar_clientes_json():
    Base.metadata.create_all(engine) #cria a tabela caso não exista
    df = pd.read_json('clientes.json')
    #with Session(engine) as session:
    with session:
        for _, row in df.iterrows(): # O traço ignora o indice da linha. Row é uma Series com os dados da linha.
            cliente = Cliente(nome=row['nome'])
            session.add(cliente)
        session.commit()
    # with open('clientes.json', 'r', encoding='utf-8') as c:
    #     clientes = json.load(c)
    # with session:
    #     for item in clientes:
    #         cliente = Cliente(nome=item['nome']) 
    #         session.add(cliente)
    #     session.commit()

def obter_id_cliente():
    id= entrar_inteiro("Informe o id do cliente: ")
    cliente = consultar_cliente_db(id)
    return cliente

def obter_produto_escolhido():
    id_produto_escolhido = entrar_inteiro("Informe o id do produto escolhido: ")          
    produto_escolhido = consultar_produto_db(id_produto_escolhido)
    #print(produto_escolhido) #é um 1 único objeto vindo do banco.
    if not produto_escolhido:
        print("Produto não cadastrado") 
        return obter_produto_escolhido()
    return produto_escolhido

def obter_quantidade_produto_escolhido(produto_escolhido):
    quantidade_produto_escolhido = entrar_inteiro("Informe a quantidade do produto: ")    
    if quantidade_produto_escolhido < 0:
        print("Erro: quantidade deve ser maior que zero")
        return obter_quantidade_produto_escolhido(produto_escolhido)
    elif quantidade_produto_escolhido > produto_escolhido.quantidade:
        print("Não há quantidade suficiente em estoque.") 
        return obter_quantidade_produto_escolhido(produto_escolhido)   
    else:             
        return quantidade_produto_escolhido 

def atualizar_quantidade_estoque(produto_escolhido, quantidade_produto_escolhido):
    nova_quantidade = produto_escolhido.quantidade - quantidade_produto_escolhido #ATUALIZAR QUANTIDADE ESTOQUE
    alterar_produto_db(nova_quantidade, produto_escolhido)

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

     


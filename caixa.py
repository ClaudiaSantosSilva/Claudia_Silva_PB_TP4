from util import *
from menu import *
from atendimento import *
from atendimento_db import *

def principal():
    opcao = entrar_opcao()
    while True:
        match (opcao):
            case 1: 
                produtos = consultar_produtos_db() 
                atendimento(produtos)
            case 0: 
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida")
        opcao = entrar_opcao()

principal()                

#FALTANDO REFATORAR E ORGANIZAR AS FUNÇÕES NESSA VERSÃO, CONFORME FEITO NA VERSÃO 1.
#ATUALIZADAS AS QUANTIDADES DOS PRODUTOS NO BANCO DE DADOS, MAS PRECISEI TESTAR E 
#CONSUMI: 1 DO PRODUTO 1 E 2 DO PRODUTO 5. 
#Questão 15: Se houvesse mais de um caixa operando ao mesmo tempo,  
#poderiam ser vendidos produtos já vendidos por outro caixa. Os
#caixas ficariam "competindo" pelos produtos.
#Questão 16: Ainda não sei responder.
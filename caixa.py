#from util import *
#from menu_atendimento import *
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


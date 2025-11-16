from atendimento import *
from webscraping_to_csv import *

def principal():
    opcao = entrar_opcao()
    while True:
        match (opcao):
            case 1: #Abre o caixa
                produtos_csv()
                carregar_produtos_db()
                carregar_json_clientes_db()
                produtos = consultar_produtos_db() 
                atendimento(produtos)
            case 0: 
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida")
        opcao = entrar_opcao()

principal()                


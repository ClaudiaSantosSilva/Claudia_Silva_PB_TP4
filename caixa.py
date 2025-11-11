from atendimento import *

def principal():
    opcao = entrar_opcao()
    while True:
        match (opcao):
            case 1: 
                produtos = consultar_produtos_db() 
                carregar_clientes_json()
                atendimento(produtos)
            case 0: 
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida")
        opcao = entrar_opcao()

principal()                


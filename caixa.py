from atendimento import *

def principal():
    opcao = entrar_opcao()
    while True:
        match (opcao):
            case 1: #Abre o caixa
                #Chamar fç carregar_produtos_db
                produtos = consultar_produtos_db() 
                carregar_json_clientes_db()
                atendimento(produtos)
            case 0: 
                print("Saindo do sistema...")
                break
            case _:
                print("Opção inválida")
        opcao = entrar_opcao()

principal()                


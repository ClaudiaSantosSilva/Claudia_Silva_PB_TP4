from util import *

def entrar_opcao():
    print("*** Supermercado Giant ***")
    print("1 - Abrir o caixa")
    print("0 - Sair do sistema")
    opcao = entrar_inteiro("Digite a opção desejada: ")
    return opcao   

def menu_escolher_atendimento():
    print("Caixa aberto! O que deseja fazer agora?")
    print("1 - Iniciar atendimento")
    print("2 - Fechar o caixa")
    opcao_do_caixa = entrar_inteiro("Digite a opção desejada: ")
    return opcao_do_caixa 
    
def situacao_atendimento():
    print("***Atendimento ***")
    print("1- Incluir item")
    print("2- Finalizar atendimento")
    opcao_atendimento = entrar_inteiro("Que operação deseja realizar?: ")  
    return opcao_atendimento


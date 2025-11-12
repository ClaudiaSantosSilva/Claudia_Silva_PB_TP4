from models import *
from conexao import *
from sqlalchemy.exc import NoResultFound
from sqlalchemy import func

def consultar_produtos_db():
    with session:
        produtos = session.query(Produto).all()
    # produtos = []
    # try:
    #     session = conectar()
    #     produtos = session.query(Produto).all()
    # except Exception as ex:
    #     print(ex)
    # finally:
    #     desconectar(session)
    return produtos

def consultar_cliente_db(id):
    with session:
        try:
            #cliente = session.query(Cliente).where(Cliente.id == id).one()
            cliente = session.query(Cliente).get(id)
            return cliente.nome
        except NoResultFound:
            print("Necessário realizar cadastro. Cliente não encontrado")
            realizar_cadastro_cliente()

def realizar_cadastro_cliente():
    with session:
        maior_id = session.query(func.max(Cliente.id)).scalar() #scalar retorna o valor em si
        novo_id = 1 if maior_id is None else maior_id + 1
        nome = f"Cliente{novo_id}"
        novo_cliente = Cliente(nome)
        session.add(novo_cliente)
        session.commit()
        consultar_cliente_db(novo_id)      

def consultar_produto_db(id):
    with session:
        produto = session.query(Produto).get(id)
        return produto
    # produto = None
    # try:
    #    produto = session.query(Produto).get(id)
    #    #produto = session.query(Produto).where(Produto.id == id).first()
    #    return produto
    # except Exception as ex:
    #     print(ex)     

def alterar_produto_db(nova_quantidade, produto_escolhido):
    #comando = "update produto set quantidade = ? where id = ?;"
    with session:
        session.query(Produto).filter(Produto.id == produto_escolhido.id).update({"quantidade":nova_quantidade})
        session.commit()
    # try:        
    #     session.query(Produto).filter(Produto.id == produto_escolhido.id).update({"quantidade":nova_quantidade})
    #     session.commit()
    # except Exception as ex:
    #     print(ex)
    
def consultar_produtos_zerados_db():
    #comando = "select * from produto where quantidade <= 0;"
    with session:
        produtos_zerados = session.query(Produto).filter(Produto.quantidade <= 0).all()
        return produtos_zerados
    # try:
    #     session = conectar()
    #     produtos_zerados = session.query(Produto).filter(Produto.quantidade <= 0).all() #usando all() já me devolve uma lista
    # except Exception as ex:
    #     print(ex)
    # finally:
    #     desconectar(session)
    # return produtos_zerados 



from models import *
from conexao import *
from sqlalchemy.orm import joinedload

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

def consultar_produto_db(id):
    produto = None
    try:
       session = conectar()
       produto = session.query(Produto).get(id)
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)
    return produto

def alterar_produto_db(nova_quantidade, produto_escolhido):
    #comando = "update produto set quantidade = ? where id = ?;"
    try:
        session = conectar()
        session.query(Produto).filter(Produto.id == produto_escolhido.id).update({"quantidade":nova_quantidade})
        session.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)

def consultar_produtos_zerados_db():
    #comando = "select * from produto where quantidade <= 0;"
    try:
        session = conectar()
        produtos_zerados = session.query(Produto).filter(Produto.quantidade <= 0).all() #usando all() já me devolve uma lista
    except Exception as ex:
        print(ex)
    finally:
        desconectar(session)
    return produtos_zerados 



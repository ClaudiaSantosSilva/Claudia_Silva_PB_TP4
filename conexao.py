import os.path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MERCADO = "mercado.db"
DIR = os.path.dirname(os.path.abspath(__file__))
MERCADO = os.path.join(DIR, MERCADO)

engine = create_engine("sqlite:///" + MERCADO)
Session = sessionmaker(bind=engine)
session = Session()

# def conectar():
#     session = None
#     try:
#         engine = create_engine("sqlite:///" + MERCADO)
#         session = sessionmaker(bind=engine)()
#     except Exception as ex:
#         print(ex)
#     return session

# def desconectar(session):
#     if session:
#         session.close()

# session = conectar()
# desconectar(session)     



     

             
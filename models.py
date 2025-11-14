from sqlalchemy import Column, Integer, String, Float #importar Integer só uma vez...é o tipo de dado
from sqlalchemy.ext.declarative import declarative_base #importar superclasse

Base = declarative_base() #instanciar superclasse
class Produto(Base):
    __tablename__ = "produto"
    id         = Column(Integer, primary_key=True)
    nome       = Column(String)
    quantidade = Column(Integer)
    preco      = Column(Float)

    def __init__(self,id,nome,quantidade,preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def debitar_quantidade(self, quantidade_produto_escolhido):
        self.quantidade -= quantidade_produto_escolhido

    def __str__(self):
       return str(self.id) + " " + self.nome + " " + str(self.quantidade) + " " + str(self.preco)
            
    def __repr__(self):
        return self.__str__()
    
class Item:
    def __init__(self, numero_item, nome_produto, quantidade_produto, preco_produto, preco_item):
        self.numero_item = numero_item
        self.nome_produto = nome_produto
        self.quantidade_produto = quantidade_produto
        self.preco_produto = preco_produto
        self.preco_item = preco_item

    def __str__(self):
       return str(self.numero_item) + " " + self.nome_produto + " " + str(self.quantidade_produto) + " " + str(self.preco_produto) + " " + str(self.preco_item)       
    
    def __repr__(self):
        return self.__str__()
    
class Cliente (Base):
    __tablename__ = "cliente"
    id         = Column(Integer, primary_key=True)
    nome       = Column(String)

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
       return str(self.id) + " " + self.nome

    def __repr__(self):
        return self.__str__()
    
    
from models import Produto

def ler_produtos():
    produtos = [Produto(1,"Produto 1",1,10), Produto(2,"Produto 2",2,20), Produto(3,"Produto 3",3,30), Produto(4,"Produto 4",4,40), Produto(5,"Produto 5",5,50)]
    if not produtos:
        print("O estoque encontra-se vazio")
        exit()
    return produtos


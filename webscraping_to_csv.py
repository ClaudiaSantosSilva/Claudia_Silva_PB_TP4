from urllib.request import urlopen
import pandas as pd
from io import StringIO #para trabalhar com paginas html
from bs4 import BeautifulSoup

URL = "https://pedrovncs.github.io/lindosprecos/produtos.html#"

def acessar_url():
    try:
        html = urlopen(URL)
    except Exception as ex:
        print(ex)
        exit()
    return html

def obter_dados_produtos(bs):
    nomes = []
    quantidades = []
    precos = []

    produtos = bs.find_all('div', class_='card-body') #Pego só a div com as infos todos os produtos
    for produto in produtos:
        nome = produto.find('h5', class_='card-title').text.title().strip()
        #quantidade = produto.find('p').get('data-qtd').strip()
        quantidade = produto.find('p', attrs={'data-qtd': True}).get('data-qtd').strip() #para garantir q pega o valor do atributo
        preco = produto.find('p', class_='card-price').get('data-preco').strip()
        preco_limpo = preco.replace('R$', '').replace('\xa0', '').strip() #\xa0 é o unicode de &nbsp;
        preco_pronto = float(preco_limpo.replace(',', '.'))

        nomes.append(nome)
        quantidades.append(quantidade)
        precos.append(preco_pronto)

    return nomes, quantidades, precos    


html = acessar_url()
bs = BeautifulSoup(html, "html.parser")
#print(bs)

def produtos_csv():
    nomes, quantidades, precos = obter_dados_produtos(bs) #aqui chamo a função para obter as listas das infos
    df = pd.DataFrame({
    "nome": nomes,
    "quantidade": quantidades,
    "preco": precos
    })

    df.to_csv("produtos.csv", index=False, encoding="utf-8")
    
#produtos_csv() # PASSAR CSV PARA BANCO DADOS. CHAMAR ESSA FÇ OU OUTRA ANTES DO ATENDIMENTO COM O CUIDADO DE NÃO REPLICAR A TABELA PRODUTOS
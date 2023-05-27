import requests
from pandas import DataFrame
from bs4 import BeautifulSoup

nomes_html = requests.get('https://www.eurodicas.com.br/nomes-e-sobrenomes-portugueses/').text

nomes = BeautifulSoup(nomes_html, 'html.parser').findAll('li', attrs={'Name': ''}) 

dados = list()

for item in nomes:
    if '<a' not in str(item):
        dados.append(str(item.contents[0])[:-1].split(' ')[0])

print(DataFrame(dados, columns=['Nomes']))

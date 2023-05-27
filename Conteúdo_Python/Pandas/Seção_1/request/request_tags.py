import requests
from bs4 import BeautifulSoup
import pandas as pd

texto_string = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').text # Retorna todo o conteúdo do site


bsp_text = BeautifulSoup(texto_string, 'html.parser') # Recebe a variavel com o conteúdo do site, e como segundo parâmetro, qual tipo de arquivo transformar (Nesse caso passar para HTML)


list_noticias = bsp_text.find_all('span', attrs={'class': 'short-desc'}) # É possível usar o "find_all" para retornar apenas as tags que seguem o filtro
"""
 parametro 1: QUal o tipo de tag deseja procurar; (Nesse caso, a tag SPAN)
 parametro 2: Filtrar as tags que contém quais atributos; (Neste exemplo, as tags que contém como Classe o nome 'Short-desc')
 retorno: Retorna em uma lista todas as tags no site solicitadas segundo os atributos.
"""

dados = list()

for item in list_noticias: # Vai apresentar cada indice dentro da lista com as tags.
    titulo = item.contents[1]
    data = str(item.contents[0].text.strip())+', 2017'
    text = item.contents[2].text
    link = item.find('a')['href'] # "find()": Procurar pelo primeiro indice da tag (Nesse caso, a tag de link "a"). | ['href']: Seleciona no objeto o indice de "href", que irá retornar o atributo URL. 
    
    dados.append((titulo, data, text, link))
    

tabela = pd.DataFrame(dados, columns=['Titulo', 'Data', 'Texto', 'Link'])

print(tabela)

from datetime import datetime
from bs4 import BeautifulSoup
from pandas import DataFrame
import requests

postagens = list()

page = requests.get('https://ge.globo.com/').text

tags = BeautifulSoup(page, 'html.parser').find_all('div', attrs={'class': 'feed-post-body'})

for i in tags:
    if ('📺' in str(i)): # Condição adicionada por haver um elemento fastasma
        continue
    
    manchete = i.find('span', attrs={'class': 'feed-post-header-chapeu'}).text
    
    descricao = i.find('div', attrs={'class': 'feed-post-body-title gui-color-primary gui-color-hover'}).text
    
    url = i.find('a').get('href')
    
    secao = i.find('span', attrs={'class': 'feed-post-metadata-section'}).text
    
    data_atual = datetime.now().strftime(r'%d-%m-%Y %H:%M')
    
    inter_publi = i.find('span', attrs={'class': 'feed-post-datetime'}).text
    
    postagens.append({
        'Manchete': manchete,
        'Descrição': descricao,
        'Link': url,
        'Seção': secao,
        'Hora extração': data_atual, 
        'Time delta': inter_publi
    })

print(DataFrame(postagens))

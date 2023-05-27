import pandas as pd

tabela_html = pd.read_html(
    io=r'https://www.homehost.com.br/blog/criar-sites/tabela-html/' 
) # retorna as tabelas do site em uma lista.

print(tabela_html[0])

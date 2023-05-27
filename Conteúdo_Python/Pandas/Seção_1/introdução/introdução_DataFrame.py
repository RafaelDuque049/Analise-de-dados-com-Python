import pandas as pd

nomes = {
    '3': 'Marcos',
    '2': 'Julio',
    '5': 'Ana'
}

print(pd.Series(data=nomes), f'\n{"=="*40}\n')

"""
Data = dado(s) a ser recebidos
columns = Nome da coluna (O parâmetro deve receber o nome dentro de uma lista)
index = indice
"""

"========================================================================================================="


lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]

dados = list(zip(lista_nomes, lista_idades, lista_cpfs, lista_emails))

dados = pd.DataFrame(dados, columns=['Nome', 'Idade', 'CPF', 'Email'])

print(dados, f'\n{"=="*40}\n')

# print(pd.DataFrame(list(zip(lista_nomes, lista_idades, lista_cpfs, lista_emails)), columns=['Nome', 'Idade', 'CPF', 'Email']).loc[4])

"========================================================================================================="
# Utilizando bibliotecas em DataFrame

listas = {
    "Nome": 'Howard Ian Peter Jonah Kellie Julio Marcos'.split(),
    "Idade": [32, 22, 25, 29, 38, 45, 12],
    "CPF": '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55 666.666.666-66 777.777.777-77'.split(),
    "Email": 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk eget.dictum.placerat@necluctus.co.uk eget.dictum.placerat@necluctus.co.uk'.split()
}

dados = pd.DataFrame(listas)

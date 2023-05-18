from pandas import Series, DataFrame

from random import randint as rd

listas = {
    "Nome": 'Howard Ian Peter Jonah Kellie Julio Marcos'.split(),
    "Idade": [32, 22, 25, 29, 38, 45, 12],
    "CPF": '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55 666.666.666-66 777.777.777-77'.split(),
    "Email": 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk eget.dictum.placerat@necluctus.co.uk eget.dictum.placerat@necluctus.co.uk'.split()
}

dados = Series([rd(1, 1000) for x in range(rd(10, 200))])
dados2 = DataFrame(listas)

print('\nMaximo:', dados.max())
print('\nminimo:', dados.min())
print('\nMediana:', dados.median())
print('\nMédia', dados.mean())
print('\nPadrão linear:', dados.std())
print('\nValores únicos:', dados.is_unique)
print('Quantidade:', dados.shape)
print('\nQuantidade de itens com retorno em tupla:', dados2.shape)
print('\nQuantidade de itens:\n', dados2.count())
print('\nDado na segunda posição do DataFrame:\n', dados2.loc[1])
print('\nColuna nome:\n', dados2.Nome)
print('\nColuna nome e idade:\n', dados2[['Nome', 'Idade']])
print('\nInformações do DataFrame:\n')
print(dados2.info())
print('\nDescrição dos valores no DataFrame:\n', dados2.describe())
print('\nOs primeiros 5 dados do DataFrame:\n', dados2.head())

print('\nIAN:', dados2.Nome.loc[1]) # Forma 1 (Recomendado)
print('IAN:', dados2.loc[1]['Nome']) # Forma 2

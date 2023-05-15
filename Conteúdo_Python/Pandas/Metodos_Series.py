import pandas as pd

from random import randint as rd

lista = pd.Series([rd(0, 5000) for num in range(100)])

print(lista, '\n')

"""
new_list = pd.Series(sorted(lista))
mediana = (new_list.loc[int(new_list.count()/2)-1]+new_list.loc[int(new_list.count()/2)])/2 # Calculo de extração da mediana    
"""

# Lista de comandos necessários para Series no Pandas:

print('Número de linhas:', lista.shape) # Retorna o número de linhas em tupla.

print('O tipo de dados é:', lista.dtypes) # Retorna a tipagem dos dados no objeto

print('Os valores são únicos:', lista.is_unique) # Verifica se todos os Objetos são únicos.

print('Valor da posição 2: ', lista.loc[2]) # Localizar valor segundo seu rótulo(indice).

print('Menor valor do Objeto:', lista.min()) # Retorna o menor valor do Objeto.

print('O maior valor do Objeto:', lista.max()) # Retorna o maior valor do Objeto.

print('Quantidade de itens:', lista.count()) # Retorna o valor de itens no Objeto.

print('A mediana dos valores é:', lista.median()) # Retorna a média dos valores na lista.

print('A média dos valores é:', lista.mean()) # retorna a média do objeto.

print('Desvio padrão da séria:', lista.std()) # Extrai o desvio padrão de uma série numérica. (O desvio padrão é uma medida que expressa o grau de dispersão de um conjunto de dados.)

print('\nDescrição\n', lista.describe()) # retorna em forma de objeto todas as informações acima

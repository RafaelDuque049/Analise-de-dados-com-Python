import pandas as pd

Series = pd.Series(data='Primeiro item') # Series() : Vetor de dados Unidimensional(uma dimensão, neste caso em horizontal).
# Output: 0    Primeiro item
print(Series)


Series2 = pd.Series('Primeiro item') # também pode ser adicionado um dado sem necessidade de expecificar que é um item.
# Output: 0    Primeiro item
print(Series2, '\n')


Series3 = pd.Series(data=100) # Um valor inteiro será dado como tipo de dado(dtype) "int64".
# Output: 0    100 
# dtype: int64 


# Itens com index segundo listas.
lista1 = 'Howard Ian Peter Jonah Kellie'.split()
lista2 = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()

print(pd.Series(data= lista1, index= lista2))

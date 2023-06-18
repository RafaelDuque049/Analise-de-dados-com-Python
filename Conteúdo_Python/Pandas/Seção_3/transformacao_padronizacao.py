import pandas as pd
from datetime import date


api_json = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json')

"======================================================================="

# drop_duplicates() = Remover valores repetidos.
no_duplicate = api_json.drop_duplicates(
    keep='last', # keep (manter): 'firts' o primeiro valor se manter no DF | 'last' o último valor continuará no DF.
    inplace=True, # inplace (substituir): Quanto recebe valor "True", atualiza o DF especificado.
    subset=['valor'] # Define que apartir dessas colunas que a linhas devem ser apagadas.
)

print(api_json.info())

"======================================================================="
#Criar uma nova coluna

# DataFrame['NomeColuna'] = valor/array : Adicionar uma nova coluna ao DF.
api_json['data extração'] = date.today()
api_json['responsavel'] = 'rAfaAL'

print(api_json)

"======================================================================="
# Trasformar em Datas

  # to_datatime() 
api_json['data'] = pd.to_datetime(api_json['data'], dayfirst=True)

print(api_json.info())

  # astype()
api_json['data extração'] = api_json['data extração'].astype('datetime64[ns]')

print(api_json.info())

print(api_json)

"======================================================================="
# Padronizar strings de colunas

mod = api_json['responsavel'].str # .str = Selecionar as Strings do Series

api_json['responsavel'] = mod.title() # Definindo que todas as strings sejam em maiusculas

# api_json['responsavel'] = api_json['responsavel'].str.upper() # formato resumido

print(api_json)

"======================================================================="
# Método de organização (Sort_values())
 
api_json.sort_values(
    by='data', # Definir qual coluna sera usada como parâmetro para organizar o DataFrame
    ascending=False, # Quando "True", indica que deseja organizar de forma Crescente.
    inplace=True # Como já citado em outro método, é usado para definir que deseja substituir o DF original.
)

print(api_json)

"======================================================================="

api_json.reset_index(
  drop=True, # Não criar uma nova coluna para os novos indices
  inplace=True # Substituir o DF existente
)

print(api_json)

new_json = api_json.set_index(
  keys='data', # Lista/Nome da coluna para substituir os indices.
  # inplace=True # Substituir o DF existente.
  drop=True # Drop: Quando recebendo True, remove a coluna selecionada para substituir os indices.
)

print(new_json)

"======================================================================="
# Indice de extremos valores de uma DF

print(api_json['valor'].idxmax()) # Retorna o indice do maior valor da coluna.

print(api_json.valor.idxmin()) # Retorna o indice do maior valor da coluna.

"======================================================================="
# Filtrar dados

min_data = pd.to_datetime('2022-01-01')
max_data = pd.to_datetime('2022-05-01')

# Filtro usando '&' = AND(E)
print(api_json.loc[
  (api_json['data'] > min_data) # primeia operação lógica: Apenas será apresentado se a data for maior que o min_data;
  & # & = And(e): Adicionar duas condições; (Para usa-lá, é necessário as operações estarem em parenteses)
  (api_json['data'] < max_data) # Segunda operação lógica: Vai ser apresentada apenas se a data for menor que max_data;
  ]
)
# print(api_json.loc[(api_json.data > min_data) & (api_json.data < max_data)])


# Filtro usando | = OR(OU)
print(api_json.loc[
  (api_json.valor < .02) # Primeira operação lógica: Valor vai ser disponível apenas de for menor que 0.02
  | # operador | = OR(OU) = Operador para definir se uma das operações retornar True, se dá como verdadeiro;
  (api_json.valor > .1) # Segunda operação lógica: valor vai ser disponível apenas se for maior que 0.1
  ]
)
# print(api_json.loc[(api_json.valor < .02) | (api_json.valor > .1)])

# Retorna valores filtrados de apenas uma coluna

print(api_json.loc[
  api_json.valor > 0.1, # Filtro a ser aplicado.
  'valor' # Nome da coluna que deseja retorna os valores filtrados.
  ]
)

"======================================================================="
# Deletar colunas do DF

api_json.drop(
  columns=['data extração', 'responsavel'], # Colunas que deseja remover;
  inplace=True # Atualizar o DF a ser modificado
)

print(api_json)

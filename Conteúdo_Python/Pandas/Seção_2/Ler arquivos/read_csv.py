import pandas as pd

file_csv = pd.read_csv(
    filepath_or_buffer=r'https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv', # Caminho do arquivo ou página csv.                 
    sep=',', # Tipo de separação por coluna do arquivo csv. (default: ',')
    index_col="LatD" # Definir uma coluna que vai usada como indíce.
)

print(file_csv)

import pandas as pd

api_json = pd.read_json(
    path_or_buf='https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json' # Caminho do arquivo ou página a extrair o json.
)

print(api_json)

from pandas import DataFrame

listas = {
    "Nome": 'Howard Ian Peter Jonah Kellie Julio Marcos'.split(),
    "Idade": [32, 22, 25, 29, 38, 45, 12],
    "CPF": '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55 666.666.666-66 777.777.777-77'.split(),
    "Email": 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk eget.dictum.placerat@necluctus.co.uk eget.dictum.placerat@necluctus.co.uk'.split()
}

dados = DataFrame(listas)

print('\nInformações do DataFrame:')
print(dados.info()) # Mostrar informações sobre o DataFrame;

print('\nDescrição:\n', dados.describe()) # Fazer uma descrição dos itens no DataFrame;

print('\nPrimeiros 5 itens:\n', dados.head()) # Apresenta apenas os primeiros 5 indices de dados;

print("\nMaior idade:", dados.Idade.max()) # Selecionar a coluna Idade para uso de métodos;
print("Menor idade:", dados['Idade'].min()) # Selecionar a coluna Idade para uso de métodos;

print('\n', dados[['Nome', 'Idade']]) # Selecionar mais de uma coluna para uso;
print(dados.get(['Nome', 'Idade', 'Email'])) # Mesmo funcionamento do metodo acima, mas utilizando "get()";

dados.update(('Josias', 21, '122.122.122-12', 'josias.046@gmail.com')) # Adiciona mais dados ao DataFrame;
print('\n', dados, '\n')

new_list = [
    ('Ana', 21, '122.100.122-12', 'ana.046@gmail.com'),
    ('Alessando', 21, '122.122.452-12', 'josofws.046@gmail.com'),
    ('Marquinhos', 21, '122.422.122-12', 'josis.046@gmail.com')
]

new_list = DataFrame(new_list, columns=['Nome', 'Idade', 'CPF', 'Email'])

dados.update(new_list, overwrite=True)

dados.drop(columns=['CPF'], inplace=True) # Deletar uma coluna e atualizar o DF
print(dados)
